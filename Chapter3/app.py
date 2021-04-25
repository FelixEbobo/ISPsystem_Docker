import http.server
import socketserver

import sys

PORT = int(sys.argv[1])

class multiHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/cookie"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()

            with open("index.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
                self.wfile.write("COOOKIEZ!".encode("utf-8"))

        elif self.path.endswith(""):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()

            with open("index.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        


with socketserver.TCPServer(("", PORT), multiHandler) as httpd:
    print("listening to socket", PORT)
    httpd.serve_forever()