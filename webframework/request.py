from .utils import QueryString

class Request:
    def __init__(self, environ):
        self.query_string = QueryString.parse(environ["QUERY_STRING"])
        self.path = environ["PATH_INFO"]
        self.http_host = environ["HTTP_HOST"]
        self.http_connection = environ["HTTP_CONNECTION"]
        self.server_protocol = environ["SERVER_PROTOCOL"]
        self.server_port = environ["SERVER_PORT"]
        self.server_hostname = environ["REMOTE_ADDR"]

        self.method = environ["REQUEST_METHOD"]

        if self.method == "POST":
            try:
                request_body_size = int(environ["CONTENT_LENGTH"])
                self.forms = QueryString.parse(environ["wsgi.input"].read(request_body_size).decode("utf-8"))
            except (TypeError, ValueError):
                self.forms = "0"