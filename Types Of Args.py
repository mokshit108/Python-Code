'''def add(a,b):#Formal
    c = a+b
    print(c)
add(5,6)#Actual
'''
'''
1.Postion 
2.Keyword
3.default
4.variable length
'''
#1
'''def person(name,age=18):
    print(name)
    print(age)'''
#person('mokshit',18)#postion 1st name and 2nd age
#2
#person(age=28,name='mokshit')
#3
#person('mokshit')
#4
def add(a,*b):#Formal
    c = a
    for i in b:
        c=c+i
    print(c)

add(5,6,5,4)#Actual