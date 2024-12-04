# Parent Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life  

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def battery_status(self):
        return f"{self.brand} {self.model} has {self.battery_life} hours of battery left."

    def __str__(self):
        return f"{self.brand} {self.model} | Price: ${self.price}"

# Subclass: SmartphoneWithStylus
class SmartphoneWithStylus(Smartphone):
    def __init__(self, brand, model, price, battery_life, stylus_type):
        super().__init__(brand, model, price, battery_life)
        self.stylus_type = stylus_type

    def use_stylus(self):
        return f"Using the {self.stylus_type} stylus with {self.brand} {self.model}."

    # Overriding the battery_status method
    def battery_status(self):
        return f"{self.brand} {self.model} (with stylus) has {self.battery_life} hours of battery left."

# Creating Objects
basic_phone = Smartphone("Nokia", "3310", 49.99, 48)
stylus_phone = SmartphoneWithStylus("Samsung", "Galaxy Note 20", 999.99, 24, "S Pen")

# Interacting with the objects
print(basic_phone)  
print(basic_phone.call("123-456-7890"))  
print(basic_phone.battery_status())  

print(stylus_phone)  
print(stylus_phone.use_stylus())  
print(stylus_phone.battery_status())  


# Assignment/Activity 2

# Base class: Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing 🚤"

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚴"

# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    print(f"{vehicle.__class__.__name__}: {vehicle.move()}")

# Creating objects of different vehicle types
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

# Demonstrating polymorphism
vehicles = [car, plane, boat, bicycle]
for v in vehicles:
    demonstrate_movement(v)