#!/usr/bin/env python3
import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8080
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} - {args[1]}\n")

# Try binding port, if busy try next port
for p in range(PORT, PORT + 20):
    try:
        server = socketserver.TCPServer(("", p), QuietHandler)
        PORT = p
        break
    except OSError:
        continue

url = f"http://localhost:{PORT}"
print("=" * 65)
print("  🏥 JOY OF CARE — PORTAL REVIEW ARTIKEL LOKAL (200 ARTIKEL)")
print("=" * 65)
print(f"  Server berjalan di : {url}")
print(f"  Direktori          : {DIR}")
print("  Tekan Ctrl+C untuk menghentikan server kapan saja.")
print("=" * 65)

try:
    webbrowser.open(url)
except Exception:
    pass

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer dihentikan.")
    server.server_close()
