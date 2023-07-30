class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)

import unittest


class TestIntegerList(unittest.TestCase):

    def setUp(self):
        """This function is called before every test case"""
        self.integer_list = IntegerList(1, 2, 3)

    def test_constructor(self):
        """Test the constructor"""
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3])

    def test_add(self):
        """Test the add method"""
        self.integer_list.add(4)
        self.assertEqual(self.integer_list.get_data(), [1, 2, 3, 4])

    def test_add_non_integer(self):
        """Test the add method with non-integer"""
        with self.assertRaises(ValueError):
            self.integer_list.add("five")

    def test_remove_index(self):
        """Test the remove_index method"""
        self.assertEqual(self.integer_list.remove_index(1), 2)
        self.assertEqual(self.integer_list.get_data(), [1, 3])

    def test_remove_index_out_of_range(self):
        """Test the remove_index method with out of range index"""
        with self.assertRaises(IndexError):
            self.integer_list.remove_index(5)

    def test_get(self):
        """Test the get method"""
        self.assertEqual(self.integer_list.get(2), 3)

    def test_get_out_of_range(self):
        """Test the get method with out of range index"""
        with self.assertRaises(IndexError):
            self.integer_list.get(5)

    def test_insert(self):
        """Test the insert method"""
        self.integer_list.insert(1, 4)
        self.assertEqual(self.integer_list.get_data(), [1, 4, 2, 3])

    def test_insert_out_of_range(self):
        """Test the insert method with out of range index"""
        with self.assertRaises(IndexError):
            self.integer_list.insert(5, 4)

    def test_insert_non_integer(self):
        """Test the insert method with non-integer"""
        with self.assertRaises(ValueError):
            self.integer_list.insert(1, "five")

    def test_get_biggest(self):
        """Test the get_biggest method"""
        self.assertEqual(self.integer_list.get_biggest(), 3)

    def test_get_index(self):
        """Test the get_index method"""
        self.assertEqual(self.integer_list.get_index(3), 2)


if __name__ == '__main__':
    unittest.main()