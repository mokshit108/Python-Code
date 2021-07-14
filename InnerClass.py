
class Student:
    def __init__(self,name,rollno):
        self.name= name
        self.rollno = rollno
        self.lap =self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand ="Hp"
            self.cpu = 'i5'
            self.ram = 0

        def show(self):
            print(self.brand, self.cpu , self.ram)



s1 = Student('Navni',20)
s2 = Student("Jenny",17)

s1.show()

lap3 = Student.Laptop()
lap1 = s1.lap
lap2 = s2.lap
print(id(lap2))
print(id(lap1))