import http.server
import socketserver

class Redirect(http.server.SimpleHTTPRequestHandler):
   def do_GET(self):
       print (self.path)
       self.send_response(301)
       new_path = '%s%s'%('http://localhost:9091', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

socketserver.TCPServer(("", 9090), Redirect).serve_forever()
