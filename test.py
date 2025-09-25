import unittest

from main import generate_strings
from strings_checker import check_strings


class TestChecker(unittest.TestCase):
    """Тесты для функции, проверяющей генерацию строк из 0 и 1"""

    def test_with_generator(self):
        """Проверка списка строк, которые возвращает функция генератор"""

        for length in range(10):
            self.assertTrue(check_strings(generate_strings(length), length))

    def test_empty(self):
        """Проверка пустого списка строк"""
        target_string_length = 0
        strings_to_check = []
        self.assertTrue(check_strings(strings_to_check, target_string_length))

    def test_min_correct(self):
        """Проверка минимального корректного списка"""
        target_string_length = 1
        strings_to_check = ["0", "1"]
        self.assertTrue(check_strings(strings_to_check, target_string_length))

    def test_min_incorrect(self):
        """Проверка минимального некорректного списка"""
        target_string_length = 1
        strings_to_check = ["0"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_with_double_zero(self):
        """Проверка списка со строкой, содержащей '00'"""
        n = 3
        strings = generate_strings(n)
        strings[0] = "1001"
        self.assertFalse(check_strings(strings, n))

    def test_with_invalid_symbol(self):
        """Проверка списка со строкой с недопустимым символом"""
        n = 3
        strings = generate_strings(n)
        strings[0] = "1a1"
        self.assertFalse(check_strings(strings, n))

    def test_large_n(self):
        """Проверка корректного набора для n большого"""
        n = 15
        strings = generate_strings(n)
        self.assertTrue(check_strings(strings, n))

    def test_negative_length(self):
        """Отрицательная длина должна вернуть False"""
        strings = ["0", "1"]
        self.assertFalse(check_strings(strings, -1))

    def test_non_string_elements(self):
        """Проверка списка, содержащего не строки"""
        n = 2
        strings = ["01", "10"]
        self.assertFalse(check_strings(strings, n))

    def test_wrong_length_strings(self):
        """Проверка: в списке строка неправильной длины"""
        strings_to_check = ["01", "1", "11"]
        self.assertFalse(check_strings(strings_to_check, 2))


if __name__ == "__main__":
    unittest.main()
