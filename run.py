import falcon
from resources.informant import Informant

app = falcon.API()
app.add_route("/", Informant())
app.run()
