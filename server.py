#!/usr/bin/env python3
"""
Lightweight HTTP server with Basic Authentication for Fourball Dashboard
Serves static files and the dashboard HTML with password protection
Includes unauthenticated /health endpoint for Railway healthchecks
"""

import os
import base64
from http.server import HTTPServer, SimpleHTTPRequestHandler
from functools import partial


class AuthHTTPRequestHandler(SimpleHTTPRequestHandler):
    """HTTP Request Handler with Basic Authentication and Security Headers"""

    def __init__(self, *args, username=None, password=None, **kwargs):
        self.auth_username = username
        self.auth_password = password
        super().__init__(*args, **kwargs)

    def end_headers(self):
        """Add security headers to all responses"""
        # Security headers
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')

        # Cache headers for static assets
        if self.path.endswith(('.png', '.jpg', '.jpeg', '.css', '.js', '.json')):
            self.send_header('Cache-Control', 'public, max-age=86400')  # 24 hours
        else:
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')

        super().end_headers()

    def list_directory(self, path):
        """Disable directory listings for security"""
        self.send_error(403, "Directory listing disabled")
        return None

    def do_authhead(self):
        """Send authentication request header"""
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Fourball Dashboard"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def check_auth(self):
        """Check if the provided credentials are valid"""
        auth_header = self.headers.get('Authorization')

        if auth_header is None:
            return False

        # Parse the Authorization header
        try:
            auth_type, auth_string = auth_header.split(' ', 1)
            if auth_type.lower() != 'basic':
                return False
        except ValueError:
            return False

        # Decode base64 credentials
        try:
            decoded = base64.b64decode(auth_string).decode('utf-8')
            username, password = decoded.split(':', 1)
        except Exception:
            return False

        # Verify credentials
        return username == self.auth_username and password == self.auth_password

    def do_GET(self):
        """Handle GET requests with authentication (except /health and /login.html)"""
        # Health check endpoint - no authentication required
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "healthy", "service": "fourball-dashboard"}')
            return

        # Login page - no authentication required
        if self.path == '/login.html' or self.path == '/':
            if self.path == '/':
                # Redirect root to login page
                self.path = '/login.html'
            return super().do_GET()

        # All other routes require authentication
        if not self.check_auth():
            # Redirect to login page instead of showing basic auth
            self.send_response(302)
            self.send_header('Location', '/login.html')
            self.end_headers()
            return

        # Serve the file using parent class
        return super().do_GET()

    def do_HEAD(self):
        """Handle HEAD requests with authentication (except /health)"""
        # Health check endpoint - no authentication required
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            return

        # All other routes require authentication
        if not self.check_auth():
            self.do_authhead()
            return
        return super().do_HEAD()

    def log_message(self, format, *args):
        """Custom log format for better Railway logging"""
        print(f"{self.address_string()} - [{self.log_date_time_string()}] {format % args}")


def run_server():
    """Start the HTTP server with authentication"""
    # Get configuration from environment
    port = int(os.environ.get('PORT', 8000))
    username = os.environ.get('DASHBOARD_USERNAME', 'admin')
    password = os.environ.get('DASHBOARD_PASSWORD', 'changeme')

    # Validate credentials are set
    if password == 'changeme':
        print("⚠️  WARNING: Using default password. Set DASHBOARD_PASSWORD environment variable!")
        print("   This is insecure for production deployments!")

    if not username or not password:
        print("❌ ERROR: DASHBOARD_USERNAME and DASHBOARD_PASSWORD must be set!")
        print("   Set them as environment variables before starting.")
        return

    # Create handler with authentication
    handler = partial(
        AuthHTTPRequestHandler,
        username=username,
        password=password
    )

    # Start server
    server = HTTPServer(('0.0.0.0', port), handler)

    print(f"🚀 Fourball Dashboard Server")
    print(f"📍 Listening on http://0.0.0.0:{port}")
    print(f"🔐 Authentication: {username} / {'*' * len(password)}")
    print(f"✅ Health endpoint: http://localhost:{port}/health (unauthenticated)")
    print(f"🎯 Dashboard: http://localhost:{port}/fourball_dashboard.html (requires login)")
    print(f"🔒 Security: Directory listings disabled, security headers enabled")
    print("\nPress Ctrl+C to stop the server")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped")
        server.shutdown()


if __name__ == '__main__':
    run_server()
