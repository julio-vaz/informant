import falcon
from resources.informant import Informant


app = falcon.API()
app.add_route("/informant", Informant())
