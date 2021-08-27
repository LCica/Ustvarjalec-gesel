import bottle
import model
import pyperclip
gesla = model.Geslo(model.DATOTEKA_S_S)

@bottle.get("/")
def index():   
    return bottle.template("index.tpl")

@bottle.get("/geslo/")
def novo_geslo():       
    bottle.redirect("/geslo/")   

@bottle.post("/geslo/")
def dodaj_st():        
    prvi = bottle.request.forms.get('prva') or 0
    drugi = bottle.request.forms.get('druga') or 0
    tretji = bottle.request.forms.get('tretja') or 0
    cetrti = bottle.request.forms.get('cetrta') or 0
    dolzine = bottle.request.forms.get('dolzine') or 0
    c = bottle.request.forms.get('ctrlc') or 0               
    if (prvi== 0 and drugi== 0 and tretji== 0 and cetrti == 0) or int(dolzine)==0:
            return bottle.template("napaka.tpl")                        
    else:                              
        geslo= gesla.geslo(prvi,drugi,tretji,cetrti,int(dolzine))
        if int(c)==1:
            gesla.novo_geslo(geslo)    
            pyperclip.copy(geslo)
    return bottle.template("proba.tpl", geslo=geslo)
         
    

bottle.run(reloader=True,debug=True)