import json
import falcon


class Informant:
    def on_post(self, request, response):
        response.body = json.dumps({})
        response.code = falcon.HTTP_201
