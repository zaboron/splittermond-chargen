ListeAbstammungen = ['Kleinbauern', 'Gesindel', 'Händler', 'Künstler', 'Priester', 'Seefahrer', 'Kriegsvolk', 'Magistrale', 'Hochadel', 'Großbauern', 'Handwerker', 'Höflinge', 'Gelehrte', 'Reisende', 'Zauberer', 'Landadel']

def inOptionenAufteilen(element):
        Optionsseintrag = {}
        Option = element.rsplit(' ',1)
        Option[0] = Option[0].replace('eine Kampffertigkeit','Handgemenge oder Klingenwaffen oder Stangenwaffen oder Kettenwaffen oder Wurfwaffen oder Schusswaffen oder Hiebwaffen')
        Option[0] = Option[0].replace('eine Waffenfertigkeit','Handgemenge oder Klingenwaffen oder Stangenwaffen oder Kettenwaffen oder Wurfwaffen oder Schusswaffen oder Hiebwaffen')
        Option[0] = Option[0].replace('eine Nahkampffertigkeit','Handgemenge oder Klingenwaffen oder Stangenwaffen oder Kettenwaffen oder Hiebwaffen')
        Option[0] = Option[0].replace('eine Magieschule','Bann oder Beherrschung oder Bewegung oder Erkenntnis oder Fels oder Feuer oder Heilung oder Illusion oder Kampf oder Licht oder Natur oder Schatten oder Schicksal oder Schutz oder Stärkung oder Tod oder Verwandlung oder Wasser oder Wind')
        Option[0] = Option[0].split(' oder ')
        for i,value in enumerate(Option[0]):
            Option[0][i] = Option[0][i].strip() 
        Optionsseintrag['options'] = Option[0]
        Optionsseintrag['value'] = int(Option[1])
        return Optionsseintrag

def splitstrip(string,sep):
    splitstring = string.split(sep)
    for i, x in enumerate(splitstring):
        splitstring[i] = x.strip()
    return splitstring

def aufteilen(string):
    if ')' in string:
        x = string.split(sep = ') oder ')
        ParsedErgebnis = {}
        for y in x:
            Fertigkeit = y.split(sep = ' ')[0]
            Meisterschaft = y.split(sep = '(')[1]
            Meisterschaft = Meisterschaft.strip('()')
            if 'oder' in Meisterschaft:
                Meisterschaft = Meisterschaft.split(sep = ' oder ')
            ParsedErgebnis[Fertigkeit.strip()] = Meisterschaft
        return ParsedErgebnis
    
def parseAbstammung(akzeptierteAbstammungRaw):
    if type(akzeptierteAbstammungRaw) is str:
        akzeptierteAbstammungRaw = [akzeptierteAbstammungRaw]
    else:
        akzeptierteAbstammungRaw = akzeptierteAbstammungRaw
    akzeptierteAbstammungRaw =  ' '.join(akzeptierteAbstammungRaw)
    akzeptierteAbstammung = []
    if 'alle' in akzeptierteAbstammungRaw:
        akzeptierteAbstammung += ListeAbstammungen
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
