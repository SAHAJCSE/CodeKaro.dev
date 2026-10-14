#!/usr/bin/env python3
"""Start the local browser app for the OOPS Java practice problems."""
import argparse
import json
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
WEB = ROOT / "public" if (ROOT / "public").is_dir() else ROOT / "web"
PROBLEMS = ROOT / "problems"
PROBLEM_ID = re.compile(r"^[a-z0-9-]+$")
MAX_REQUEST_BYTES = 1_000_000


def get_problem_ids():
    return sorted(path.name for path in PROBLEMS.iterdir() if path.is_dir())


def get_problem(problem_id):
    if not PROBLEM_ID.fullmatch(problem_id) or problem_id not in get_problem_ids():
        return None

    problem_dir = PROBLEMS / problem_id
    readme = (problem_dir / "README.md").read_text(encoding="utf-8")
    title = next(
        (line[2:].strip() for line in readme.splitlines() if line.startswith("# ")),
        problem_id.replace("-", " ").title(),
    )
    summary = next(
        (
            line.strip()
            for line in readme.splitlines()
            if line.strip() and not line.startswith("#") and not line.startswith("*Source:")
        ),
        "",
    )
    solution = (problem_dir / "Solution.java").read_text(encoding="utf-8")
    return {
        "id": problem_id,
        "title": title,
        "summary": summary,
        "readme": readme,
        "solution": solution,
    }


class AppHandler(BaseHTTPRequestHandler):
    def send_bytes(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, payload):
        body = json.dumps(payload).encode("utf-8")
        self.send_bytes(status, body, "application/json; charset=utf-8")

    def read_json(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "Invalid Content-Length header."})
            return None
        if length < 0 or length > MAX_REQUEST_BYTES:
            self.send_json(413, {"error": "Request body must be under 1 MB."})
            return None
        try:
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "Request body must be valid UTF-8 JSON."})
            return None
        if not isinstance(payload, dict):
            self.send_json(400, {"error": "Request body must be a JSON object."})
            return None
        return payload

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path == "/api/problems":
            problems = []
            for problem_id in get_problem_ids():
                problem = get_problem(problem_id)
                problems.append({
                    "id": problem["id"],
                    "title": problem["title"],
                    "summary": problem["summary"],
                })
            self.send_json(200, {"problems": problems})
            return

        if path.startswith("/api/problems/"):
            problem_id = path[len("/api/problems/"):]
            problem = get_problem(problem_id)
            if problem is None:
                self.send_json(404, {"error": "Problem not found."})
                return
            self.send_json(200, problem)
            return

        static_files = {
            "/": ("index.html", "text/html; charset=utf-8"),
            "/index.html": ("index.html", "text/html; charset=utf-8"),
            "/app.css": ("app.css", "text/css; charset=utf-8"),
            "/app.js": ("app.js", "text/javascript; charset=utf-8"),
        }
        if path not in static_files:
            self.send_json(404, {"error": "Page not found."})
            return
        filename, content_type = static_files[path]
        try:
            body = (WEB / filename).read_bytes()
        except OSError as error:
            self.send_json(500, {"error": f"Could not read app file: {error}"})
            return
        self.send_bytes(200, body, content_type)

    def do_POST(self):
        path = unquote(urlparse(self.path).path)
        match = re.fullmatch(r"/api/problems/([a-z0-9-]+)/(save|run)", path)
        if match is None:
            self.send_json(404, {"error": "Endpoint not found."})
            return
        problem_id, action = match.groups()
        if problem_id not in get_problem_ids():
            self.send_json(404, {"error": "Problem not found."})
            return

        payload = self.read_json()
        if payload is None:
            return
        source = payload.get("code")
        if not isinstance(source, str):
            self.send_json(400, {"error": "The 'code' field must be a string."})
            return

        try:
            (PROBLEMS / problem_id / "Solution.java").write_text(source, encoding="utf-8")
        except OSError as error:
            self.send_json(500, {"error": f"Could not save Solution.java: {error}"})
            return
        if action == "save":
            self.send_json(200, {"saved": True})
            return

        try:
            result = subprocess.run(
                [sys.executable, str(ROOT / "judge.py"), problem_id],
                cwd=ROOT,
                capture_output=True,
                text=True,
                timeout=90,
                check=False,
            )
        except subprocess.TimeoutExpired as error:
            output = error.stdout or ""
            if isinstance(output, bytes):
                output = output.decode("utf-8", errors="replace")
            self.send_json(200, {
                "saved": True,
                "passed": False,
                "exitCode": None,
                "output": output + "\nJudge timed out after 90 seconds.",
                "error": "The judge took too long to finish.",
            })
            return
        except OSError as error:
            self.send_json(503, {"error": f"Could not start the judge: {error}"})
            return

        output = result.stdout
        if result.stderr:
            output = f"{output}{result.stderr}"
        self.send_json(200, {
            "saved": True,
            "passed": result.returncode == 0,
            "exitCode": result.returncode,
            "output": output.strip(),
        })

    def log_message(self, format_string, *args):
        print(f"[app] {self.address_string()} - {format_string % args}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000, help="local web server port (default: 8000)")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("--port must be between 1 and 65535")

    server = ThreadingHTTPServer(("127.0.0.1", args.port), AppHandler)
    print(f"OOPS Judge is running at http://127.0.0.1:{args.port}")
    print("Keep this terminal open while using the app. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping OOPS Judge.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
