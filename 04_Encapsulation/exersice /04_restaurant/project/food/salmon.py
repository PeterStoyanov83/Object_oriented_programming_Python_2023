from project.food.main_dish import MainDish


class Salmon(MainDish):
    GRAMS = 22

    def __init__(self):
        super().__init__("Salmon", 0, Salmon.GRAMS)
