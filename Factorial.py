def fact(x):
    '''if(x>0):
        if(x==1):
            print(0)
        else:
        '''
    f=1
    for i in range(1,x+1):
        f=f*i
    return f
result = fact(5)
print(result)


