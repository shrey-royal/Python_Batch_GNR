"""
Classes and Objects:
- The Class can be defined as a collection of objects. It is a logical entity and has some specific attribuets and methods.
- The Object is an entity that has state and behaviour.
"""

class Car:
    # attributes / states
    model: str
    year: int

    # methods / methods
    def set_car_details(self, model, year):
        self.model = model
        self.year = year

    def get_car_details(self):
        return f"(Model: {self.model}, Year: {self.year})"


car = Car() # initialize/instantiate
c1 = Car()

car.set_car_details("Toyota Fortuner", 2024)
print(car.get_car_details())

c1.set_car_details("Toyota", 2024)
c1.make = "Fortuner"    # adding extra attribute for this specific object only
print(c1.get_car_details(), c1.make)

# Adding attrs when needed
car.owner = "kaushal"
c1.owner = "Dhruv"
print(car.owner, c1.owner)