class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 in A")
    def feature2(self):
        print("feature 2 in A")

class B(A):
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("feature 3 in B")
    def feature4(self):
        print("feature 4 in B")

class C(B):
    def __init__(self):
        print("in C init")
    def feature5(self):
        print("feature 5 in C")
    def feature6(self):
        print("feature 6 in C")
z=C()
z.feature1()
