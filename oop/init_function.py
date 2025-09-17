class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def getStudent(self):
        print(self.name,self.age)

s1 = Student('Sam',25)
s2 = Student('Brin',20)
s3 = Student('Joe',22)
s4 = Student('Shawn',24)

students = [s1,s2,s3,s4]
for s in students:
    s.getStudent()