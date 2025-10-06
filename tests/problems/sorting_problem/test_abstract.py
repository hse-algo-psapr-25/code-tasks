from abc import ABC

from problems.sorting_problem.errors.error_message_template_enum import (
    ErrorMessageTemplateEnum,
)


class TestAbstractSorter(ABC):
    """Класс для тестирования сортировки"""

    sort_method = None

    def test_empty_list(self):
        """Проверяет сортировку пустого списка"""
        self.assertEqual(self.sort_method([]), [])

    def test_single_element_list(self):
        """Проверяет сортировку списка с одним элементом"""
        self.assertEqual(self.sort_method([8]), [8])

    def test_identical_elements_list(self):
        """Проверяет сортировку списка с одинаковыми элементами"""
        items = [5, 5, 5, 5, 5, 5]
        self.assertEqual(self.sort_method(items), [5, 5, 5, 5, 5, 5])

    def test_repeated_elements_list(self):
        """Проверяет сортировку списка с повторяющимися элементами"""
        items = [9, 12, 4, -3, -5, 7, -5, 6, 6, 1, -10, -5]
        self.assertEqual(
            self.sort_method(items), [-10, -5, -5, -5, -3, 1, 4, 6, 6, 7, 9, 12]
        )

    def test_unique_elements_list(self):
        """Проверяет сортировку списка с уникальными элементами"""
        items = [5, 4, -2, 8, 0, -3, -5, 10, 1, -4, 7, -1, 6, 9, 2, 3]
        self.assertEqual(
            self.sort_method(items),
            [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )

    def test_mixed_int_float_list(self):
        """Проверяет сортировку списка с вещественными и целыми числами"""
        items = [3, 9, 1.4, -2.7, 10.23, 7.77]
        self.assertEqual(self.sort_method(items), [-2.7, 1.4, 3, 7.77, 9, 10.23])

    def test_string_list(self):
        """Проверяет сортировку списка строк"""
        items = ["кот", "котенок", "ab", "котик", "a", "aa"]
        self.assertEqual(
            self.sort_method(items), ["a", "aa", "ab", "кот", "котенок", "котик"]
        )

    def test_ascending_sorted_list(self):
        """Проверяет сортировку отсортированного по возрастанию списка"""
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(self.sort_method(items), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_descending_sorted_list(self):
        """Проверяет сортировку отсортированного по убыванию списка"""
        items = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.assertEqual(self.sort_method(items), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_user_objects_list(self):
        """Проверяет сортировку пользовательских объектов"""

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __eq__(self, other):
                return self.x == other.x and self.y == other.y

            def __lt__(self, other):
                return self.x < other.x

            def __gt__(self, other):
                return self.x > other.x

            def __le__(self, other):
                return self.x <= other.x

            def __ge__(self, other):
                return self.x >= other.x

            def __repr__(self):
                return f"Point({self.x}, {self.y})"

        items = [Point(2, 3), Point(7, 7), Point(4, 4), Point(10, 6)]
        self.assertEqual(
            self.sort_method(items),
            [Point(2, 3), Point(4, 4), Point(7, 7), Point(10, 6)],
        )

    def test_incomparable_embedded_types(self):
        """Проверяет выброс исключения при попытке сравнения несравнимых типов"""
        with self.assertRaises(TypeError) as err:
            self.sort_method([1, "a"])
        self.assertEqual(
            ErrorMessageTemplateEnum.ERR_INCOMPARABLE_EMBEDDED_TYPES.format(
                "str", "int"
            ),
            str(err.exception),
        )

    def test_incomparable_user_types(self):
        """Проверяет выброс исключение при попытке сравнения несравнимых пользовательских объектов"""

        class Point:
            def __init__(self, x, y):
                self.x = x
                self.y = y

        with self.assertRaises(TypeError) as err:
            self.sort_method([Point(1, 1), Point(7, 7)])
        self.assertEqual(
            ErrorMessageTemplateEnum.ERR_INCOMPARABLE_EMBEDDED_TYPES.format(
                "Point", "Point"
            ),
            str(err.exception),
        )
