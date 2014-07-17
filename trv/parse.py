import sys
import graphviz
import re
import os
import glob
import json
filename = 'test.txt'
flags = re.DOTALL|re.I
createproc = re.compile(r"""\s*create procedure (?P<procedurename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
callproc = re.compile(r"""\s*call (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
droptable = re.compile(r"""\s*drop table (if exists)* (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
createtable = re.compile(r"""\s*create table (if not exists)* (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
createindex = re.compile(r"""\s*create index [a-zA-Z_0-9. ]*on (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
altertable = re.compile(r"""\s*alter table (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
inserttable = re.compile(r"""\s*insert (ignore )*into (?P<tablename>[a-zA-Z_0-9.]+)\s*""", 
           flags)
updatetable = re.compile(r"""\s*update (?P<tablename>.*?)\s* set""", 
           flags)
deletetable = re.compile(r"""\s*delete [a-zA-Z_0-9. ]*from[\r\n\s]*(?P<tablename>\S+)[\r\n\s]+""", 
           flags)
selecttable = re.compile(r"""select.*from (?P<tablename>.*?) (where|group|order|$|limit)""", 
           flags)

callexp = [callproc]
readexp = [selecttable]
writeexp = [droptable,createtable,createindex,altertable,inserttable,updatetable,deletetable]

from collections import namedtuple
parsedprocedure = namedtuple('ParsedProcedure', 'name writetables readtables callprocs')

blacklist = ['into', 'qs01', 'qs_s', 'qs02', 'pclpd','select','group','startDate','where','qs00','qs03','pptc','pptcm','ptres','(date_id']
procedureblacklist = ['updatePartnerArchive', 'archive_item_relevance2_old', 'adblocking_clickshare',
                      'updateSpiderLog','createDumpTables','aggregatesemsList','updateHotelierKpis',
                      'updateAdExposureDevelopment','selectParterCoTrackingVemas','updateDummy','pptcm','ptres']

ListOfProcedures = {}

# Read the file contents and generate a list with each line


def removeComments(string):
    string = re.sub(re.compile("if \(select.*",flags ) ,"" ,string)
    string = re.sub(re.compile("on duplicate.*",flags ) ,"" ,string)
    string = re.sub(re.compile("on \(.*\)",flags ) ,"" ,string)
    string = re.sub(re.compile("\( select.*\)",flags ) ,"" ,string)
    string = re.sub(re.compile("[a-zA-Z0-9_\.\*]+ [<>=]+ ['a-zA-Z0-9_\.]+",flags ) ,"" ,string)
    string = re.sub(re.compile("/\*.*?\*/",flags ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("--.*?\n" ) ,"" ,string) # remove all occurance singleline comments (--COMMENT\n ) from string
    string = re.sub(re.compile("#.*?\n" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    string = re.sub(re.compile("call logQueryTime" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    string = re.sub(re.compile("\)",flags ) ," \)" ,string)
    return string

def splitjoins(string):
    string = removeComments(string)
    string = re.sub(r"""(straight)*(left)*(\s)*(outer )*(\s)*join|as [a-zA-Z0-9_,\n]+|\([a-zA-Z0-9_= ,\.]+\)|using| on| and|\n|,""",'',string, flags)
    tables = string.split(' ')
    tables = [x for x in tables if x and len(x) > 3]
    return  tables

def addtablematch(trv_sourcestring,trv_regexp,trv_target):
    #print(trv_sourcestring)
    trv_match_exists = trv_regexp.search(trv_sourcestring)
    if trv_match_exists:
        #print(trv_match_exists.group("tablename"))
        tablenames = splitjoins(trv_match_exists.group("tablename"))
        #print(tablenames)
        for tablename in tablenames:
            if tablename not in trv_target and 'temp' not in tablename and tablename not in blacklist:
                trv_target.append(tablename)

def parsesqlfile(filename):
    with open(filename, 'r') as f:
        data=f.read()
    procedures = re.split('//|\|\|',data)
    for element in procedures:
        element = removeComments(element)
        commands = element.split(';')
        procedure = ''
        writetables = []
        readtables = []
        calltables = []
        for command in commands:
            command = removeComments(command)
            command = re.sub(r"""\r|\n|\s""",' ',command, flags = re.I)
            command = command.strip()
            command = " ".join(command.split())
            #print(command)
            procedurematch = createproc.match(command)
            if procedurematch:
                procedure = procedurematch.group("procedurename")
            for element in callexp:
                addtablematch(command,element,calltables)
            for element in writeexp:
                addtablematch(command,element,writetables)
            for element in readexp:
                addtablematch(command,element,readtables)
        if procedure:
            ListOfProcedures[procedure] = parsedprocedure(procedure,writetables,readtables, calltables)


path = r'D:\workspace\analytic\stored_procedures'
for filename in glob.glob(os.path.join(path, '*.sql')):
    #parsesqlfile(filename)
    pass

#parsesqlfile(r'D:\workspace\analytic\stored_procedures\63_FirstPosDilution.sql')
    


for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if '.sql' in name:
            #print(os.path.join(root, name))
            try:
                parsesqlfile(os.path.join(root, name))
            except ValueError:
                pass
            
dot = graphviz.Digraph(comment='Dependency Table BI')
drawnwritetables = []
drawnreadtables = []
for procedure in ListOfProcedures:   
    n = ListOfProcedures[procedure]
    if n.name not in procedureblacklist and '(' not in n.name and ')' not in n.name:
        dot.node(n.name, shape= 'box', fontsize = '14')
        for readt in n.readtables:
            if readt not in drawnreadtables:
                dot.node(readt, fontsize = '14')
                drawnreadtables += [readt]
            dot.edge(readt, n.name)
        
        for writet in n.writetables:
            if writet not in drawnwritetables:
                dot.node(writet, fontsize = '14')
                drawnreadtables += [writet]
            dot.edge(n.name, writet)
    #print(json.dumps(dict(zip(n._fields, list(n)) ), indent=4, sort_keys=True))
    #
#print(dot.source)

workfile = r"C:\Users\csiebenkaes\Pictures\workfile.gv"
f = open(workfile, 'w')
f.write(dot.source)
#dot.render(workfile, view=True)