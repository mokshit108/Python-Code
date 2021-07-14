class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


        print("in init")
    def config(self):
        print("Config is",self.cpu,self.ram)

'''
a =5
print(type(a))
'''
com1 = Computer("i5",16)
com2 = Computer("Ryzen 3",15)
#print(type(com1))
'''Computer.config(com1)
Computer.config(com2)'''
com1.config()
com2.config()