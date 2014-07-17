import pprint
import codecs
import re
import json
from parsesplimo import *

from collections import namedtuple
Ausbildung = namedtuple('Ausbildung', 'name Stärke Ressourcen Fertigkeiten Meisterschaften Varianten')
AusbildungFinal = namedtuple('Ausbildung', 'name description stats')
stats = namedtuple('stats', 'strengths skills ressources masteries')



with codecs.open('Ausbildung.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    Ausbildungen = {}
    for x in lines:
        for y in x:
            Werteblock = y.rsplit(sep = 'Werte eine',maxsplit =1)[1]
            Ausbildung_parse = [y.split(sep = '„',maxsplit =1)[0],]+ re.split(" [a-zA-ZäöüßÄÖÜß]+:",Werteblock,maxsplit =5)[1:5]+[Werteblock.split(sep = ":",maxsplit =5)[5],]
            Ausbildungen[Ausbildung_parse[0]] = Ausbildung(*Ausbildung_parse)



AusbildungenFinal = {}
AusbildungenStats = {}

        

for Ausbildung_iterate in Ausbildungen.keys():
    Fertigkeitenliste = []
    Meisterschaftenliste = []
    Ressourcenliste =  []
    #print(Ausbildungen[Ausbildung_iterate])
    for element in splitstrip(Ausbildungen[Ausbildung_iterate].Fertigkeiten,','):
        Fertigkeitenliste.append(inOptionenAufteilen(element))
        
    for element in splitstrip(Ausbildungen[Ausbildung_iterate].Ressourcen,','):
        if element.startswith('2 Punkte'):
            element = element.replace('2 Punkte frei wählbar aus ','')
            element = element.replace('2 Punkte frei verteilt auf ','')
            element = element.replace('und','oder')
            element = element + ' 2'
        Ressourcenliste.append(inOptionenAufteilen(element))
    Meisterschaftenliste.append(inOptionenAufteilen(Ausbildungen[Ausbildung_iterate].Meisterschaften+' 1'))
    for Meisterschaft in Meisterschaftenliste:
        pauschalMeisterschaft = Meisterschaft['options'][0].split(' (', maxsplit = 1)[0]
        for option in Meisterschaft['options']:
            option = option.replace('eine beliebige Schwelle 1-Meisterschaften in Heilkunde oder Heilungsmagie','Heilkunde: Felddiagnose oder Heilunde: Heilungsgeschick oder Heilkunde: Lebensretter oder Heilkunde: Schwerpunkt Gifte oder Heilkunde: Schwerpunkt Wunden oder Heilkunde: Schwerpunkt Zustände oder Heilkunde: Schwerpunkt Krankheiten oder Heilkunde: Schwerpunkt Heilkräuter bestimmen oder Heilungsmagie: Schwerpunkt Nach Zauber-Typus oder Heilungsmagie: Fokuskontrolle oder Heilungsmagie: Hand des Zauberers oder Heilungsmagie: Sparsamer Zauberer oder Heilungsmagie: Zauberfinger oder Heilungsmagie: Zauber verzögern oder Heilungsmagie: Entgiftung oder Heilungsmagie: Kosmetische THaumaturgie')
            if len(option.split('(', maxsplit = 1)) > 1:
                #print(option.split(' (', maxsplit = 1)[0]+': '+ option.split('(', maxsplit = 1)[1][:-1])
                Meisterschaft['options'] = [option.split(' (', maxsplit = 1)[0]+': '+ option.split('(', maxsplit = 1)[1][:-1]]
            else:
                #print(pauschalMeisterschaft+': '+ option.split('(', maxsplit = 1)[0][:-1])
                Meisterschaft['options'] = [pauschalMeisterschaft+': '+ option.split('(', maxsplit = 1)[0][:-1]]
  
    Ausbildungen[Ausbildung_iterate] = Ausbildungen[Ausbildung_iterate]._replace(Fertigkeiten = Fertigkeitenliste)
    Ausbildungen[Ausbildung_iterate] = Ausbildungen[Ausbildung_iterate]._replace(Meisterschaften = Meisterschaftenliste)
    Ausbildungen[Ausbildung_iterate] = Ausbildungen[Ausbildung_iterate]._replace(Stärke = inOptionenAufteilen(Ausbildungen[Ausbildung_iterate].Stärke+' 1'))
    stats([Ausbildungen[Ausbildung_iterate].Stärke],Fertigkeitenliste,Ressourcenliste,Meisterschaftenliste)
    AusbildungenStats[Ausbildungen[Ausbildung_iterate].name] = stats([Ausbildungen[Ausbildung_iterate].Stärke],Fertigkeitenliste,Ressourcenliste,Meisterschaftenliste)
    n = AusbildungenStats[Ausbildungen[Ausbildung_iterate].name]
    AusbildungenFinal[Ausbildungen[Ausbildung_iterate].name] = AusbildungFinal(Ausbildungen[Ausbildung_iterate].name, Ausbildungen[Ausbildung_iterate].name, dict(zip(n._fields, list(n))))

        
#attribute += [splitstrip(y,';') for y in x]

v = ''
for x in AusbildungenFinal:
    n = AusbildungenFinal[x]
    z = n.stats
    #print(json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+',')
    
    v +=json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+','

    

workfile = r"C:\Users\csiebenkaes\Google Drive\Splittermond\splittermond-chargen\Ausbildungen.json"
f = open(workfile, 'w')
f.write('['+v[:-1]+']')