import re
import bottle
import model


@bottle.get("/")
def index():
    return bottle.template("Ustvarjalec-gesel\index.tpl")

@bottle.post("/novo-geslo")
def novo_geslo():    
    bottle.redirect("/geslo")   

@bottle.get("/geslo")
def novo():
    geslo = (model.geslo())
    return geslo
@bottle.route("/geslo/")
def neee():
    geslo = (model.geslo())
    return geslo
bottle.run(reloader=True,debug=True)