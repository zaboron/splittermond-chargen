import json
from kulturen import *
import codecs
from collections import Counter
jsonfertigkeiten = list(json.load(codecs.open('fertigkeiten.json', "r", "utf-8"),encoding= 'UTF-8').keys())
jsonstaerken = list(json.load(codecs.open('staerken.json', "r", "utf-8"),encoding= 'UTF-8').keys())
print(x)

def abgleicheElemente(a,b):
    print('in a but not b')
    for e in a:
        if e not in b:
            print(e)   
    print('in b but not a')
    for e in b:
        if e not in a:
            print(e)

abgleicheElemente(Fertigkeitenliste,jsonfertigkeiten)
abgleicheElemente(Stärkenliste,jsonstaerken)

