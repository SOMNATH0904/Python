class Base:
    def __init__(self):
        self.a = 2

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class :",self.a)

        self.a = 3
        print("Calling modified protected member outside class :",self.a)


obj1 = Derived()
obj2 = Base()
print("Accessing protected member of obj1: ", obj1.a)
print("Accessing protected member of obj2: ", obj2.a)
