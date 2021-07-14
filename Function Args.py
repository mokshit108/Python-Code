def update(x):
    print(id(x))
    x = int(input('Enter a new pin'))
    print(id(x))
    print("x",x)
y = int(input('Enter a pin'))


print(id(y))
#print(y)
update(y)
print("y",y)