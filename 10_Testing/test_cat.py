class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_cat_constructor(self):
        # arrange
        cat = Cat("Bobby")

        # assert
        self.assertEqual("Bobby", cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_cat_size_increased_after_eating(self):
        cat = Cat("Bobby")

        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_if_cat_fed_after_eating(self):
        cat = Cat("Bobby")
        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_if_cat_fed_2_raises_error(self):
        cat = Cat("Bobby")

        # First feed the cat
        cat.eat()

        # Then try to feed the cat again and expect an error
        with self.assertRaises(Exception) as ex:
            cat.eat()

        # Check the exception message
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cannot_sleep_if_not_fed(self):
        cat = Cat("Bobby")

        with self.assertRaises(Exception) as ex:
            cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_if_cat_not_sleepy_after_sleeping(self):
        # Arrange: Create a cat and feed it, so it can sleep
        cat = Cat("Bobby")

        cat.eat()  # The cat needs to be fed before it can sleep

        # Act:
        cat.sleep()

        # Assert:
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
