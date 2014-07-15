import re
selecttable = re.compile(r"""(?<=from )(?P<tablename>.*)(?= where)""")
teststring = 'create table select test   from trivago_analytic.temppb_bidding20 join analzitcs, blabla where bla'
match =selecttable.match(teststring)
if match:
    print(match.group("tablename"))
    
print(re.findall ( 'from (.*?) (where|group|order|limit)', teststring, re.DOTALL))