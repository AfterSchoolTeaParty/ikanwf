from urllib import parse

class Chain:
    def __init__(self, status:bool):
        self.ischain = status

    def __call__(self):
        if self.ischain:
            self.ischain = False
        else:
            self.ischain = True

class QueryString:
    @staticmethod
    def parse(str_query):
        return dict(parse.parse_qs(str_query))

class URLPattern:
    def __init__(self, str_pattern):
        self.str_pattern = str_pattern
        self.list_pattern = str_pattern.split("/")[1:]

    def match(self, str_url:str):
        list_url = str_url.split("/")[1:]
        if str_url == self.str_pattern:
            return {"status" : True}
        if len(list_url) != len(self.list_pattern):
            return {"status" : False}

        params = {}
        for i in range(len(list_url)):
            if self.list_pattern[i].startswith(":"):
                params[self.list_pattern[i].replace(":", "", 1)] = list_url[i]
            else:
                if self.list_pattern[i] != list_url[i]:
                    return {"status" : False}
        
        return {"status" : True, "params" : params}
