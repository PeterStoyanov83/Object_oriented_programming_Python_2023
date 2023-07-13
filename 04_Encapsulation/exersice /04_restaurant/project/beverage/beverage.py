from project.product import Product


class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)
        self.__milliliters = milliliters

    def get_milliliters(self):
        return self.__milliliters
