from .middleware import Middleware
from .request import Request
from .response import Response

class Page(Middleware):
    def __init__(self, name, urlpatterns, get_method=None, post_method=None):
        super().__init__(urlpatterns)
        self.GET= get_method
        self.POST = post_method
        self.name = name
    
    def POST(self, post_method):
        self.POST = post_method

    def GET(self, get_method):
        self.GET = get_method
    
    def execute(self, request, response, next):
        if request.method == "POST":
            self.POST(request, response, next)
        if request.method == "GET":
            self.GET(request, response, next)

