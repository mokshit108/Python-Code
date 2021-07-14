class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature A1")

    def feature2(self):
        print("Feature A2")


'''class B(A):
    def __init__(self):
        super().__init__()
        print(" in B init")
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")
        
'''


class B:
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature1(self):
        print("Feature B1")

    def feature2(self):
        print("Feature B2")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feat(self):
       super().feature2()




a1 = C()
a1.feature1()
a1.feat()



