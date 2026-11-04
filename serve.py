import http.server
import socket
import socketserver
import webbrowser
import os
import sys

# Configure UTF-8 for console output on Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def find_free_port(start=8000, max_attempts=50):
    for port in range(start, start + max_attempts):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return start

def run():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_free_port(8000)
    
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Ensure correct MIME types for ES modules and WebFonts
    Handler.extensions_map.update({
        '.js': 'application/javascript',
        '.mjs': 'application/javascript',
        '.css': 'text/css',
        '.woff2': 'font/woff2',
        '.woff': 'font/woff',
        '.svg': 'image/svg+xml',
        '.webmanifest': 'application/manifest+json',
        '.json': 'application/json',
    })
    
    url = f"http://localhost:{port}"
    print(f"========================================================")
    print(f"  کاوشگر پروتکل‌های اینترنت (نسخه فارسی) در حال اجراست")
    print(f"  Protocol Explorer running at: {url}")
    print(f"========================================================")
    print(f"Serving files from: {os.getcwd()}")
    sys.stdout.flush()

    # Open browser
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Could not open browser automatically: {e}")

    with socketserver.TCPServer(("0.0.0.0", port), Handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    run()
