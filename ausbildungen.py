import pprint
import codecs
import re
import parsesplimo

from collections import namedtuple
Ausbildung = namedtuple('Ausbildung', 'name Stärken Ressourcen Fertigkeiten Meisterschaften Varianten')



with codecs.open('Ausbildung.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    Ausbildungen = {}
    for x in lines:
        for y in x:
            Werteblock = y.rsplit(sep = 'Werte eine',maxsplit =1)[1]
            Ausbildung_parse = [y.split(sep = '„',maxsplit =1)[0],]+ re.split(" [a-zA-ZäöüßÄÖÜß]+:",Werteblock,maxsplit =5)[1:5]+[Werteblock.split(sep = ":",maxsplit =5)[5],]
            Ausbildungen[Ausbildung_parse[0]] = Ausbildung(*Ausbildung_parse)




for Ausbildung_iterate in Ausbildungen.keys():
    Fertigkeitenliste = {}
    Ressourcenliste = {}
    Fertigkeit =  Ausbildungen[Ausbildung_iterate].Fertigkeiten.split(',')
    Ressource = Ausbildungen[Ausbildung_iterate].Ressourcen.split(',')
    for element in Fertigkeit:            
            x = element.rsplit(' ',1)
            Fertigkeitenliste[x[0].strip()] = x[1]
    for element in Ressource:            
            x = element.rsplit(' ',1)
            Ressourcenliste[x[0].strip()] = x[1]
    Ausbildungen[Ausbildung_iterate] = Ausbildungen[Ausbildung_iterate]._replace(Fertigkeiten = Fertigkeitenliste)
    Ausbildungen[Ausbildung_iterate] = Ausbildungen[Ausbildung_iterate]._replace(Ressourcen = Ressourcenliste)
        
#attribute += [splitstrip(y,';') for y in x]

print(Ausbildungen)