from typing import List
import unittest

def fio(initials: List[str]) -> str:
    # Напишите ваш код здесь
    a=initials[0]
    b=initials[1]
    c=initials[2]
    d=(a[0]+b[0]+c[0])
    return d

class TestFio(unittest.TestCase):

    def test_fio_with_three_initials(self):
        self.assertEqual(fio(['John', 'Doe', 'Smith']), 'JDS')

    def test_fio_with_lowercase(self):
        self.assertEqual(fio(['jane', 'doe', 'smith']), 'jds')

    def test_fio_with_mixed_cases(self):
        self.assertEqual(fio(['JaNe', 'DoE', 'SmItH']), 'JDS')

    def test_fio_with_special_characters(self):
        self.assertEqual(fio(['@#$%', '^&*(', '!+_-']), '@^!')

# Запуск всех тестов
if __name__ == '__main__':
    unittest.main()
