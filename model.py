import random
import array
import json

DATOTEKA_S_S = 'stanje.json'

class Geslo:
    def __init__(self,DATOTEKA_S_S):
        
        self.datoteka_s_s = DATOTEKA_S_S
        self.gesla = {}
        self.max_id = 0    
    def geslo(self,prvi=True,drugi=True,tretji=True,cetrti=True,dolzina=0):
        vse = []        
        if int(prvi) == 1:
            vse += ['0','1','2','3','4','5','6','7','8','9']
        if int(drugi) == 2:
            vse += ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y','z']
        if int(tretji) == 3:
            vse += ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y', 'Z']
        if int(cetrti) == 4:
            vse += ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
        rand_skp = ""
        for x in range(dolzina):
            rand_skp += random.choice(vse)
            rand_skp_list = array.array('u',rand_skp)    
            random.shuffle(rand_skp_list)
        geslo = ""
        for x in rand_skp_list:
            geslo += x
        return geslo
    def prost_id(self):
        self.max_id += 1
        return self.max_id
    def novo_geslo(self,geslo):
        id_gesla=self.prost_id()
        self.gesla[id_gesla]= (geslo)
        self.zapisi_geslo_v_datoteko()
        return id_gesla
    def zapisi_geslo_v_datoteko(self):
        with open(self.datoteka_s_s,'w',encoding="utf-8") as f:
            gesla = self.gesla
            json.dump(gesla,f)















#NAJ_DOL = int(input("Vnesi dolžino gesla:\n"))

#s = None
#while s not in ("Da","da","DA","dA","Ne","NE","ne","nE"):
#    s = input("Želite imeti številke? Vnesi Da ali Ne:")
#    if s == "Da" or s == "DA" or s == "da" or s == "dA":
#        STEVILKE = ['0','1','2','3','4','5','6','7','8','9']
#    elif s == "Ne" or s == "NE" or s == "ne" or s == "nE":
#        STEVILKE = ['']
#    else:
#        input("VNESITE DA ALI NE!")
#
#m = None
#while m not in ("Da","da","DA","dA","Ne","NE","ne","nE"):
#    m = input("Želite imeti male črke? Vnesi Da ali Ne:")
#    if m == "Da" or m == "DA" or m == "da" or m == "dA":
#        MALE_CRKE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
#    elif m == "Ne" or m == "NE" or m == "ne" or m == "nE":
#        MALE_CRKE = ['']
#    else:
#        input("VNESI DA ALI NE!")
#
#v = None
#while v not in ("Da","da","DA","dA","Ne","NE","ne","nE"):
#    v = input("Želite imeti velike črke? Vnesi Da ali Ne:")
#    if v == "Da" or v == "DA" or v == "da" or v == "dA":
#        VELKE_CRKE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#    elif v == "Ne" or v == "NE" or v == "ne" or v == "nE":
#        VELKE_CRKE = ['']
#    else:
#        input("VNESI DA ALI NE!")
#
#i = None
#while i not in ("Da","da","DA","dA","Ne","NE","ne","nE"):
#    i = input("Želite imeti simbole? Vnesi Da ali Ne:")
#    if i == "Da" or i == "DA" or i == "da" or i == "dA":
#        SIMBOLI = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
#    elif i == "Ne" or i == "NE" or i == "ne" or i == "nE":
#       SIMBOLI = ['']
#    else:
#        input("VNESI DA ALI NE!") 
#
#



#def odstrani_st(self):
    #    for znak in self.st:
    #        if znak in self.vse:
    #            self.vse.remove(znak)
    #def odstrani_mc(self):
    #    for znak in self.mc:
    #        if znak in self.vse:
    #            self.vse.remove(znak)
    #def odstrani_vc(self):
    #    for znak in self.vc:
    #        if znak in self.vse:
    #            self.vse.remove(znak)
    #def odstrani_si(self):
        #for znak in self.si:
        #    if znak in self.vse:
        #        self.vse.remove(znak)  



