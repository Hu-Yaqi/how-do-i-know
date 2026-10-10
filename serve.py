"""Serves this folder on http://localhost so the page can use the copy of the face
tracker saved in vendor/ (works without internet).
Run:  python3 serve.py      Stop:  Ctrl+C"""
import http.server
import os
import sys
import threading
import webbrowser

os.chdir(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      ".mjs": "text/javascript", ".js": "text/javascript",
                      ".wasm": "application/wasm", ".task": "application/octet-stream"}

    def log_message(self, *args):
        pass


url = f"http://localhost:{PORT}/"
print(f"How Do I Know? is on {url}")
print("Open it in Chrome, Edge or Firefox. Press Ctrl+C here to stop.")
threading.Timer(1.0, lambda: webbrowser.open(url)).start()
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
