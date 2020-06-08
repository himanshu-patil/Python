class student:
    school = "himanshu"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("this is static method")

s1=student(34,87,95)
s2=student(55,77,22)
s3=student(88,11,22)
print(s1.avg())
print(student.getschool())
student.info()









