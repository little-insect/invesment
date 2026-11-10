#!/usr/bin/env python3
"""Serve only the public app files; Codespaces provides the private login gate."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import os

ROOT = Path(__file__).resolve().parents[1] / 'public'
PORT = int(os.environ.get('CHANGPO_PORT', '4173'))

class Handler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, '.mjs': 'text/javascript; charset=utf-8'}

    def do_GET(self):
        if urlsplit(self.path).path == '/healthz':
            payload = json.dumps({'app': 'changpo-private-preview', 'ok': True}).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        segments = unquote(urlsplit(self.path).path).split('/')
        if any(part.startswith('.') or part == '..' for part in segments if part):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        segments = unquote(urlsplit(self.path).path).split('/')
        if any(part.startswith('.') or part == '..' for part in segments if part):
            self.send_error(404)
            return
        super().do_HEAD()

    def list_directory(self, path):
        self.send_error(404)
        return None

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Referrer-Policy', 'same-origin')
        super().end_headers()

    def log_message(self, format, *args):
        # Quiet serving avoids HTTP logs keeping an idle Codespace awake.
        pass

if __name__ == '__main__':
    server = ThreadingHTTPServer(('0.0.0.0', PORT), partial(Handler, directory=str(ROOT)))
    server.serve_forever()
