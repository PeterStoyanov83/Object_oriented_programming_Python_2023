from hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self, caffeine: float):
        super().__init__("Coffee", Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    def get_caffeine(self):
        return self.__caffeine
