from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self) -> None:
        ...

    @abstractmethod
    def feed(self) -> None:
        ...


class Bird(Animal):
    def __init__(self, name, weight, wing_size) -> None:
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal):
    def __init__(self, name, weight, living_region) -> None:
        super().__init__(name, weight)
        self.living_region = living_region
