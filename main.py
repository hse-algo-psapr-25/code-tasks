from typing import List


def validate_matrix(matrix: List[List[int]]):
    """
    Валидирует матрицу
    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    """
    if matrix is None:
        raise ValueError("Matrix can't be None")
    if not isinstance(matrix, list):
        raise ValueError("Matrix should be list")
    if matrix == []:
        raise ValueError("Mattrix can't be empty")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Matrix should be square")
    if not all(isinstance(item, int) for row in matrix for item in row):
        raise ValueError("All matrix items must be integers")


def get_matrix_order_lower(matrix: List[List[int]], i: int, j: int):
    """
    Понижает порядок матрицы, удаляя из нее i-й строк и j-й столбец
    :params: i: индекс строки, которая удаляется
             j: индекс столбца, который удаляется
    :return: матрица пониженного порядка
    """
    return [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]


def _calcualte_determinant_recursive(matrix: List[List[int]], n) -> int:
    """
    Рекурсивно вычисляет определитель квадратной матрицы
    :param matrix: целочисленная квадратная матрица
    :return: значение определителя
    """
    if n == 1:
        return matrix[0][0]
    det = 0
    first_row = matrix[0]
    for j, item in enumerate(first_row):
        order_lower_matrix = get_matrix_order_lower(matrix, 0, j) 
        sign = (-1)  ** j
        det += item * sign * _calcualte_determinant_recursive(order_lower_matrix, n-1) 
    return det


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    try:
        validate_matrix(matrix)
        n = len(matrix)
        return _calcualte_determinant_recursive(matrix, n)
    except Exception as e:
        raise e

def main():
    matrix = [[3, -3, -5, 8], [-3, 2, 4, -6], [2, -5, -7, 5], [-4, 3, 5, -6]]
    print("Матрица")
    for row in matrix:
        print(row)
    
    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()