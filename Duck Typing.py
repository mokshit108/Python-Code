class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditior:
    def execute(self):
        print("Compiling")
        print("Running")
        print("Spell Checking")
        print("Convention check")


class Laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditior()
lap1 = Laptop()
lap1.code(ide)

