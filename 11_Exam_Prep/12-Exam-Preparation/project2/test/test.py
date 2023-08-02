from project2.movie import Movie

import unittest


class TestMovie(unittest.TestCase):
    def test_initialization(self):
        movie = Movie("Inception", 2010, 8.8)
        self.assertEqual(movie.name, "Inception")
        self.assertEqual(movie.year, 2010)
        self.assertEqual(movie.rating, 8.8)
        self.assertEqual(movie.actors, [])

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Movie("", 2010, 8.8)

    def test_invalid_year(self):
        with self.assertRaises(ValueError):
            Movie("Inception", 1800, 8.8)

    def test_add_actor(self):
        movie = Movie("Inception", 2010, 8.8)
        movie.add_actor("Leonardo DiCaprio")
        self.assertEqual(movie.actors, ["Leonardo DiCaprio"])

    def test_add_existing_actor(self):
        movie = Movie("Inception", 2010, 8.8)
        movie.add_actor("Leonardo DiCaprio")
        response = movie.add_actor("Leonardo DiCaprio")
        self.assertEqual(response, "Leonardo DiCaprio is already added in the list of actors!")
        self.assertEqual(movie.actors, ["Leonardo DiCaprio"])

    def test_comparison(self):
        movie1 = Movie("Inception", 2010, 8.8)
        movie2 = Movie("Titanic", 1997, 7.8)
        self.assertEqual(movie1 > movie2, '"Inception" is better than "Titanic"')
        self.assertEqual(movie2 > movie1, '"Inception" is better than "Titanic"')

    def test_repr(self):
        movie = Movie("Inception", 2010, 8.8)
        movie.add_actor("Leonardo DiCaprio")
        self.assertEqual(str(movie), "Name: Inception"
                                     "\nYear of Release: 2010"
                                     "\nRating: 8.80"
                                     "\nCast: Leonardo DiCaprio")


if __name__ == '__main__':
    unittest.main()
