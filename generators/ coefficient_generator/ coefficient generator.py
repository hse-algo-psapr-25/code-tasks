import numpy as np
from typing import List, Tuple, Dict


def generate_lambda_pairs(l_min: int, l_max: int) -> List[Tuple[int, int]]:
    """Генерирует пары корней (lambda_1, lambda_2) характеристического уравнения, из заданного диапазона,
    исключая нулевые корни.

    Args:
        l_min (int): начала диапазона значений
        l_max (int): конец диапазона значений

    Returns:
        List[Tuple[int, int]]: Список кортежей пар лямбд
    """
    pairs = []
    for l1 in range(l_min, l_max + 1):
        for l2 in range(l_min, l_max + 1):
            if l1 != 0 and l2 != 0:
                pairs.append((l1, l2))

    return pairs


def calculate_abc_parameters(
    lambda_pairs: List[Tuple[int, int]],
) -> List[Tuple[int, int, int, int]]:
    """Вычисляет параметры a, b, c из корней lambda_1, lambda_2, по теореме Виета

    Args:
        lambda_pairs (List[Tuple[int, int]]): список пар значений корней характеристического уравнения

    Returns:
        List[Tuple[int, int, int, int]]: Список кортежей, со значениями a, bc, l1, l2
    """
    parameters = []
    for l1, l2 in lambda_pairs:
        a = l1 + l2
        bc = l1 * l2
        parameters.append((a, bc, l1, l2))

    return parameters


def generate_bc_factorizations(
    parameters: List[Tuple[int, int, int, int]], not_grate_than=15
) -> List[Tuple[int, int, int, int, int]]:
    """Генерирует все значение параметров b и c  для матрицы по отдельности

    Args:
        parameters (List[Tuple[int, int, int, int]]): Список кортежей параметров a, bc, l1, l2
        not_grate_than (int, optional): устанавливает порог для значений b и с, т.е. они не будет больше чем non_grate_than. Defaults to 15.

    Returns:
        List[Tuple[int, int, int, int, int]]: Список кортежей параметров и лямбд: a, b, c, l1, l2
    """
    all_parameters = []

    for a, bc, l1, l2 in parameters:
        divisors = []
        for i in range(1, abs(bc) + 1):
            if bc % i == 0:
                divisors.append(i)

        for b in divisors:
            c = bc // b
            if (
                abs(b) <= not_grate_than
                and abs(c) <= not_grate_than
                and b != 0
                and c != 0
            ):
                all_parameters.append((a, b, c, l1, l2))
                all_parameters.append((a, -b, -c, l1, l2))

    return all_parameters


def calculate_constants(
    all_parameters: List[Tuple[int, int, int, int, int]],
) -> List[Dict]:
    """Вычисляет значение констант для общего решения

    Args:
        all_parameters (List[Tuple[int, int, int, int, int]]): Список кортежей параметров и лямбд: a, b, c, l1, l2

    Returns:
        List[Dict]: Список словарей со всеми необходимыми параметрами
    """
    result = []

    for a, b, c, l1, l2 in all_parameters:
        det1 = a
        det2 = a**2 - b * c

        if l1 != l2:
            A = np.array([[l1, l2], [l1**2, l2**2]])
            B = np.array([det1, det2])
            try:
                C1, C2 = np.linalg.solve(A, B)
                if is_nice_fractions(C1) and is_nice_fractions(C2):
                    result.append(
                        {
                            "a": a,
                            "b": b,
                            "c": c,
                            "lambda_1": l1,
                            "lambda_2": l2,
                            "C1": float(C1),
                            "C2": float(C2),
                        }
                    )
            except np.linalg.LinAlgError:
                continue
        else:
            l = l1
            A = np.array([[l, l], [l**2, 2 * l**2]])
            B = np.array([det1, det2])
            try:
                C1, C2 = np.linalg.solve(A, B)
                if is_nice_fractions(C1) and is_nice_fractions(C2):
                    result.append(
                        {
                            "a": a,
                            "b": b,
                            "c": c,
                            "lambda_1": l1,
                            "lambda_2": l2,
                            "C1": float(C1),
                            "C2": float(C2),
                        }
                    )
            except np.linalg.LinAlgError:
                continue

    return result


def is_nice_fractions(rational_number: float, tol: float = 1e-10) -> bool:
    """Проверяет, является ли константа хорошей дробью

    Args:
        rational_number (float): число для проверки
        tol (float, optional): для проверки на одинаковость разности чисел с плавающей точкой. Defaults to 1e-10.

    Returns:
        bool: True, если число целое или если число хорошая дробь
              False, иначе
    """

    if abs(rational_number - round(rational_number)) < tol:
        return True

    for denominator in range(2, 7):
        for numerator in range(1, denominator):
            fraction = numerator / denominator
            if abs(rational_number - fraction) < tol:
                return True
            if abs(rational_number + fraction) < tol:
                return True
    return False


def main():
    lambda_pairs = generate_lambda_pairs(1, 5)
    abc_params = calculate_abc_parameters(lambda_pairs)
    all_params = generate_bc_factorizations(abc_params)
    results = calculate_constants(all_params)
    for result in results:
        print("--------")
        for key, val in result.items():
            print(f"{key}: {val}")


if __name__ == "__main__":
    main()
