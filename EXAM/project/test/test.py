import unittest
from project.second_hand_car import SecondHandCar

class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.car = SecondHandCar('Toyota', 'Sedan', 150000, 5000.0)

    def test_init_with_edge_values(self):
        car = SecondHandCar('Toyota', 'Sedan', 101, 1.01)
        self.assertEqual(car.mileage, 101)
        self.assertEqual(car.price, 1.01)

    def test_init_with_invalid_values(self):
        with self.assertRaises(ValueError):
            SecondHandCar('Toyota', 'Sedan', 100, 5000.0)
        with self.assertRaises(ValueError):
            SecondHandCar('Toyota', 'Sedan', 150000, 1.0)
    def test_price_setter(self):
        with self.assertRaises(ValueError):
            self.car.price = 0.5
        with self.assertRaises(ValueError):
            self.car.price = 1.0

    def test_mileage_setter(self):
        with self.assertRaises(ValueError):
            self.car.mileage = 50
        with self.assertRaises(ValueError):
            self.car.mileage = 100

    def test_set_promotional_price(self):
        with self.assertRaises(ValueError):
            self.car.set_promotional_price(6000.0)

        self.assertEqual(self.car.set_promotional_price(4000.0), 'The promotional price has been successfully set.')
        self.assertEqual(self.car.price, 4000.0)

    def test_need_repair(self):
        self.assertEqual(self.car.need_repair(3000.0, 'Engine Repair'), 'Repair is impossible!')
        self.assertEqual(self.car.need_repair(1000.0, 'Engine Repair'), 'Price has been increased due to repair charges.')
        self.assertEqual(self.car.price, 6000.0)  # Price should increase by repair price
        self.assertEqual(len(self.car.repairs), 1)

    def test_gt(self):
        car2 = SecondHandCar('Honda', 'SUV', 200000, 6000.0)
        self.assertEqual(self.car > car2, 'Cars cannot be compared. Type mismatch!')

        car3 = SecondHandCar('Honda', 'Sedan', 200000, 6000.0)
        self.assertTrue(car3 > self.car)

    def test_str(self):
        expected_output = "Model Toyota | Type Sedan | Milage 150000km\nCurrent price: 5000.00 | Number of Repairs: 0"
        self.assertEqual(str(self.car), expected_output)


if __name__ == '__main__':
    unittest.main()
