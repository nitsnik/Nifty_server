
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime, timezone

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/data":
            data = {
                "server": "NIFTY Server",
                "status": "running",
                "message": "Server API is working",
                "time_utc": datetime.now(timezone.utc).isoformat()
            }
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)
        else:
            body = b"NIFTY Server is running"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, format, *args):
        pass

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("NIFTY Server started on port 8000")
server.serve_forever()
