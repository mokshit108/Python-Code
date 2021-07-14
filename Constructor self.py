class computer:
    def __init__(self):
        self.name ="Mokshit"
        self.age = 18

    def update(self):
        self.age=30
    def compare(self,c2):
        if self.age == c2.age:
            return True
        else:
            return False






c1 = computer()
c2 = computer()
'''c1.name="Rashi"'''
c1.age = 12

if c1.compare(c2):
    print("There are same")
else:
    print("There are different")

print(c1.name)
print(c2.name)
c1.update()