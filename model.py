import random
import array
import json

datoteka_s_s = 'stanje.json'

class Geslo:
    def __init__(self, dolzina,st=None,mc=None,vc = None,si = None):
        self.dolzina = dolzina
        self.st= st or list()
        self.mc= mc or list()
        self.vc= vc or list()
        self.si = si or list() 
    def dodaj_st(self, odg):
        if odg == True:
            self.st = ['0','1','2','3','4','5','6','7','8','9']
    def dodaj_mc(self, odg):
        if odg == True:
            self.mc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    def dodaj_vc(self, odg):
        if odg == True:
            self.vc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    def dodaj_si(self, odg):
        if odg == True:
            self.si = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']
    def geslo(self):
        VSE_SKP = self.dodaj_st() + self.dodaj_mc() + self.dodaj_vc() + self.dodaj_si()
        rand_cifra = random.choice(self.dodaj_st())
        rand_male = random.choice(self.dodaj_mc())
        rand_velke = random.choice(self.dodaj_vc())
        rand_simbol = random.choice(self.dodaj_si())
        rand_skp = rand_cifra + rand_male + rand_velke + rand_simbol
        for x in range(self.dolzina-4):
            rand_skp += random.choice(VSE_SKP)
            rand_skp_list = array.array('u',rand_skp)    
            random.shuffle(rand_skp_list)
        geslo = ""
        for x in rand_skp_list:
            geslo += x
        return geslo 
class Generator:
    def __init__(self,datoteka_s_s):
        self.max_id = 0
        self.gesla = {}
        self.datoteka_s_s = datoteka_s_s
    def prost_id(self):
        self.max_id += 1
        return self.max_id
    def novo_geslo(self):
        pass
    def zapisi_geslo_v_datoteko(self):
        with open(self.datoteka_s_s,'w',encoding="utf-8") as f:
            gesla = {id_gesla: (geslo.geslo,geslo.dolzina) for id_gesla,(geslo,dolzina) in self.gesla.items()}
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







