a = 10
print(id(a))

def something():

    a=50
    #a=15
    #b=8
    x = globals()['a']
    print(id(x))
    print("Local",a)
    globals()['a'] = 15

#print(b)#error
something()

print("global",a)

