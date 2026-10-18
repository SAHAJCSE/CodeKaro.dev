TASK: restyle ONLY the About page main content (everything between the header and the footer) using the design direction below. Edit only about.html, about.css and about.js. Do not touch the header, footer, nav, Home, Profile, Practice or any shared file. Smallest edits needed, no new sections, no copy changes, no logic changes. Report what you changed and stop.

REFERENCE: a dark landing hero with a bold white sans headline whose second line is a soft lavender-to-pink gradient, a large gray paragraph, a pastel-gradient primary button with dark text and an icon, a dark outlined secondary button, small monospace labels, and a faint grid on a near-black background. Use it for mood only. Do not copy its words, badge, logos or layout exactly.

1. Fonts (one family for all main content)
   - Load "Inter" (weights 400, 500, 600, 800) from Google Fonts with display=swap and a system-ui fallback. Use it for every heading, paragraph, button and card text between the header and the footer.
   - Load "JetBrains Mono" (weights 400, 500) for small labels only: the "// ABOUT" and "// TEAM" labels, the workspace panel, and chips.
   - Remove the wide display font from this page's main content. Headings: weight 800, letter-spacing -0.03em, line-height 1.05. Body: 400, line-height 1.6. No text-shadow, no all-caps except the small mono labels.
   - Sizes: h1 clamp(44px, 7vw, 84px); h2 clamp(30px, 4vw, 48px); lead paragraph 20px; body 16px; mono labels 12 to 13px.

2. Background and theme
   - Page background near-black (#0a0a0b) with a faint grid: 1px lines at rgba(255,255,255,0.04) every 64px, faded out toward the edges and bottom with a CSS mask.
   - Keep Home's animated character field but only inside the hero, at 8% opacity maximum, so About still feels related to Home. Remove the purple gradient and the dark rounded card behind the hero text (the card is no longer needed).
   - Colors: headings #ffffff, paragraph #a1a1aa, hairline borders rgba(255,255,255,0.12), panel background #101012. Accent gradient: linear-gradient(90deg, #c7d2fe, #e9d5ff, #fbcfe8). Use these as CSS variables defined at the top of about.css under the About page scope.

3. Hero (same text as now)
   - Headline "Java practice, tested for real." on two lines: line 1 "Java practice," in white, line 2 "tested for real." with the accent gradient as text (background-clip: text).
   - Paragraph max-width 52ch, color #a1a1aa.
   - Buttons side by side, height 48px, radius 10px, Inter 600 16px, with a 20px inline SVG icon on the left:
     - Primary "Start practicing" (links to /practice): accent gradient background, dark text #0a0a0b, 1px border rgba(255,255,255,0.25), a small code icon.
     - Secondary "Meet the team" (scrolls to #team): background #111113, 1px border rgba(255,255,255,0.14), white text, a small people icon.
     - Hover: brightness 1.08 on the primary, border brightens on the secondary. 150ms. No movement or glow. Visible focus rings.
   - Between the paragraph and the buttons add one small mono row like "Runs on" followed by two small chips, "Java 17" and "Docker". Check the project code first and only include a chip if it is really true; hide the row otherwise.
   - Do not add a badge, counters, or any new claim.

4. Workspace panel (right column): keep all its data and logic. Restyle only: background #101012, hairline border, mono font for the rows, the Easy/Medium/Hard chips with muted tinted backgrounds, and its buttons using the same two button styles as the hero but 40px high. Do not change which buttons appear (a separate task handles that).

5. Team section: heading "Meet the team" in the new h2 style, the mono label "// TEAM" above it. For the cards change ONLY the font-family (Inter) and colors to match this palette. Do not change their layout, content or links.

6. Responsive and quality
   - 1440, 1024 and 390 wide: no overlap, no horizontal scroll, the hero buttons fully visible with at least 48px below them. The headline wraps cleanly (two lines at 1440, up to four on a phone).
   - Contrast of every text at least WCAG AA. Respect prefers-reduced-motion.
   - Use the gradient text only on the h1 line 2.

VERIFY (describe what you saw): screenshots of the hero at 1440 and 390; the fonts in dev tools show Inter and JetBrains Mono only (no display font) in the main content; the header and footer look exactly as before; the character animation is still faintly visible in the hero; git diff --stat lists only about.html, about.css and about.js. Then stop."""Vercel Serverless Function entry point for the Code-Karo.dev API."""
import json
import os
import re
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, unquote, urlparse

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

        if path.startswith("/api/problems/"):
            problem_id = path[len("/api/problems/"):]
            problem = PROBLEMS.get(problem_id)
            if problem is None:
                self.send_json(404, {"error": f"Problem '{problem_id}' not found."})
                return
            self.send_json(200, problem)
            return

        # Fallback static file serving if a static request reaches the serverless function
        clean = path.strip("/")
        if clean.startswith("web/"):
            clean = clean[4:]
        if clean.startswith("public/"):
            clean = clean[7:]
        if clean in ("", "index.html", "about.html", "about", "about.css", "about.js", "team.js", "team.json", "app.css", "app.js", "config.js"):
            file_name = "index.html" if clean == "" else "about.html" if clean == "about" else clean
            content_types = {
                "index.html": "text/html; charset=utf-8",
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
