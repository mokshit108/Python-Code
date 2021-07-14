from array import *
vals = array('i',[5,9,8,4,2])
Newarr = array(vals.typecode, (a*a for a in vals))
print(vals)
for i in Newarr:
    print(i)
for i in vals:
    print(i)
    '''range(len(vals)):'''

