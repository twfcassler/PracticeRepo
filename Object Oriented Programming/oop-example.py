class Student():
    def __init__(self, name, age, gender, gpa, number):
        self.name = name
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.number = number

        self.numCredit = 0
    
    def studentStatus(self):
        if self.gpa > 3:
            return "Good job!"
        elif self.gpa > 2:
            return "You are getting there."
        else:
            return "Uh oh..."

firstStudent = Student("Thomas", 23, "Male", 3.5, 78910)

firstStudent.numCredit += 10
print(firstStudent.name)
print(firstStudent.numCredit)

myStatus = firstStudent.studentStatus()
print(myStatus)

if myStatus == "Good job!":
    print("Yay!")