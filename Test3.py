import unittest

def longest_film(film_1: str, film_2: str,film_3: str) -> bool:
    f1=len(film_1)
    f2=len(film_2)
    f3=len(film_3)
    if f1>f2 and f1>f3:
      result = (film_1)
    elif f2>f1 and f2>f3:
      result = (film_2)
    elif f1==f2 or f2==f3 or f1==f3:
        result = (film_1)
    else:
      result = (film_3)
    return result

class TestLongestFilm(unittest.TestCase):

    def test_first_film_longest(self):
        self.assertEqual(longest_film('Film1', 'Film2', 'Film3'), 'Film3')

    def test_second_film_longest(self):
        self.assertEqual(longest_film('Film1', 'Film22', 'Film3'), 'Film22')

    def test_third_film_longest(self):
        self.assertEqual(longest_film('Film1', 'Film2', 'Film333'), 'Film333')

    def test_two_films_same_length(self):
        self.assertEqual(longest_film('Film1', 'Film2', 'Film2'), 'Film1')

    def test_all_films_same_length(self):
        self.assertEqual(longest_film('Film111', 'Film111', 'Film111'), 'Film111')

if __name__ == '__main__':
    unittest.main()
