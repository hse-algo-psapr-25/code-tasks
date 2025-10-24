import unittest

from main import Bounds, find_bounds


class TestFindBounds(unittest.TestCase):
    def test_basic_examples(self):
        # Примеры из описания (логика: last index < key, first index > key)
        self.assertEqual(find_bounds([1, 2, 3, 3, 4], 2), Bounds(0, 2))
        self.assertEqual(find_bounds([1, 2, 3, 3, 4], 7), Bounds(4, 5))
        self.assertEqual(find_bounds([1, 2, 3, 3, 4], 0), Bounds(-1, 0))

    def test_singleton_and_empty(self):
        self.assertEqual(find_bounds([1], 2), Bounds(0, 1))
        self.assertEqual(find_bounds([], 2), Bounds(-1, 0))

    def test_duplicates(self):
        self.assertEqual(find_bounds([1, 1, 1, 1], 1), Bounds(-1, 4))
        self.assertEqual(find_bounds([1, 1, 2, 2, 3], 2), Bounds(1, 4))

    def test_invalid_inputs(self):
        # Нечто, что не список — функция возвращает None
        self.assertIsNone(find_bounds(None, None))
        self.assertIsNone(find_bounds("not a list", 1))

    def test_not_comparable(self):
        # Список с несравнимыми типами — ожидаем None (TypeError внутри)
        self.assertIsNone(find_bounds([1, "a"], 2))

    def test_strings(self):
        self.assertEqual(find_bounds(["a", "b", "b", "c"], "b"), Bounds(0, 3))
        self.assertEqual(find_bounds(["аб", "аб", "б"], "аб"), Bounds(-1, 2))

    def test_tuples(self):
        data = [(1, "a"), (1, "b"), (2, "a")]
        self.assertEqual(find_bounds(data, (1, "b")), Bounds(0, 2))

    def test_int_and_float(self):
        self.assertEqual(find_bounds([1, 2.0, 3], 2), Bounds(0, 2))

    def test_input_unchanged(self):
        data = [1, 2, 2, 3]
        copy = list(data)
        find_bounds(data, 2)
        self.assertEqual(data, copy)

    def test_type_mismatch_returns_none(self):
        self.assertIsNone(find_bounds(["a", "b"], 1))


if __name__ == "__main__":
    unittest.main()
