from .request import Request
from .response import Response
from .utils import URLPattern

class Middleware:
    def __init__(self, urlpatterns = "", **kwargs):
        self.urlpatterns = urlpatterns
        if urlpatterns:
            if type(urlpatterns) == str:
                self.urlpatterns = [urlpatterns]
            elif type(urlpatterns) == list:
                pass
            else:
                raise TypeError(f"urlpatterns should be either {str} or {list}")
        if "execute" in kwargs and callable(kwargs["execute"]):
            self.execute = kwargs["execute"]

    def execute(self, execute_method):
        self.execute = execute_method
    
    def match_urlpattern(self, url_str):
        if "" in self.urlpatterns:
            return True
        for urlpattern in self.urlpatterns:
            if URLPattern(urlpattern).match(url_str)["status"]:
                return True
        return False

    def __call__(self, request, response, next):
        if "" in self.urlpatterns:
            self.execute(request, response, next)
            return True

        for urlpattern in self.urlpatterns:
            if URLPattern(urlpattern).match(request.path)["status"]:
                self.execute(request, response, next)
                return True
        return False