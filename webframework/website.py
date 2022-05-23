import os
from wsgiref import simple_server

from .request import Request
from .response import Response
from .middleware import Middleware
from .page import Page

from .utils import Chain


class Website:
    def __init__(self, file:__file__):
        self.hostname = "localhost"
        self.port = 8080
        self.ROOT_DIRECTORY = os.path.dirname(file)
        self.middlewares = []

    def application(self, environ, respond):
        request = Request(environ)
        response = Response(respond)
        chain = Chain(False)

        for middleware in self.middlewares:
            if middleware(request, response, chain):
                if chain.ischain:
                    chain()
                    continue
                else:
                    break
        return [response.get_data()]

    def __call__(self, hostname, port):
        if hostname:
            self.hostname = hostname
        if port:
            self.port = port
        httpd = simple_server.make_server(self.hostname, self.port, self.application)
        print(f"Serving on port {self.port}, CTRL-C to close the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Shutting Down")
            httpd.server_close()
        
    def register(self, middleware:Page|Middleware):
        self.middlewares.append(middleware)
    
    def register_bundle(self, middlewares:list):
        self.middlewares += middlewares
