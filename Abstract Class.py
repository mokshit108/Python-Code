from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
       pass

class Laptop(Computer):
    def process(self):
        print("it is running")

'''class whiteboard:
    def write(self):
        ("it is writing")'''


class Programmer:
    def work(self,com):
        print("Solving problem")
        com.process()

'''com = Computer()
com.process()'''
lap = Laptop()
#lap2 = whiteboard()
lap.process()
prog1 = Programmer()
prog1.work(lap)
