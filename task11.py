class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

vehicle1 = Vehicle("GenericBrand", "ModelX")
vehicle1.move()


car1 = Car("Toyota", "Camry")
car1.move()