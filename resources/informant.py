import json
import falcon
from case_insensitive_dict.case_insensitive_dict import CaseInsensitiveDict
from helpers.bot import send_message


class Informant:
    def on_post(self, request, response):
        raw_json = request.stream.read()
        data = CaseInsensitiveDict(json.loads(raw_json))
        status = send_message(data["message"])
        response.body = json.dumps({"sucess": bool(status)})
        response.status = falcon.HTTP_201
