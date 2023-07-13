from dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self):
        super().__init__("Cake", Cake.PRICE, Cake.GRAMS, Cake.CALORIES)