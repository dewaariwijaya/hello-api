# app.py - minimal deployable app (Python standard library only)
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = int(os.environ.get("PORT", "8000"))  # host sets this; don't hardcode

class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/health":
            self._send(200, {"status": "ok"})
        else:
            self._send(200, {"message": "Hello from Dewa's redeployed app!"})

    def log_message(self, *args):  # keep logs clean
        print("request:", self.path)

if __name__ == "__main__":
    print(f"Listening on port {PORT} - try /health")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
