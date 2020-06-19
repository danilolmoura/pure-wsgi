from http.server import BaseHTTPRequestHandler, HTTPServer

class Index(BaseHTTPRequestHandler):
    def do_GET(self):
        """Hhndle HTTP GET requests"""
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<h3>Hello WSGI with Python 3<h3>'.encode('utf-8'))


app = HTTPServer(('0.0.0.0', 8000), Index)
app.serve_forever()