from unittest import TestLoader, TestSuite, TextTestRunner

from tests.data_structures.lists.test_doubly_linked_list import TestDoublyLinkedList
from tests.data_structures.lists.test_linkedlist import TestLinkedList
from tests.problems.coins_change_problem.test_coins_change import TestCoinChange
from tests.problems.knapsack_problem.test_brute_force import TestBruteForceSolver
from tests.problems.sorting_problem.test_merge_sort import TestMergeSort
from tests.problems.sorting_problem.test_quick_sort import TestQuickSort


def suite():
    """Создает набор тест-кейсов для тестирования."""
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestLinkedList))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestDoublyLinkedList))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestBruteForceSolver))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestQuickSort))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestCoinChange))
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestMergeSort))

    return test_suite


if __name__ == "__main__":
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
