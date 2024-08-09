class Car:

    @staticmethod
    def start():
        print("Car Started ...")

    @staticmethod
    def stop():
        print("Car Stopped ...")

class TataCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Nexon(TataCar):
    def __init__(self, type):
        self.type = type

car1 = Nexon("petrol")
car1.start()