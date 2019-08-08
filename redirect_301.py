import http.server
import socketserver

class FakeRedirect(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       print (self.path)
       self.send_response(301)
       new_path = '%s%s'%('http://127.0.0.1:9091', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

socketserver.TCPServer(("", 9090), FakeRedirect).serve_forever()
