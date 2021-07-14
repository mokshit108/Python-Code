def person(name, **data):
    print(name)
    #print(data)
    for i,j in data.items():
        print(i,j)

person('navin',age = 28, city ='mumbai', number =98765432)