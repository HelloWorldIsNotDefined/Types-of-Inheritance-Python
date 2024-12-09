class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("NAME:",self.name)
        print("AGE:",self.age)


class Teacher(Person):
    def __init__(self,name,age,exp,r_area):
        super().__init__(name,age)
        self.exp=exp
        self.r_area=r_area
        
    def displaydata(self):
        super().display()
        print("EXPERIENCE:",self.exp)
        print("RESEARCH AREA:",self.r_area)


class Student(Person):
    def __init__(self,name,age,course,marks):
        super().__init__(name,age)
        self.course=course
        self.marks=marks
        
    def displaydata(self):
        super().display()
        print("COURSE:",self.course)
        print("MARKS:",self.marks)


print("TEACHER")
t = Teacher("jaya",43,20,"recommender systems")
t.displaydata()

print("STUDENT")
s = Student("mani",20,"btech",78)
s.displaydata()
