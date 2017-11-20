from web_api import httpserver
from cherrypy.wsgiserver import CherryPyWSGIServer

server = CherryPyWSGIServer(
    ('0.0.0.0', 8008),
    httpserver,
    server_name='My_App',
    numthreads=10)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()

