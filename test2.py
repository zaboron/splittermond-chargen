
from collections import Counter
def zehn(ziffer):
    if int(ziffer) == 0:
        return 10
    else:
        return int(ziffer)

diff = []
for w in range(0,100000):
    list_of_ints = [zehn(i) for i in str(w)] + [ 10 for i in range(0,5)]
    result = sorted(list_of_ints[:4])
    if sum(result[0:2]) < 4:
        x = sum(result[0:2])
        y = sum(result[0:2])
    else:
        x = sum(result[2:4])
        y = sorted([result[0],result[2],result[3],list_of_ints[4]])
        if sum(y[0:2]) < 4:
            y = sum(y[0:2])
        else:
            y = sum(y[2:4])
    diff += [str(y-x)]
    

print(Counter(elem[0] for elem in diff))