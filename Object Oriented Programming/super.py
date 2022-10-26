class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduction(self):
        print(self.name)

class Student(Person):
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa

class Teacher(Person):
    def __init__(self, name, age, course):
        self.course = course

myStudent = Student("Thomas", 23, 3.5)

myStudent.introduction()