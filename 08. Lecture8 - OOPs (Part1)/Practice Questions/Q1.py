# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

'''
class Student:

    def __init__(self, name, phy, chem, maths):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def calcAverage(self):
        return (self.phy + self.chem + self.maths) / 3
    

s1 = Student("Somnath", 81, 87, 89)
print("Average marks of",s1.name,"in three subjects is :",s1.calcAverage())
'''

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def getAverage(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, ", Your Average Score is :", sum/3)


s1 = Student("Somnath", [81, 85, 89])
s1.getAverage()

s1.name = "Raja"
s1.getAverage()