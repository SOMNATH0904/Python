class Student:
    collegeNmae = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome Student,",self.name)

    def getMarks(self):
        return self.marks

s1 = Student("Somnath", 97)
s1.welcome()
print("Marks:",s1.getMarks())