import http.server
import socketserver
import pymysql

import sys

PORT = int(sys.argv[1])

connection_params = {
    "user": "root",
    "password": "123456",
    "host": "database",
    "port": 3306,
}

class multiHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith("/cookie"):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()

            cnx = pymysql.Connect(**connection_params)

            cur = cnx.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS isp;")
            cnx.select_db("isp")

            cur.execute("CREATE TABLE IF NOT EXISTS cookie (cookie_id INTEGER PRIMARY KEY AUTO_INCREMENT);")

            cur.execute("INSERT INTO cookie (cookie_id) VALUES (null);")
            cur.connection.commit()

            cur.execute("select COUNT(*) from cookie;")
            output = cur.fetchone()

            with open("index.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
                self.wfile.write(f'<p style="text-align: center;">{output[0]} COOOKIEZ!</p>'.encode("utf-8"))

        elif self.path.endswith(""):
            self.send_response(200)
            self.send_header("content-type", "text/html")
            self.end_headers()

            with open("index.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        


with socketserver.TCPServer(("", PORT), multiHandler) as httpd:
    print("listening to socket", PORT)
    httpd.serve_forever()