import unittest

from problems.sorting_problem.quick_sort import quick_sort
from tests.problems.sorting_problem.test_abstract import TestAbstractSorter


class TestQuickSort(unittest.TestCase, TestAbstractSorter):
    """Набор тестов для проверки некоторого метода сортировки."""

    sort_method = lambda _, items: quick_sort(items)


if __name__ == "__main__":
    unittest.main()
