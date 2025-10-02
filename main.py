from typing import List


def calculate_determinant(matrix: List[List[int]]) -> int:
    """Публичная функция: валидирует вход и один раз запускает расчёт."""
    _validate_square_int_matrix(matrix)
    return _determinant(matrix)


def _validate_square_int_matrix(matrix: List[List[int]]) -> None:
    if matrix is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Ожидалась непустая квадратная матрица из целых чисел")

    order = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != order:
            raise Exception("Матрица должна быть квадратной")
        for x in row:
            if not isinstance(x, int):
                raise Exception("Матрица должна содержать только целые числа")


def _determinant(matrix: List[List[int]]) -> int:
    """Внутренняя рекурсивная функция без валидации."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    det = 0

    first_row = matrix[0]
    for j, a in enumerate(first_row):
        if a == 0:
            continue
        sub = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += a * ((-1) ** j) * _determinant(sub)
    return det


def main():
    matrix = [
        [3, 7, -5, 1, 19, 5, 0, -2, 4, 10],
        [-2, 2, 4, -6, 1, 0, 3, 5, 7, 1],
        [5, -5, -7, 5, 8, 9, -1, 0, 2, 2],
        [-4, 3, 5, -6, 17, -1, 9, 0, 2, 3],
        [3, -3, -5, 8, -9, -1, 0, 2, 4, 7],
        [-3, 2, 4, -6, 1, 0, 3, 5, 7, 11],
        [2, -5, -7, 7, 8, 9, -1, 0, -2, 5],
        [-4, 3, 15, -6, 7, -1, 9, 1, 2, 13],
        [3, -3, -5, 8, 9, -1, 0, 2, 4, 17],
        [-13, 2, 4, -6, 1, 0, -3, 5, 7, 1],
    ]
    print("Матрица")
    for row in matrix:
        print(row)
    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
