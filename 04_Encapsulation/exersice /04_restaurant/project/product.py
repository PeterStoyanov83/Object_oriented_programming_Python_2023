class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
