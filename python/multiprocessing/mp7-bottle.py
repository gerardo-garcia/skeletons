from wsgiref.simple_server import make_server, WSGIServer
from SocketServer import ThreadingMixIn
import bottle

"""
Simple multithreaded WSGI HTTP server.
"""
class ThreadingWSGIServer(ThreadingMixIn, WSGIServer):
    daemon_threads = True

class Server:
    def __init__(self, wsgi_app, listen='127.0.0.1', port=8080):
        self.wsgi_app = wsgi_app
        self.listen = listen
        self.port = port
        self.server = make_server(self.listen, self.port, self.wsgi_app,
                                  ThreadingWSGIServer)

    def serve_forever(self):
        self.server.serve_forever()

wsgiapp = bottle.default_app()
httpd = Server(wsgiapp)
httpd.serve_forever()

