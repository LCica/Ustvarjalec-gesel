from bottle import Bottle
import bottle
import array
import random
app = Bottle()

@app.get("/")
def index():   
    return bottle.template("index.tpl")

@app.get("/geslo/")
def novo_geslo():       
    app.redirect("/geslo/")   

@app.post("/geslo/")
def dodaj_st():
    if bottle.request.method == 'POST':        
        prvi = bottle.request.forms.get('prva') or 0
        drugi = bottle.request.forms.get('druga') or 0
        tretji = bottle.request.forms.get('tretja') or 0
        cetrti = bottle.request.forms.get('cetrta') or 0
        dolzine = bottle.request.forms.get('dolzine') or 0
        dolzina = int(dolzine)               
        st=['0','1','2','3','4','5','6','7','8','9']
        mc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
        vc=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        si=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']   
        VSE_SKP = st + mc + vc + si
        if (prvi== 0 and drugi== 0 and tretji== 0 and cetrti == 0) or dolzina==0:
                return bottle.template("napaka.tpl")                        
        else:            
            if prvi == 0:
                for ele in sorted(st, reverse = True):
                    del VSE_SKP[int(ele)] 
            if drugi == 0:
                for ele in sorted(mc, reverse = True):
                    del VSE_SKP[int(ele)]  
            if tretji == 0:
                for ele in sorted(vc, reverse = True):
                    del VSE_SKP[int(ele)] 
            if cetrti == 0:
                for ele in sorted(si, reverse = True):
                    del VSE_SKP[int(ele)]                    
            rand_skp = ""
            for x in range(dolzina):
                rand_skp += random.choice(VSE_SKP)
                rand_skp_list = array.array('u',rand_skp)    
                random.shuffle(rand_skp_list)
            neki = ""
            for x in rand_skp_list:
                neki += x       
            return bottle.template("geslo.tpl", geslo=neki)

app.run(reloader=True,debug=True)