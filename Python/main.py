import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class InfoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        response = {
            "project": "Minimal Python Docker App",
            "description": "A tiny web server to demonstrate minimal Docker setup",
            "author": "Rishabh Garg",
            "version": "1.0.0",
            "status": "Running"
        }
        self.wfile.write(json.dumps(response, indent=4).encode("utf-8"))

if __name__ == "__main__":
    PORT = int(os.environ.get("APP_PORT", 8081))  # Default to 8081
    server = HTTPServer(("", PORT), InfoHandler)
    print(f"Server started at http://0.0.0.0:{PORT}")
    server.serve_forever()
