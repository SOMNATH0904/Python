'''
Ques: Define an Employee class with attributes role, department & salary. This class also has a showDetails() method.
      Create an Engineer class that inherits properties from Employees & has additional attributes : name & age.
'''

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showDetails(self):
        print("Role:", self.role)
        print("Dept:", self.dept)
        print("Salary:", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")


# emp1 = Employee("Accountant", "Finance", "60,000")
# emp1.showDetails()

er1 = Engineer("Somnath", 21)
er1.showDetails()