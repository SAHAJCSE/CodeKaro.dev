import collections
import json
import os
import re
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import unquote, urlparse

try:
    from runner.core import (
        MAX_REQUEST_BYTES,
        get_problem_ids,
        is_valid_problem,
        run_solution,
    )
except ImportError:
    from core import (
        MAX_REQUEST_BYTES,
        get_problem_ids,
        is_valid_problem,
        run_solution,
    )

DEFAULT_ORIGINS = "https://oops-judge.vercel.app,http://localhost:8080,http://127.0.0.1:8080,http://localhost:3000"
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", DEFAULT_ORIGINS).strip()
PORT = int(os.environ.get("PORT", "8000"))

# Security limits: rate limiting (20 runs/min/IP) and concurrency cap (2)
RATE_LIMIT_WINDOW_SECONDS = 60
MAX_RUNS_PER_MINUTE = 20
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "judge_verify_secret")
_rate_limit_lock = threading.Lock()
_ip_request_history = collections.defaultdict(list)

MAX_CONCURRENT_RUNS = 2
CONCURRENCY_TIMEOUT_SECONDS = 20.0
_concurrency_semaphore = threading.Semaphore(MAX_CONCURRENT_RUNS)


def check_rate_limit(client_ip: str) -> tuple[bool, str | None]:
    """Sliding-window IP rate limiter: max 20 runs per minute."""
    now = time.time()
    cutoff = now - RATE_LIMIT_WINDOW_SECONDS
    with _rate_limit_lock:
        history = [t for t in _ip_request_history[client_ip] if t > cutoff]
        if len(history) >= MAX_RUNS_PER_MINUTE:
            _ip_request_history[client_ip] = history
            return False, f"Rate limit exceeded (maximum {MAX_RUNS_PER_MINUTE} runs per minute). Please wait a moment before trying again."
        history.append(now)
        _ip_request_history[client_ip] = history
        return True, None


def get_allowed_origin(request_origin: str | None) -> str:
    """Determine the Access-Control-Allow-Origin header value."""
    if ALLOWED_ORIGINS == "*":
        return "*"
    if not request_origin:
        return ALLOWED_ORIGINS.split(",")[0].strip() if ALLOWED_ORIGINS else "*"
    allowed_list = [o.strip() for o in ALLOWED_ORIGINS.split(",") if o.strip()]
    if request_origin in allowed_list:
        return request_origin
    return allowed_list[0] if allowed_list else "*"


class RunnerHandler(BaseHTTPRequestHandler):
    def send_bytes(self, status: int, body: bytes, content_type: str = "application/json; charset=utf-8"):
        origin = self.headers.get("Origin")
        allowed_origin = get_allowed_origin(origin)

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", allowed_origin)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status: int, payload: dict):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_bytes(status, body, "application/json; charset=utf-8")

    def do_OPTIONS(self):
        origin = self.headers.get("Origin")
        allowed_origin = get_allowed_origin(origin)

        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", allowed_origin)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

    def read_json_body(self) -> tuple[dict | None, int | None, str | None]:
        """
        Read and validate JSON body.
        Returns (payload, status_code, error_message).
        """
        content_length_header = self.headers.get("Content-Length")
        if not content_length_header:
            return None, 400, "Missing Content-Length header."
        try:
            length = int(content_length_header)
        except ValueError:
            return None, 400, "Invalid Content-Length header."

        if length < 0:
            return None, 400, "Negative Content-Length."
        if length > MAX_REQUEST_BYTES:
            return None, 413, f"Payload too large. Maximum size is {MAX_REQUEST_BYTES // 1024}KB."

        raw_data = self.rfile.read(length)
        try:
            payload = json.loads(raw_data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            return None, 400, "Request body must be valid UTF-8 JSON."

        if not isinstance(payload, dict):
            return None, 400, "Request body must be a JSON object."

        return payload, None, None

    def do_GET(self):
        path = unquote(urlparse(self.path).path).rstrip("/")

        # Health check endpoints: /health or /api/health
        if path in ("/health", "/api/health", ""):
            self.send_json(200, {"status": "ok"})
            return

        # List problems count
        if path in ("/problems", "/api/problems"):
            self.send_json(200, {
                "status": "ok",
                "problems_count": len(get_problem_ids()),
                "problems": get_problem_ids(),
            })
            return

        self.send_json(404, {"error": "Endpoint not found."})

    def get_client_ip(self) -> str:
        """Extract client IP address, supporting X-Forwarded-For when behind proxy."""
        forwarded = self.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return self.client_address[0] if self.client_address else "127.0.0.1"

    def do_POST(self):
        path = unquote(urlparse(self.path).path).rstrip("/")

        # Match /problems/{id}/run or /api/problems/{id}/run
        match = re.fullmatch(r"(?:/api)?/problems/([a-z0-9-]+)/run", path)
        if match is None:
            self.send_json(404, {"error": "Endpoint not found. Use POST /problems/{id}/run."})
            return

        problem_id = match.group(1)
        if not is_valid_problem(problem_id):
            self.send_json(404, {"error": f"Problem '{problem_id}' not found."})
            return

        payload, err_status, err_msg = self.read_json_body()
        if err_status is not None:
            self.send_json(err_status, {"error": err_msg})
            return

        code = payload.get("code")
        if not isinstance(code, str):
            self.send_json(400, {"error": "The 'code' field is required and must be a string."})
            return

        raw_mode = payload.get("mode")
        if raw_mode is None:
            mode = "run"
        elif not isinstance(raw_mode, str) or raw_mode.lower().strip() not in ("run", "submit"):
            self.send_json(400, {"error": "The 'mode' field must be either 'run' or 'submit'."})
            return
        else:
            mode = raw_mode.lower().strip()

        # Step 1: Check IP rate limit (20 runs/minute) unless verified batch test runner token is supplied
        verify_header = self.headers.get("X-Verify-Token")
        is_verified = bool(VERIFY_TOKEN and verify_header and verify_header == VERIFY_TOKEN)

        if not is_verified:
            client_ip = self.get_client_ip()
            allowed, rate_err = check_rate_limit(client_ip)
            if not allowed:
                self.send_json(429, {
                    "status": "RATE_LIMITED",
                    "error": rate_err,
                })
                return

        # Step 2: Global concurrency queue (max 2 concurrent runs, max 20s queue wait)
        acquired = _concurrency_semaphore.acquire(timeout=CONCURRENCY_TIMEOUT_SECONDS)
        if not acquired:
            self.send_json(429, {
                "status": "RATE_LIMITED",
                "error": f"Server is currently at maximum capacity ({MAX_CONCURRENT_RUNS} concurrent runs). Queued request timed out after waiting {int(CONCURRENCY_TIMEOUT_SECONDS)}s. Please try again.",
            })
            return

        try:
            result = run_solution(problem_id, code, mode=mode)
            self.send_json(200, result)
        except OSError as exc:
            self.send_json(503, {"error": f"Execution environment error: {exc}"})
        except Exception as exc:
            self.send_json(500, {"error": f"Internal runner error: {exc}"})
        finally:
            _concurrency_semaphore.release()

    def log_message(self, format_string, *args):
        # Format clean runner logs to stdout
        sys.stdout.write(f"[runner] {self.address_string()} - {format_string % args}\n")
        sys.stdout.flush()


def run_server(port: int = PORT):
    server = ThreadingHTTPServer(("0.0.0.0", port), RunnerHandler)
    print(f"OOPS Judge Runner started on http://0.0.0.0:{port}")
    print(f"Allowed CORS Origins: {ALLOWED_ORIGINS}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down runner server.")
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()
