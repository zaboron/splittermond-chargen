import pprint
import codecs
import json
from parsesplimo import *


from collections import namedtuple
Kultur = namedtuple('Kultur', 'name Rassen Abstammungen Muttersprache Kulturkunde Stärke Fertigkeiten Meisterschaften')
KulturFinal = namedtuple('Kultur', 'name description stats')
stats = namedtuple('stats', 'strengths skills masteries')



with codecs.open('kulturen.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    attribute = []
    for x in lines:
        attribute += [splitstrip(y,';') for y in x]
    
Kulturen = {}
KulturenFinal = {}
KulturenStats = {}

for row in attribute:
    for i, field in enumerate(row):
        if ',' in field:
            row[i] = splitstrip(field,',')
    Kulturen[Kultur(*row).name] = Kultur(*row)      
    


for Kultur in Kulturen.keys():
    Fertigkeitenliste = []
    Meisterschaftenliste = []
    for element in Kulturen[Kultur].Fertigkeiten:
        Fertigkeitenliste.append(inOptionenAufteilen(element))
    Meisterschaftenliste.append(inOptionenAufteilen(Kulturen[Kultur].Meisterschaften+' 1'))
    for Meisterschaft in Meisterschaftenliste:
        pauschalMeisterschaft = Meisterschaft['options'][0].split(' (', maxsplit = 1)[0]
        for option in Meisterschaft['options']:
            if len(option.split('(', maxsplit = 1)) > 1:
                #print(option.split(' (', maxsplit = 1)[0]+': '+ option.split('(', maxsplit = 1)[1][:-1])
                Meisterschaft['options'] = [option.split(' (', maxsplit = 1)[0]+': '+ option.split('(', maxsplit = 1)[1][:-1]]
            else:
                #print(pauschalMeisterschaft+': '+ option.split('(', maxsplit = 1)[0][:-1])
                Meisterschaft['options'] = [pauschalMeisterschaft+': '+ option.split('(', maxsplit = 1)[0][:-1]]
  
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Fertigkeiten = Fertigkeitenliste)
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Meisterschaften = Meisterschaftenliste)
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Stärke = inOptionenAufteilen(Kulturen[Kultur].Stärke+' 1'))
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Abstammungen = parseAbstammung(Kulturen[Kultur].Abstammungen))
    KulturenStats[Kulturen[Kultur].name] = stats([Kulturen[Kultur].Stärke],Fertigkeitenliste,Meisterschaftenliste)
    n = KulturenStats[Kulturen[Kultur].name]
    KulturenFinal[Kulturen[Kultur].name] = KulturFinal(Kulturen[Kultur].name, Kulturen[Kultur].name, dict(zip(n._fields, list(n))))
        
def dictify(some_named_tuple): 
    return dict((s, getattr(some_named_tuple, s)) for s in some_named_tuple._fields) 

#n = Kulturen['Zwingard']
#print(dict(zip(n._fields, list(n))))

v = ''

for x in KulturenFinal:
    n = KulturenFinal[x]
    z = n.stats
    print(json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+',')
    
    v +=json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+','

    

workfile = r"C:\Users\csiebenkaes\Google Drive\Splittermond\splittermond-chargen\Kulturen.json"
f = open(workfile, 'w')
f.write('['+v[:-1]+']')
#print(z)
#from collections import Counter
#pprint.pprint(Counter(elem for elem in z))

#print(json.dumps(Kulturen['Zwingard'], indent=4, sort_keys=True))