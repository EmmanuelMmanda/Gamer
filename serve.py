import http.server
import socketserver


PORT = 8000
FILE = 'index.html'

class customHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = FILE
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
    
with socketserver.TCPServer(("",PORT), customHandler) as httpd:
    print ('Server started at 127.0.0.0:8000')
    httpd.serve_forever()