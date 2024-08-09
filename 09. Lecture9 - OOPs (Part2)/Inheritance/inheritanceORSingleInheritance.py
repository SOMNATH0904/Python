# This is an example of Single Inheritance

class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")

class TataCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TataCar("Nexon")
car2 = TataCar("Harrier")

car1.start()
car2.stop()
print(car1.color)