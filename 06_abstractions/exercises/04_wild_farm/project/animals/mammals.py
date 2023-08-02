from a.project import Mammal
from a.project import Vegetable, Fruit, Meat


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self) -> str:
        return "Squeak"

    def feed(self, food) -> str:
        if isinstance(food, (Vegetable, Fruit)):
            self.weight += 0.10 * food.quantity
            self.food_eaten += food.quantity
        return f"Mouse does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
        return f"Mouse [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self) -> str:
        return "Woof!"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += 0.40 * food.quantity
            self.food_eaten += food.quantity
        return f"Dog does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
        return f"Dog [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self) -> str:
        return "Meow"

    def feed(self, food) -> str:
        if isinstance(food, (Vegetable, Meat)):
            self.weight += 0.30 * food.quantity
            self.food_eaten += food.quantity

        return f"Cat does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
        return f"Cat [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight, living_region)

    def make_sound(self) -> str:
        return "ROAR!!!"

    def feed(self, food) -> str:
        if isinstance(food, Meat):
            self.weight += 1.00 * food.quantity
            self.food_eaten += food.quantity
        return f"Tiger does not eat {food.__class__.__name__}!"

    def __repr__(self) -> str:
        return f"Tiger [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
