import re
filename = 'test.txt'
createproc = re.compile(r"""\s*create procedure (?P<procedurename>[a-zA-Z_0-9.]+)\s*""")
droptable = re.compile(r"""\s*drop table (if exists)* (?P<tablename>[a-zA-Z_0-9.]+)\s*""")
createtable = re.compile(r"""\s*create table (if not exists)* (?P<tablename>[a-zA-Z_0-9.]+)\s*""")
createindex = re.compile(r"""\s*create index [a-zA-Z_0-9. ]*on (?P<tablename>[a-zA-Z_0-9.]+)\s*""")
altertable = re.compile(r"""\s*alter table (?P<tablename>[a-zA-Z_0-9.]+)\s*""")
inserttable = re.compile(r"""\s*insert into (?P<tablename>[a-zA-Z_0-9.]+)\s*""")
updatetable = re.compile(r"""\s*update (?P<tablename>[a-zA-Z_0-9.]+)\s* set""")
deletetable = re.compile(r"""\s*delete [a-zA-Z_0-9. ]*from (?P<tablename>[a-zA-Z_0-9., ]+)\s*""")

selecttable = re.compile(r"""[(\)\-\sa-zA-Z_0-9*,. ]*\s*select [\r\n\(\)\-\sa-zA-Z_0-9*,. ]*from[\s\r\n]* (?P<tablename>[a-zA-Z_0-9.\r\n]+)(?=(\s|where|group|order|limit))*""")
selecttable2 = re.compile(r"""(?<=from)(?P<tablename>.*)(?=where)""")
test = selecttable2

new_file = []
textcontent =''

from collections import namedtuple
parsedprocedure = namedtuple('ParsedProcedure', 'name writetables readtables')

with open(filename, 'r') as f:
    data=f.read()
# Read the file contents and generate a list with each line
    
def addtablematch(trv_sourcestring,trv_regexp,trv_target):
    trv_match_exists = trv_regexp.match(trv_sourcestring)
    if trv_match_exists:
            tablename = trv_match_exists.group("tablename")
            if tablename not in trv_target:
                trv_target.append(tablename)

procedures = re.split('//|\|\|',data)
for element in procedures:
    commands = element.split(';')
    procedure = ''
    writetables = []
    for command in commands:
        procedurematch = createproc.match(command)
        if procedurematch:
            procedure = procedurematch.group("procedurename")
            createtablematch = createtable.match(command)
        addtablematch(command,test,writetables)
    print(procedure,writetables)   
        
    #print(element)

print(procedures[1])
'''
# Iterate each line
for line in lines:

    # Regex applied to each line 
    match = regex.match(f)
    if match:
        # Make sure to add \n to display correctly when we write it back
        new_line = match.group() + '\n'
        print(match.group("procedurename"))
        
        new_file.append(new_line)
        
'''