class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = ""
print(car)

from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("make", "model", 10, 100)

    def test_car_init(self):
        self.assertEqual(self.car.make, "make")
        self.assertEqual(self.car.model, "model")
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_car_make_setter(self):
        with self.assertRaises(Exception):
            self.car.make = ""

    def test_car_model_setter(self):
        with self.assertRaises(Exception):
            self.car.model = ""

    def test_car_fuel_consumption_setter(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_car_fuel_capacity_setter(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1

    def test_car_fuel_amount_setter(self):
        with self.assertRaises(Exception):
            self.car.fuel_amount = -1

    def test_car_refuel_negative(self):
        """Test the refuel method with negative amount"""
        with self.assertRaises(Exception):
            self.car.refuel(-50)

    def test_car_refuel(self):
        self.car.refuel(50)
        self.assertEqual(self.car.fuel_amount, 50)

    def test_car_refuel_over_capacity(self):
        self.car.refuel(200)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_car_drive(self):
        self.car.refuel(100)
        self.car.drive(200)
        self.assertEqual(self.car.fuel_amount, 80)

    def test_car_drive_not_enough_fuel(self):
        with self.assertRaises(Exception):
            self.car.drive(200)


if __name__ == '__main__':
    main()
