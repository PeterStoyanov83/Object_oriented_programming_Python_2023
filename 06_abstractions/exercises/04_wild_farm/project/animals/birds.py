from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += 0.25 * food.quantity
            self.food_eaten += food.quantity
        return f"Owl does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
        return f"Owl [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):
    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight, wing_size)

    def make_sound(self) -> str:
        return "Cluck"

    def feed(self, food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity

    def __repr__(self) -> str:
        return f"Hen [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"
