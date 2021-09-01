import bottle
import model
import pyperclip
gesla = model.Geslo(model.DATOTEKA_S_S)

with open("skrivnost.txt") as f:
    SKRIVNOST = f.read()


@bottle.get("/")
def index():   
    return bottle.template("index.tpl")

@bottle.post("/geslo/")
def novo_geslo():
    st = bottle.request.forms.get('prva') or 0
    mc = bottle.request.forms.get('druga') or 0
    vc = bottle.request.forms.get('tretja') or 0
    si = bottle.request.forms.get('cetrta') or 0
    d = bottle.request.forms.get('dolzine') or 0
    c = bottle.request.forms.get('ctrlc') or 0    
    if (st== 0 and mc== 0 and vc== 0 and si == 0) or int(d)==0:
        bottle.redirect("/napaka/")                            
    else:
        geslo= gesla.geslo(st,mc,vc,si,d)
        id = gesla.novo_geslo(geslo)
        bottle.response.set_cookie('idgesla','idigre{}'.format(id),secret=SKRIVNOST, path='/')                                            
        if int(c)==1:
            pyperclip.copy(geslo)                   
        bottle.redirect("/geslo/")

@bottle.get("/geslo/")
def dodaj_st():
    id= int(bottle.request.get_cookie('idgesla', secret=SKRIVNOST).split('e')[1])        
    geslo = gesla.gesla[id]
    return bottle.template("geslo.tpl", geslo=geslo)

@bottle.get("/napaka/")
def napaka():
    return bottle.template("napaka.tpl")
         
    

bottle.run(reloader=True,debug=True)