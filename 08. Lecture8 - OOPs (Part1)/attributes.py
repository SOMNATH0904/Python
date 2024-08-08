class Student:
    collegeName = "ABC College"
    name = "anonymous"  #class attr

    def __init__(self, name, marks):
        self.name = name    #obj attr   (Object attribute > Class attribute)
        self.marks = marks


s1 = Student("Somnath", 97)
print(s1.name) 

print(s1.collegeName)