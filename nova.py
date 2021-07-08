import bottle


@bottle.get("/")
def index():
    return bottle.template("index.tpl")
    




bottle.run(reloader=True,debug=True)