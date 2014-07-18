import pprint
import codecs
import json
import operator
from parsesplimo import *
import re
flags = re.DOTALL|re.I


from collections import namedtuple
Zauber = namedtuple('Zauber', 'name schulen Dauer Wirkungsdauer Zauberkosten Optionen Reichweite Schwierigkeit Typus Wirkung Verst\u00e4rkt')


def removeKlammern(string):
    string = re.sub(re.compile("\(.*\)",flags ) ,"" ,string)

    return string

with codecs.open('zauber.txt', "r", "utf-8") as f:
    lines = [x.splitlines() for x in f.readlines()[1:]]
    attribute = []
    for x in lines:
        attribute += [splitstrip(y,':') for y in x]
    
Zauberen = {}

for row in attribute:
    for i, field in enumerate(row):
        if '•' in row[i]:
            tempz = row[i].rsplit('•', maxsplit = 1)[1]
            tempz = tempz.rsplit(' ',maxsplit = 1)[1]
            row[4] += ' ('+tempz
        row[i] = field.rsplit(' ', maxsplit = 1)[0]  
        row[i] = row[i].rsplit('•', maxsplit = 1)[0]   
        row[i] = row[i].strip()
        row[i] = re.sub(re.compile(r'\•',flags ) ,"" ,row[i])
        
    row[0] = removeKlammern(row[0])
    row[0] = row[0].strip()  
    
    #print(len(row))
    #print(row)    
    if len(row) == 12:
        Zauberen[row[0]] = Zauber(*operator.itemgetter(0,1,5,8,4,10,6,3,2,7,11)(row))
    else:
        if len(row) == 11:
            Zauberen[row[0]] = Zauber(*operator.itemgetter(0,1,5,8,4,9,6,3,2,7,10)(row))
        else:
            Zauberen[row[0]] = Zauber(*operator.itemgetter(0,1,5,2,4,8,6,3,2,7,9)(row))

for row in attribute:
    for i, field in enumerate(row):
        if ',' in field:
            row[i] = splitstrip(field,',')
            
for Zauber in Zauberen.keys():
    Schulenliste = {}
    for element in splitstrip(Zauberen[Zauber].schulen,','):
        Schulenliste[element.split(' ')[0]] = element.split(' ')[1]  
    Zauberen[Zauber] = Zauberen[Zauber]._replace(schulen = Schulenliste)
    Zauberen[Zauber] = Zauberen[Zauber]._replace(Optionen = [x.strip() for x in Zauberen[Zauber].Optionen.split(',') if 'Verst' not in x])

  
v = ''
for x in Zauberen:
    n = Zauberen[x]
    print(json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+',')
    v +=json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True)+','

    

workfile = r".\Zauber.json"
f = open(workfile, 'w')
f.write('['+v[:-1]+']')