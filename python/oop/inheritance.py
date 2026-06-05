"""
THE FOUR PILLARS OF OOP
Pillar 2: Inheritance (Parent → Child)


Dependencies:
- Python 3.8+
- No external packages
"""

# Parent class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        """Generic animal sound"""
        return "Some sound"

    def describe(self):
        return f"{self.name} is {self.age} years old"


class Dog(Animal):
    def __init__(self, name, age, breed):
        # Call parent constructor
        super().__init__(name, age)
        self.breed = breed

    # Override parent method
    def sound(self):
        return "Woof! 🐕"

    # New method specific to dogs
    def wag_tail(self):
        return f"{self.name} wags tail happily!"


# Another child class
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def sound(self):
        return "Meow! 🐈"

    def purr(self):
        return f"{self.name} purrs softly"



if __name__ == "__main__":

    # Using inheritance
    animals = [
        Dog("Rex", 3, "German Shepherd"),
        Cat("Whiskers", 5, "Orange"),
        Dog("Buddy", 2, "Golden Retriever")
    ]

    for animal in animals:
        print(f"\n{animal.describe()}")
        print(f" Says: {animal.sound()}")

        # Check type for specific method
        if isinstance(animal, Dog):
            print(f" {animal.wag_tail()}")
        elif isinstance(animal, Cat):
            print(f" {animal.purr()}")