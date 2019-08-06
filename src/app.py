from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os
import socket
import ssl


class HTTPHostnameHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'type: %s\nhostname: %s' % (os.getenv('APP_SERVICE_TYPE', 'A (default)').encode(),
                                                      socket.gethostname().encode()))


httpd = HTTPServer(('0.0.0.0', 4443), HTTPHostnameHandler)


httpd.socket = ssl.wrap_socket(httpd.socket, 
                               keyfile="/etc/app/key-u.pem",
                               certfile="/etc/app/cert.pem",
                               server_side=True)


httpd.serve_forever()