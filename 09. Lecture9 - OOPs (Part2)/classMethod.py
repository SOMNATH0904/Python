class Person:
    name = "anonymous"

    # def changeName(self, name):  # -> One way of using classMethod
    #     Person.name = name

    # def changeName(self, name): # -> Second way of using classMethod
    #     self.__class__.name = "Somnath"

    # Actual use of classMethod
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Somnath Shaw")
print(p1.name)
print(Person.name)