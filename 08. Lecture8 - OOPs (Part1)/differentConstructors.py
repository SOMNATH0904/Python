class Student:

    # Default Constructors
    def __init__(self):
        print("This is a Default Constructor")

    # Parameterized Constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database")
    
s1 = Student("Somnath", 97)
print(s1.name, s1.marks)

s2 = Student("Shaw", 83)
print(s2.name, s2.marks)