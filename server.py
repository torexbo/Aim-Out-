# server.py
from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')  # Allow CORS
        super().end_headers()

if __name__ == "__main__":
    os.chdir('files')  # Serve files from the 'files' directory
    server_address = ('', 8000)  # Listen on all interfaces, port 8000
    httpd = HTTPServer(server_address, CustomHandler)
    print("Serving files on http://localhost:8000")
    httpd.serve_forever()
