# Assignment 1: Superhero Class

class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        print(f"I am {self.name}, my power is {self.power}, and I come from {self.origin}.")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

# Subclass for flying heroes
class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flight_speed} km/h using {self.power}!")

# Subclass for tech-based heroes
class TechHero(Superhero):
    def __init__(self, name, power, origin, gadget):
        super().__init__(name, power, origin)
        self.gadget = gadget

    def use_power(self):
        print(f"{self.name} deploys {self.gadget} to enhance {self.power}!")

# Example usage
hero1 = FlyingHero("SkyBlade", "Wind Slash", "Cloud City", 500)
hero2 = TechHero("Circuit", "Cyber Blast", "Silicon Valley", "Nano Suit")

hero1.introduce()
hero1.use_power()

hero2.introduce()
hero2.use_power()

# Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()