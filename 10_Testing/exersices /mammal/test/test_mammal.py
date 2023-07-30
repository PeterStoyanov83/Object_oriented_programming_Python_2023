from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal(
            "some name",
            "some type",
            "some sound"
        )

    def test_correct_initializing(self):
        self.assertEqual("some name", self.mammal.name)
        self.assertEqual("some type", self.mammal.type)
        self.assertEqual("some sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_animal_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("some name makes some sound", result)

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("some name is of type some type", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

if __name__ == "__main__":
    main()
