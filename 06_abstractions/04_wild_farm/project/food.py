from abc import ABC


class Food(ABC):
    def __init__(self, quantity) -> None:
        self.quantity = quantity


class Vegetable(Food):
    ...


class Fruit(Food):
    ...


class Meat(Food):
    ...


class Seed(Food):
    ...
