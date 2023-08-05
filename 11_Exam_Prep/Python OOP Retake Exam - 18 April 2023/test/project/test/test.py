from project import Robot

import unittest


class TestRobot(unittest.TestCase):

    def setUp(self):
        self.robot = Robot('R1', 'Military', 100, 5000)

    def test_init(self):
        self.assertEqual(self.robot.robot_id, 'R1')
        self.assertEqual(self.robot.category, 'Military')
        self.assertEqual(self.robot.available_capacity, 100)
        self.assertEqual(self.robot.price, 5000)

    def test_category(self):
        with self.assertRaises(ValueError):
            self.robot.category = 'Invalid'
        self.robot.category = 'Education'
        self.assertEqual(self.robot.category, 'Education')

    def test_price(self):
        with self.assertRaises(ValueError):
            self.robot.price = -10
        self.robot.price = 7000
        self.assertEqual(self.robot.price, 7000)

    def test_upgrade(self):
        result = self.robot.upgrade('new_component', 500)
        self.assertEqual(result, 'Robot R1 was upgraded with new_component.')
        self.assertEqual(self.robot.price, 5750)  # 5000 + 500 * 1.5

        # Trying to upgrade with the same component
        result = self.robot.upgrade('new_component', 500)
        self.assertEqual(result, 'Robot R1 was not upgraded.')

    def test_update(self):
        result = self.robot.update(2.0, 50)
        self.assertEqual(result, 'Robot R1 was updated to version 2.0.')
        self.assertEqual(self.robot.available_capacity, 50)  # 100 - 50

        # Trying to update with a lower version
        result = self.robot.update(1.5, 50)
        self.assertEqual(result, 'Robot R1 was not updated.')

    def test_comparison(self):
        robot2 = Robot('R2', 'Entertainment', 150, 4000)
        result = self.robot > robot2
        self.assertEqual(result, 'Robot with ID R1 is more expensive than Robot with ID R2.')

if __name__ == '__main__':
    unittest.main()
