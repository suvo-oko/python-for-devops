class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def car_description(self):
        print(f"This car is a {self.year} {self.make} {self.model}")

my_car = Car("Ford", "Mustang", 1972)

my_car.car_description()