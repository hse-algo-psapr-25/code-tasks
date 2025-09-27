from typing import List


def validate_matrix(matrix: List[List[int]]):
    if not isinstance(matrix, list):
        raise ValueError("Matrix should be list")
    if matrix is None:
        raise ValueError("Matrix can't be None")
    if matrix == []:
        raise ValueError("Mattrix can't be empty")
    if not all(len(row) == len(matrix) for row in matrix):
        raise ValueError("Matrix should be square")
    if not all(isinstance(item, int) for row in matrix for item in row):
        raise ValueError("All matrix items must be integers")


def get_minor(matrix: List[List[int]], i: int, j: int):
    """
    Get minor by i raw and j column
    params: i: index of raw
            j: index of column
    return: minor
    """
    return [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]


def _calcualte_determinant_recursive(matrix: List[List[int]], n) -> int:
    """
    Recursive calculate determinant of sqare matrix
    params: matrix: square matrix
    return: determinant
    """
    if n == 1:
        return matrix[0][0]
    det = 0
    first_row = matrix[0]
    for j, item in enumerate(first_row): # n * (n-1) * (n-2) ... 1 
        minor = get_minor(matrix, 0, j) 
        sign = (-1)  ** j
        det += item * sign * _calcualte_determinant_recursive(minor, n-1) # n-1
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
        print(f"Validation error: {e}")
        raise

def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)
    
    print(f"Minor is {get_minor(matrix, 0, 0)}")
    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()