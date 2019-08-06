from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import os
import socket
import ssl


class HTTPHostnameHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """return APP_SERVICE_TYPE env variable and hostname.
        
        APP_SERVICE_TYPE allows you to differentiate between "classes"
        of services, which may be useful. if not set, it defaults
        to... guess what... "default".
        """
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'type: %s\nhostname: %s' % (os.getenv('APP_SERVICE_TYPE', 'default').encode(),
                                                      socket.gethostname().encode()))


httpd = HTTPServer(('0.0.0.0', 4443), HTTPHostnameHandler)


# NOTE: encrypted certs will prompt for a passphrase every time
# the service is started. to avoid this, we're using unencrypted
# certs. do not use this setup in production.
httpd.socket = ssl.wrap_socket(httpd.socket,
                               keyfile="/etc/app/key-u.pem",
                               certfile="/etc/app/cert.pem",
                               server_side=True)


httpd.serve_forever()