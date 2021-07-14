#1.Filter
#2.Map
#3 Reduce
'''def is_even(a):
    return a%2==0

nums= [7,4,8,5,9,6,2,1]
evens = list(filter(is_even,nums))
print(evens)'''
# with lambda

from functools import reduce
'''def add_all(a,b):
    return a+b'''
nums= [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n:n%2==0,nums))

doubles = list(map(lambda n: n*2,evens))
sum = reduce(lambda a,b:a+b,doubles)

print(doubles)
print(sum)