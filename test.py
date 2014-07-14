import abstammungen
import kulturen
testabst = ["alle au\u00dfer Hochadel",
        "H\u00f6flinge und Landadel"]
testabst2 = [
        "Einsiedler",
        "Handwerker",
        "Kleinbauern",
        "Kriegsvolk",
        "Reisende",
        "Zauberer"
    ]


def parseAbstammung(akzeptierteAbstammungRaw):
    if type(akzeptierteAbstammungRaw) is str:
        akzeptierteAbstammungRaw = [akzeptierteAbstammungRaw]
    else:
        akzeptierteAbstammungRaw = akzeptierteAbstammungRaw
    akzeptierteAbstammungRaw =  ' '.join(akzeptierteAbstammungRaw)
    akzeptierteAbstammung = []
    if 'alle' in akzeptierteAbstammungRaw:
        akzeptierteAbstammung += abstammungen.ListeAbstammungen
        if 'außer' in akzeptierteAbstammungRaw:
            ausnahmen = akzeptierteAbstammungRaw.rsplit(sep = ' außer ', maxsplit = 1)[1]
            for ausnahme in ausnahmen.split(' '):
                try:
                    akzeptierteAbstammung.remove(ausnahme)
                except ValueError:
                    pass    
                
    else:
        akzeptierteAbstammung += akzeptierteAbstammungRaw.split(sep = ' ')
    return akzeptierteAbstammung

for x in kulturen.Kulturen:
    print(parseAbstammung(kulturen.Kulturen[x].Abstammungen))