class Car:
    def __init__(self, type):
        self.type = type
    
    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")

class TataCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = TataCar("Nexon", "Electric")
print(car1.type)