from project.product import Product


class Food(Product):
    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price)
        self.__grams = grams

    def get_grams(self):
        return self.__grams
