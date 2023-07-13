from functools import reduce


class Calculator:
    # noinspection PyUnreachableCode

    @staticmethod
    def add(*args):
        return reduce(lambda x, y: x + y, args)

        """Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, 
        so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) 
        calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the 
        calculation, and serves as a default when the iterable is empty."""

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x - y, args)

    @staticmethod
    def multiply(*args):
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x / y, args)
