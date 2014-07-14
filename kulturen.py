import pprint
import codecs
import json
from parsesplimo import *


from collections import namedtuple
Kultur = namedtuple('Kultur', 'name Rassen Abstammungen Muttersprache Kulturkunde Stärke Fertigkeiten Meisterschaften')



with codecs.open('kulturen.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    attribute = []
    for x in lines:
        attribute += [splitstrip(y,';') for y in x]
    
Kulturen = {}

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
    if 'oder' in Kulturen[Kultur].Meisterschaften:
        Meisterschaftenliste.append(aufteilen(Kulturen[Kultur].Meisterschaften))
    else:
        Meisterschaftenliste.append(Kulturen[Kultur].Meisterschaften)
   
  
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Fertigkeiten = Fertigkeitenliste)
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Meisterschaften = Meisterschaftenliste)
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Stärke = inOptionenAufteilen(Kulturen[Kultur].Stärke+' 1'))
    Kulturen[Kultur] = Kulturen[Kultur]._replace(Abstammungen = parseAbstammung(Kulturen[Kultur].Abstammungen))
        
def dictify(some_named_tuple): 
    return dict((s, getattr(some_named_tuple, s)) for s in some_named_tuple._fields) 

#n = Kulturen['Zwingard']
#print(dict(zip(n._fields, list(n))))


Fertigkeitenliste = []
Stärkenliste = []
for x in Kulturen:
    n = Kulturen[x]
    print(json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True))
    for y in n.Fertigkeiten:
        Fertigkeitenliste += y['options']

for x in Kulturen:
    Stärkenliste +=Kulturen[x].Stärke['options']
    
    
#print(z)
#from collections import Counter
#pprint.pprint(Counter(elem for elem in z))

#print(json.dumps(Kulturen['Zwingard'], indent=4, sort_keys=True))