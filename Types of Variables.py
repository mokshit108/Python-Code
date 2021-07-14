#1 instance
#2 class(static)
class Car:
    wheels = 4

    def __init__(self):
        self.com = "BMW"
        self.mil = 10


c1 = Car()
c2 = Car()
c1.mil = 8
Car.wheels = 5
#print(c1.com ,c1.mil)
#print(c2.com ,c2.mil)
print(c1.com ,c1.wheels)
print(c2.com ,c2.wheels)