from collections import namedtuple
from random import randint
Rasse = namedtuple('Rasse', 'name Attributsmodifikatoren Größenklasse Stärken Farbenart Haarfarbe Augenfarbe Körpergröße Gewicht')

class Charakter():
    def __init__(self):
        pass
Rassen = {}
Rassen['Alb'] = Rasse('Alb',{'AUS':'1','BEW':'1','BEL':'1','KON':'-1'},5,['Attraktivität','Scharfes Gehör','Dämmersicht'],'Hautfarbe',
{'silberweiß':[2,3],'weißblond':[4,5],'goldblond':[6,7,8],'dunkelblond':[9,10],
'hellbraun':[11,12],'dunkelbraun':[13,14],'rotbraun':[15,16],'kupferrot':[17,18],'blauschwarz':[19,20]},
{'schwarz':[2,],'grau':[3,4],'graublau':[5,6],'blau':[7,8,9,10],
'braun':[11,12,13,14],'grün':[15,16,17],'bernsteinfarben':[18,19],'golden':[20]},
[160, 5],[50, 100])


Rassen['Gnom'] = Rasse('Gnom',{'MYS':'1','VER':'1','BEL':'1','STÄ':'-1'},3,['Feensinn','Hoher Geistiger Widerstand','Flink'],'Hautfarbe',
{'aschgrau':[2,],'weißblond':[3,],'blond':[6,4,5],'dunkelblond':[9,8,7],
'rotblond':[11,10],'rot':[13,12],'hellbraun':[15,14],'dunkelbraun':[17,16],'blauschwarz':[19,18], 'blassblau':[20]},
{'orange':[2,],'grau':[3,4],'aquamarin':[5,6],'dunkelblau':[7,8,9,10],
'dunkelgrün':[11,12,13,14],'hellgrün':[15,16,17],'schwarz':[18,19],'violett':[20]},
[105,2],[20, 35])


Rassen['Mensch'] = Rasse('Mensch',{'BEL':'2'},5,['Zusätzliche Splitterpunkte'],'Hautfarbe',
{'rot':[2,3],'hellblond':[4,5,],'dunkelblond':[6,7,8],'hellbraun':[9,10,11,12],
'dunkelbraun':[13,14,15],'schwarz':[16,17,18,19],'grau':[20]},
{'grau':[2,],'graublau':[3,4],'blau':[5,6],'grünblau':[7,8,9,10],
'grün':[11,12,13,14],'braun':[15,16,17],'goldbraun':[18,19],'golden':[20]},
[152,5],[50, 120])

Rassen['Varg'] = Rasse('Varg',{'STÄ':'2','BEL':'1','WIL':'-1'},6,['Natürlicher Rüstungsschutz','Ausdauernd','Natürliche Waffe'],'Fellfarbe',
{'sandfarben':[2,3],'ocker':[4,5,6],'hellbraun':[9,10,7,8],'dunkelbraun':[13,11,12],
'dunkelgrau':[16,14,15],'schwarz':[20,17,18,19]},
{'schwarz':[2,3],'goldbraun':[6,5,4],'bernsteinfarben':[7,8,9,10,11,12,13,14],
'bernsteinfarben mit grauen Sprengseln':[15,16,17,18,19],'eisblau':[20]},
[200,3],[110, 160])

Rassen['Zwerg'] = Rasse('Zwerg',{'KON':'1','WIL':'1','BEL':'1','BEW':'-1'},4,['Giftresistenz','Robust','Orientierungssinn'],'Hautfarbe',
{'weiß':[2,3],'hellblond':[4,5,6],'dunkelblond':[9,7,8],'hellbraun':[10,11,12],
'dunkelbraun':[13,14],'schwarz':[16,17,18,15],'feuerrot':[19,20]},
{'schwarz':[2,],'grau':[3,4],'dunkelbraun':[5,6],'hellbraun':[7,8,9,10],
'grünbraun':[11,12,13,14],'grün':[15,16,17],'kupferfarben':[18,19],'silbern':[20]},
[135,2],[60, 100])


def bestimmeFarbe(Farbenliste):
    Ergebnis = randint(1,10)+ randint(1,10)
    for Farbe, Wurf in Farbenliste.items():
        if Ergebnis in Wurf:
            return(Farbe)
        
def bestimmeStatur(Größe, Gewicht):
    Ergebnis = sum(randint(1,10) for x in range(Größe[1]))
    return Ergebnis+Größe[0], int(Gewicht[0]+ Ergebnis/(Größe[1]*10)*(Gewicht[1]-Gewicht[0]))
    
def bestimmeHaarfarbe(Charakter):
    Charakter.Haarfarbe = bestimmeFarbe(Charakter.Rasse.Haarfarbe)
    return Charakter.Haarfarbe

def bestimmeAugenFarbe(Charakter):
    Charakter.Augenfarbe = bestimmeFarbe(Charakter.Rasse.Augenfarbe)
    return Charakter.Augenfarbe
        
Charakter.Rasse = Rassen['Gnom']
'''
print(Charakter.Rasse.name)
print(Charakter.Rasse.Farbenart + ": " + bestimmeHaarfarbe(Charakter))
print("Augenfarbe: " + bestimmeAugenFarbe(Charakter))
Charakterstatur = bestimmeStatur(Charakter.Rasse.Körpergröße, Charakter.Rasse.Gewicht)
'''