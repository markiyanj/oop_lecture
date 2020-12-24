class Car:
    def __init__(self):
        print("Engine started")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999

car_a = Car()
print(car_a.name)
print(car_a._model)
print(car_a.__make)
