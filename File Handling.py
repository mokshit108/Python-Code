
f = open('MyData','r')
f1 = open('MyData2','a')

for data in f:
   f1.write(data)
