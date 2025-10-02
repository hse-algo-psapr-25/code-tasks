# main.py

from typing import List


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы
    методом разложения по строке (Лаплас).

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    # валидация
    if matrix is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Something went wrong")

    order = len(matrix)
    for row in matrix:
        if not isinstance(row, list) or len(row) != order:
            raise Exception("Something went wrong")
        for x in row:
            if not isinstance(x, int):
                raise Exception("Something went wrong")

    # базовый случай
    if order == 1:
        return matrix[0][0]

    # разложение по первой строке
    det = 0
    for idx, item in enumerate(matrix[0]):
        if item == 0:
            continue
        det += item * ((-1) ** idx) * _get_minor(0, idx, matrix)

    return det


def _get_minor(idx_row: int, idx_col: int, matrix: List[List[int]]) -> int:
    """Возвращает детерминант минора (матрицы без строки idx_row и столбца idx_col)"""
    # формируем подматрицу (минор)
    sub = []
    for r, row in enumerate(matrix):
        if r == idx_row:
            continue
        sub_row = row[:idx_col] + row[idx_col + 1 :]
        sub.append(sub_row)

    # рекурсивно считаем детерминант минора тем же методом
    return calculate_determinant(sub)


def main():
    matrix = [
        [3, 7, -5],
        [-2, 2, 4],
        [5, -5, -7],
    ]
    print("Матрица")
    for row in matrix:
        print(row)
    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
