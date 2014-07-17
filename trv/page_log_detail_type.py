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
pld_type = re.compile(r"""\s*type = (?P<tablename>[0-9]+)\s*""", 
           flags)


def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",flags ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("--.*?\n" ) ,"" ,string) # remove all occurance singleline comments (--COMMENT\n ) from string
    string = re.sub(re.compile("#.*?\n" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    string = re.sub(re.compile("call logQueryTime" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    return string

def splitjoins(string):
    string = removeComments(string)
    tables = string.split(' ')
    tables = [x for x in tables if x and len(x) > 3]
    return  tables

def addtablematch(trv_sourcestring,trv_regexp,trv_target,proc):
    #print(trv_sourcestring)
    trv_match_exists = trv_regexp.findall(trv_sourcestring)
    for element in trv_match_exists:
        trv_target[proc] = trv_match_exists

def parsesqlfile(filename):
    with open(filename, 'r') as f:
        data=f.read()
    procedures = re.split('//|\|\|',data)
    procname = ''
    for element in procedures:
        element = removeComments(element)
        procedurematch = createproc.match(element)
        if procedurematch:
            procname = procedurematch.group("procedurename")
        commands = element.split(';')
        for command in commands:
            command = removeComments(command)
            command = re.sub(r"""\r|\n|\s""",' ',command, flags = re.I)
            command = command.strip()
            command = " ".join(command.split())
            if 'page_log_detail' in command:
                #print(command)
                addtablematch(command,pld_type,writetables,procname)


writetables = {}
path = r'D:\workspace\analytic\stored_procedures'

#parsesqlfile(r'D:\workspace\analytic\stored_procedures\63_FirstPosDilution.sql')
    

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        if '.sql' in name:
            #print(os.path.join(root, name))
            try:
                parsesqlfile(os.path.join(root, name))
            except ValueError:
                pass

print(json.dumps(writetables , indent=4, sort_keys=True))

all_plds = []
for element in writetables:
    for pldtype in writetables[element]:
        if pldtype not in all_plds:
            all_plds.append(pldtype)
            
print(all_plds)