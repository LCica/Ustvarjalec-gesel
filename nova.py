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
        cifre = (bottle.request.forms.getlist('moje'))                
        
        for element in cifre:
            st=['']
            mc=['']
            vc=['']
            si=['']
            if element == '1':
               st += ['0','1','2','3','4','5','6','7','8','9']
            elif element == '2':
                mc += ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
            elif element == '3':
                vc += ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            elif element == '4':
                si += ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
            VSE_SKP = st + mc + vc + si
            rand_cifra = random.choice(st)
            rand_male = random.choice(mc)
            rand_velke = random.choice(vc)
            rand_simbol = random.choice(si)
            rand_skp = rand_cifra + rand_male + rand_velke + rand_simbol
            for x in range(10):
                rand_skp += random.choice(VSE_SKP)
                rand_skp_list = array.array('u',rand_skp)    
                random.shuffle(rand_skp_list)
            geslo = ""
            for x in rand_skp_list:
                geslo += x          
    return bottle.template("geslo.tpl", geslo=geslo)

app.run(reloader=True,debug=True)