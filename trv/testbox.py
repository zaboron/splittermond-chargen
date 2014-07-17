import re
import os
import glob
import json
filename = 'test.txt'
flags = re.DOTALL|re.I
pld_type = re.compile(r"""\s*type = (?P<tablename>[0-9]+)\s*""", 
           flags)
subquery = re.compile("\((?P<subquery>.*)\)",re.DOTALL)
def splitjoins(string):
    test = subquery.findall(string)
    string = re.sub(re.compile("on \(.*\)",re.DOTALL ) ,"" ,string)
    string = re.sub(r"""on \([a-zA-Z0-9_= ,\.]+\)""",'',string, flags = flags)
    #string = re.sub(r"""(left)*(\s)*(outer )*(\s)*join|as [a-zA-Z0-9_,\n]+|\([a-zA-Z0-9_= ,\.]+\)|using| on |\n|,""",'',string, flags = flags)
    tables = string.split(' ')
    tables = [x for x in tables if x and len(x) > 3]
    return  tables,test

def removeComments(string):
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("--.*?\n" ) ,"" ,string) # remove all occurance singleline comments (--COMMENT\n ) from string
    string = re.sub(re.compile("#.*?\n" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    string = re.sub(re.compile("call logQueryTime" ) ,"" ,string) # remove all occurance singleline comments (#COMMENT\n ) from string
    return string

teststring = r"""create temporary table temp_pld_64_date_ids engine = memory as select date_id, data from page_log_detail where date_id between concat(startDate, '00000000000') + 0 and concat(endDate, '24000000000') + 0 and type = 64"""

print(pld_type.findall(teststring))

trv_match_exists = pld_type.search(teststring)
if trv_match_exists:
       # print(trv_match_exists.group("tablename"))
        tablenames = splitjoins(trv_match_exists.group("tablename"))
        print(tablenames)
        for tablename in tablenames:
            #print(tablename)
            pass