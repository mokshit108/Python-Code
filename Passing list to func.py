def count (lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd;



lst = [20,24,2,4,8,8,9,7,5,3,1,5,9]
even, odd = count(lst)
print("Even: {} and Odd: {}".format(even,odd))


more = []
less = []
lst = []

def count(lst):
    for i in lst:
        if len(i) >= 5:
            more.append(i)
        else:
            less.append(i)
    return more, less


x = int(input("Enter the limit:>"))

for i in range(x):
    lst.append(input("Enter the name:>"))

more, less = count(lst)
print("Names with more than 5 characters",more,"\n")
print("Names with less than 5 characters",less)





