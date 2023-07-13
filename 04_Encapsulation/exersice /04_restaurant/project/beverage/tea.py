from project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50

    def __init__(self):
        super().__init__("Tea", Tea.PRICE, Tea.MILLILITERS)
