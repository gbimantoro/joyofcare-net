#!/usr/bin/env python3
"""
Joy of Care Local Review Portal Server
Provides local HTTP serving for review portal with editor opening capabilities.
"""

import http.server
import socketserver
import os
import sys
import subprocess
import urllib.parse
import json

PORT = 8908
if len(sys.argv) > 1:
    try:
        PORT = int(sys.argv[1])
    except ValueError:
        pass

DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(DIR)
os.chdir(DIR)

class JoyOfCareHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Prevent aggressive browser caching during review/development
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        
        # API: Open File in Editor
        if parsed.path == '/api/open-editor':
            query = urllib.parse.parse_qs(parsed.query)
            file_param = query.get('file', [''])[0]
            if not file_param:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Missing file parameter'}).encode('utf-8'))
                return
            
            # Resolve path and ensure within project root
            target_path = os.path.abspath(file_param if os.path.isabs(file_param) else os.path.join(PROJECT_ROOT, file_param))
            if not target_path.startswith(PROJECT_ROOT) or not os.path.exists(target_path):
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'File not found or forbidden', 'path': target_path}).encode('utf-8'))
                return

            # Try opening in editor (code -> cursor -> xdg-open)
            opened = False
            error_msg = ""
            for cmd in [['code', target_path], ['cursor', target_path], ['xdg-open', target_path]]:
                try:
                    subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    opened = True
                    break
                except Exception as e:
                    error_msg = str(e)
                    continue

            self.send_response(200 if opened else 500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'success': opened,
                'path': target_path,
                'error': None if opened else error_msg
            }).encode('utf-8'))
            return

        # API: Server Status
        if parsed.path == '/api/status':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                'status': 'online',
                'portalDir': DIR,
                'projectRoot': PROJECT_ROOT
            }).encode('utf-8'))
            return

        return super().do_GET()

    def log_message(self, format, *args):
        # Compact log
        if args and isinstance(args[0], str) and not args[0].startswith("GET /articles-data.js"):
            sys.stderr.write(f"[{self.log_date_time_string()}] {args[0]} - {args[1] if len(args) > 1 else ''}\n")

import socket
import time

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except (AttributeError, OSError):
            pass
        super().server_bind()

# Bind target port (retry if recently in TIME_WAIT)
server = None
for attempt in range(15):
    try:
        server = ReusableTCPServer(("", PORT), JoyOfCareHandler)
        break
    except OSError:
        time.sleep(1)

if not server:
    # Fallback to next available port if port is permanently occupied
    for p in range(PORT, PORT + 20):
        try:
            server = ReusableTCPServer(("", p), JoyOfCareHandler)
            PORT = p
            break
        except OSError:
            continue

if not server:
    sys.stderr.write(f"Tidak ada port yang tersedia!\n")
    sys.exit(1)

url = f"http://localhost:{PORT}"
print("=" * 68)
print("  🏥 JOY OF CARE — PORTAL REVIEW ARTIKEL LOKAL (210 ARTIKEL)")
print("=" * 68)
print(f"  URL Portal Review  : {url}")
print(f"  Direktori Berkas   : {DIR}")
print("  Fitur Interaktif   : Buka di Editor, Dual View, Fullscreen, Filter")
print("  Tekan Ctrl+C untuk menghentikan server.")
print("=" * 68)

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer dihentikan.")
    server.server_close()
