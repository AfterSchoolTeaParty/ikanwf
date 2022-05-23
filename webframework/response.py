import json
class Response:
    def __init__(self, respond):
        self.respond = respond
        self.data = ""
        self.status_code = "200 OK"
        self.mimetype = "text/plain"

    def json(self, data:dict, status_code = "200 OK"):
        self.mimetype = "application/json"
        self.data = json.dumps(data)

    def html(self, html, status_code = "200 OK"):
        self.mimetype = "text/html"
        self.data = html

    def text(self, text, status_code = "200 OK"):
        self.mimetype = "text/plain"
        self.data = text
    
    def get_data(self):
        self.respond(self.status_code, [("Content-Type", self.mimetype)])
        return self.data.encode("utf-8")