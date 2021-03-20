#! /usr/bin/env python

from datetime import datetime as _dt
from http.server import BaseHTTPRequestHandler, HTTPServer
import platform
import json
import cgi


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        response = {'response_at': str(_dt.now()), 'response_from': platform.node()}
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))

        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return

        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        message['received_at'] = str(_dt.now())
        message['received_from'] = platform.node()

        self._set_headers()
        self.wfile.write(json.dumps(message).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=Server, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    try:
        print(f'info: start HTTP on port {port}...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('info: HTTP Server stoped')
    except Exception as e:
        print(f'error: {e}')


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
