

def greet():
    print("Hello")
    print("Good Morning")

def add_sub(x,y):
    a=x+y
    b=x-y
    #print(a)
    return a,b

'''add(4,5)
add(10,15)'''
result_sum, result_sub = add_sub(100,80)
print(result_sum)
print(result_sub)