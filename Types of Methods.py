#1 instance method
#2 class method
#3 static method

class Student:

    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return ( self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school
    @staticmethod
    def infostatic():
        print("This is student static method")

""" def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value
        """

s1 = Student(34,77,89)
s2 = Student(89,32,12)

print(s1.avg())
print(Student.info())
Student.infostatic()