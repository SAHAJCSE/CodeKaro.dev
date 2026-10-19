"""Vercel Serverless Function entry point for the Code-Karo.dev API."""
import json
import os
import re
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, unquote, urlencode, urlparse

try:
    from api.problems_data import PROBLEMS
except ImportError:
    try:
        from problems_data import PROBLEMS
    except ImportError:
        PROBLEMS = {}

MAX_REQUEST_BYTES = 1_000_000


class handler(BaseHTTPRequestHandler):
    def send_bytes(self, status, body, content_type):
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store, max-age=0")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_bytes(status, body, "application/json; charset=utf-8")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def get_effective_path(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        # 1. From rewrite query ?path=$1
        if "path" in query and query["path"] and query["path"][0]:
            subpath = query["path"][0].strip("/")
            return f"/api/{subpath}"

        # 2. From Vercel routing headers
        for h in ("x-matched-path", "x-invoke-path", "x-forwarded-uri"):
            val = self.headers.get(h)
            if val:
                hp = unquote(urlparse(val).path).rstrip("/")
                if hp.startswith("/api"):
                    return hp

        # 3. Direct path
        raw = unquote(parsed.path).rstrip("/")
        if raw.endswith("/index.py"):
            raw = raw[:-len("/index.py")].rstrip("/")
        return raw or "/api"

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
        path = self.get_effective_path()
        if path in ("", "/api"):
            self.send_json(200, {
                "status": "ok",
                "app": "Code-Karo.dev API",
                "problems_count": len(PROBLEMS)
            })
            return

        if path == "/api/problems":
            problem_list = [
                {
                    "id": p["id"],
                    "title": p["title"],
                    "summary": p["summary"],
                    "difficulty": p.get("difficulty", "Easy"),
                    "topics": p.get("topics", []),
                }
                for p in sorted(PROBLEMS.values(), key=lambda x: x["id"])
            ]
            self.send_json(200, {"problems": problem_list})
            return

        if path == "/api/github-callback":
            query = parse_qs(urlparse(self.path).query)
            code_val = query.get("code", [None])[0]

            if not code_val:
                self.send_json(400, {"error": "Missing code parameter."})
                return

            client_id = os.environ.get("GITHUB_CLIENT_ID", "")
            client_secret = os.environ.get("GITHUB_CLIENT_SECRET", "")

            if not client_id or not client_secret:
                self.send_json(501, {
                    "error": "GitHub OAuth not configured on server. Set GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET."
                })
                return

            try:
                import urllib.request

                token_data = urlencode({
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "code": code_val,
                }).encode("utf-8")

                req = urllib.request.Request(
                    "https://github.com/login/oauth/access_token",
                    data=token_data,
                    headers={"Accept": "application/json"},
                    method="POST",
                )

                with urllib.request.urlopen(req, timeout=10) as resp:
                    token_json = json.loads(resp.read())

                access_token = token_json.get("access_token")

                if not access_token:
                    self.send_json(401, {
                        "error": token_json.get(
                            "error_description",
                            "Token exchange failed."
                        )
                    })
                    return

                user_req = urllib.request.Request(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"Bearer {access_token}",
                        "Accept": "application/vnd.github+json",
                        "User-Agent": "CodeKaro-App",
                    },
                )

                with urllib.request.urlopen(user_req, timeout=10) as resp:
                    user_json = json.loads(resp.read())

                self.send_json(200, {
                    "access_token": access_token,
                    "user": user_json
                })
                return

            except Exception as exc:
                self.send_json(500, {
                    "error": f"GitHub OAuth error: {exc}"
                })
                return

        if path.startswith("/api/problems/"):
            problem_id = path[len("/api/problems/"):]
            problem = PROBLEMS.get(problem_id)

            if problem is None:
                self.send_json(
                    404,
                    {"error": f"Problem '{problem_id}' not found."}
                )
                return
            self.send_json(200, problem)
            return

        # Fallback static file serving if a static request reaches the serverless function
        clean = path.strip("/")
        if clean.startswith("web/"):
            clean = clean[4:]
        if clean.startswith("public/"):
            clean = clean[7:]
        if clean in (
            "", "index.html",
            "auth", "auth.html",
            "problems", "problems.html", "problems.css", "problems.js",
            "practice", "practice.html",
            "profile", "profile.html",
            "about", "about.html", "about.css", "about.js",
            "team.js", "team.json",
            "app.css", "app.js", "config.js",
        ):
            file_name = clean or "index.html"

            if file_name in ("auth",):
                file_name = "auth.html"
            elif file_name == "problems":
                file_name = "problems.html"
            elif file_name == "practice":
                file_name = "practice.html"
            elif file_name == "profile":
                file_name = "profile.html"
            elif file_name == "about":
                file_name = "about.html"

            content_types = {
                "index.html": "text/html; charset=utf-8",
                "auth.html": "text/html; charset=utf-8",
                "problems.html": "text/html; charset=utf-8",
                "problems.css": "text/css; charset=utf-8",
                "problems.js": "application/javascript; charset=utf-8",
                "practice.html": "text/html; charset=utf-8",
                "profile.html": "text/html; charset=utf-8",
                "about.html": "text/html; charset=utf-8",
                "about.css": "text/css; charset=utf-8",
                "about.js": "application/javascript; charset=utf-8",
                "team.js": "application/javascript; charset=utf-8",
                "team.json": "application/json; charset=utf-8",
                "app.css": "text/css; charset=utf-8",
                "app.js": "application/javascript; charset=utf-8",
                "config.js": "application/javascript; charset=utf-8",
            }
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            for folder in ("public", "web"):
                file_path = os.path.join(base_dir, folder, file_name)
                if os.path.isfile(file_path):
                    try:
                        with open(file_path, "rb") as f:
                            self.send_bytes(200, f.read(), content_types.get(file_name, "text/plain"))
                        return
                    except Exception:
                        pass

        self.send_json(404, {
            "error": "Endpoint not found.",
            "resolved_path": path,
            "raw_path": self.path
        })

    def do_POST(self):
        path = self.get_effective_path()
        match = re.fullmatch(r"/api/problems/([a-z0-9-]+)/(save|run)", path)
        if match is None:
            self.send_json(404, {
                "error": "Endpoint not found.",
                "resolved_path": path,
                "raw_path": self.path
            })
            return

        problem_id, action = match.groups()
        if problem_id not in PROBLEMS:
            self.send_json(404, {"error": f"Problem '{problem_id}' not found."})
            return

        payload = self.read_json()
        if payload is None:
            return
        source = payload.get("code")
        if not isinstance(source, str):
            self.send_json(400, {"error": "The 'code' field must be a string."})
            return

        if action == "save":
            self.send_json(200, {
                "saved": True,
                "note": "Saved (saved in browser local storage and preview session)."
            })
            return

        self.send_json(400, {
            "error": "Code execution is hosted on the runner backend. Please configure RUNNER_URL."
        })
