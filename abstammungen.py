import pprint
import codecs
import json
from parsesplimo import *

from collections import namedtuple
Abstammung = namedtuple('Abstammung', 'name description resources skills')


with codecs.open('Abstammung.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    Abstammungen = {}
    for x in lines:
        for y in x:
            Abstammung_parsed = [y.split(maxsplit =1)[0]]+[splitstrip(y.split(maxsplit =1)[1],'-;-')[0]]+splitstrip(y.split(maxsplit =1)[1],'-;-')[1:3]
        Abstammungen[Abstammung_parsed[0]] = Abstammung(*Abstammung_parsed)


for Abstammung in Abstammungen.keys():
    Fertigkeitenliste = []
    Ressourcenliste = []
    Fertigkeit =  Abstammungen[Abstammung].skills.split(',')
    Ressource = Abstammungen[Abstammung].resources.split(',')
    
    for element in Fertigkeit:
        Fertigkeitenliste.append(inOptionenAufteilen(element))
    for element in Ressource:
        Ressourcenliste.append(inOptionenAufteilen(element))
    Abstammungen[Abstammung] = Abstammungen[Abstammung]._replace(skills = Fertigkeitenliste)
    Abstammungen[Abstammung] = Abstammungen[Abstammung]._replace(resources = Ressourcenliste)
        
