class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        # self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    # def calcPercentage(self):
    #     self.percentage = str((self.phy + self.chem + self.maths) / 3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.maths) / 3) + "%"

stu1 = Student(90, 87, 95)
print(stu1.percentage)

stu1.phy = 86
print(stu1.phy)     # -> Marks will change
# print(stu1.percentage)    # -> But, the percentage will same as of previous data
print(stu1.percentage)      # -> But, in this case, i.e, after using the @property decorator, there will be no error. We will get the correct value.