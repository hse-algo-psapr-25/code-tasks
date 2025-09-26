from typing import List


def validate_matrix(matrix: List[List[int]]):
    if not isinstance(matrix, list):
        raise ValueError('Matrix should be list')
    

def get_minor(maxtrix: List[List[int]]):...


def _calcualte_determinant_recursive(maxtrix: List[List[int]]) -> int:...


def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    try:
        validate_matrix(matrix)
        return _calcualte_determinant_recursive(matrix)
    except Exception as e:
        print(f"Validation error: {e}")
        raise


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
