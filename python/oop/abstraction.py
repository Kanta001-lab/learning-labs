"""
PART 3: THE FOUR PILLARS OF OOP
Pillar 4: Abstraction (Hide complexity)   


Dependencies:
- Python 3.8+
- ABC, abstractmethod(standard library - no install needed)

"""

# Constants
SEPARATOR = "=" * 50
CURRENCY = "₦"


from abc import ABC, abstractmethod

class KitchenAppliance(ABC):
    """Abstract Base Class - blueprint for all appliances"""

    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        self.is_on = False


    def turn_on(self):
        """Concrete method - same for all"""
        if not self.is_on:
            self.is_on = True
            print(f"🔌 {self.brand} appliance turned on")


    def turn_off(self):
        """Concrete method - same for all"""
        if self.is_on:
            self.is_on = False
            print(f"🔌 {self.brand} appliance is turned off")

    @abstractmethod
    def operate(self):
        """Abstract method - MUST be implemented by children"""
        pass

    @abstractmethod
    def clean(self):
        """Abstract method - MUST be implemented by children"""
        pass


class Oven(KitchenAppliance):
    def __init__(self, brand, power, temperature):
        super().__init__(brand, power)
        self.temperature = temperature
        self.current_temp = 0


    def operate(self):
        """Must implement this!"""
        if self.is_on:
            print(f"🔥 {self.brand} oven heating to {self.temperature}°F")
            self.current_temp = self.temperature
        else:
            print("❌ Turn on the oven first!")

    def clean(self):
        """Must implement this!"""
        print(f"🧹 Running self-cleaning cycle on {self.brand} oven")

    def bake(self, food):
        """Oven-specific method"""
        if self.current_temp > 0:
            print(f"🍕 Baking {food} at {self.current_temp}°F")
        else:
            print("❌ Oven not preheated")

class Blender(KitchenAppliance):
    def __init__(self, brand, power, speed_levels):
        super().__init__(brand, power)
        self.speed_levels = speed_levels
        self.current_speed = 0


    def operate(self):
        """Must implement this!"""
        if self.is_on:
            print(f"🌀 {self.brand} blender running at speed {self.current_speed}")
            self.current_speed = self.speed_levels
        else:
            print("❌ Turn on the blender first!")

    def clean(self):
        """Must implement this"""
        print(f"🧽 Running quick-clean cycle on {self.brand}")

    def blend(self, ingredients):
        """Blender-specific method"""
        if self.is_on:
            print(f"🥤 Blending {ingredients}.... VRRRR!")
        else:
            print("❌ Turn on the blender first!")


if __name__ == "__main__":
    # Use our Appliance
    print(SEPARATOR)
    print("🔧 KITCHEN APPLIANCE SIMULATOR")
    print(SEPARATOR)

    oven = Oven("GE", 3000, 350)
    blender = Blender("Ninja", 1200, 10)


    # Oven operations
    oven.turn_on()
    oven.operate()
    oven.bake("Pizza")
    oven.clean()
    oven.turn_off()

    print()

    # Blender operations
    blender.turn_on()
    blender.operate()
    blender.blend("fruits and ice")
    blender.clean()
    blender.turn_off()