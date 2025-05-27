#Method overriding 
class Vehicle:
    def drive(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def drive(self):
        print("Car is driving on the road")

class Boat(Vehicle):
    def drive(self):
        print("Boat is sailing on water")

# Usage
vehicle = Vehicle()
car = Car()
boat = Boat()

vehicle.drive()  # Vehicle is moving
car.drive()      # Car is driving on the road
boat.drive()     # Boat is sailing on water