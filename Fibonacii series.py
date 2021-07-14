def fib(n):
    a=0
    b=1
    if (n<0):
        print("Wrong Input")
    else:
        if n == 1:
            print(a)
        else:
            print(a)
            print(b)
            for i in range(2,n):
               c = a+b
               a=b
               b=c
               print(c)


x =int(input("Enter a Number"))
if x<=89:
    fib(x)
else:
    print("Try Again")


