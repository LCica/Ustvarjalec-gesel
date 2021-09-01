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
        for x in range(int(dolzina)):
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

















 



