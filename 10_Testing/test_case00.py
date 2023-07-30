import unittest


def sum_num(a, b):
    return a + b


class TestSumNums(unittest.TestCase):
    def test_sum_nums(self):
        result = sum_num(5, 6)
        expected_result = 11
        self.assertEquals(result, expected_result)


if __name__ == '__main__':
    unittest.main()
