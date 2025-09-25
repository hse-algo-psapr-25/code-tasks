import unittest

from data_structures.lists.linked_list.linked_list import LinkedList
from tests.data_structures.lists.test_baselist import TestBaseList


@unittest.skipIf(LinkedList().size is None, "LinkedList is not implemented")
class TestLinkedList(unittest.TestCase, TestBaseList):
    """Набор тестов для класса LinkedList."""

    def create_list(self):
        """Вернёт LinkedList"""
        return LinkedList()


if __name__ == "__main__":
    unittest.main()
