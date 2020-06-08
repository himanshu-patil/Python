class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("feature 1 in A")
    def feature2(self):
        print("feature 2 in A")

class B:
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("feature 1 in B")
    def feature4(self):
        print("feature 4 in B")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")
    def feat(self):
        super.feature2()

z=C()
z.feat()
