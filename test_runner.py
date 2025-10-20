from unittest import TestLoader, TestSuite, TextTestRunner

from tests.generators.test_permutation_generator import TestPermutationGenerator


def suite():
    """Создает набор тест-кейсов для тестирования."""
    test_suite = TestSuite()
    test_suite.addTest(TestLoader().loadTestsFromTestCase(TestPermutationGenerator))

    return test_suite


if __name__ == "__main__":
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
