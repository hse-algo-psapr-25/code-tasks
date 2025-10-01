import random
from collections import namedtuple

Case = namedtuple("Case", ["matrix", "det"])
MAX_RANDOM_VALUE = 10
MIN_RANDOM_VALUE = 1

def add_row_multiple(matrix, order):
    for m in range(order * 2):
        i, j = random.sample(range(order), 2)
        rand_coef = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
        for col in range(order):
            matrix[i][col] += (-1) ** m * rand_coef * matrix[j][col]


def add_col_multiple(matrix, order):
    for m in range(order * 2):
        i, j = random.sample(range(order), 2)
        rand_coef = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
        for row in range(order):
            matrix[row][i] += (-1) ** m * rand_coef * matrix[row][j]


def generate_matrix_and_det(order) -> Case:
    """Генерирует случайную квадратную целочисленную матрицу с заранее
    известным значением определителя.

    :param order: порядок матрицы
    :raise Exception: если порядок матрицы не является целым числом и порядок
    меньше 1
    :return: именованный кортеж Case с полями matrix, det
    """
    if not isinstance(order, int) or order < 1:
        raise Exception("Order must be a positive integer")

    det = random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)
    
    # если порядок 1, то матрица из одного элемента (определителя)
    if order == 1:
        return Case(matrix=[[det]], det=det)
    
    # создаем единичную матрицу
    matrix = [[1 if i == j else 0 for j in range(order)] for i in range(order)]

    # первый элемент матрицы -- определитель
    matrix[0][0] = det 

    add_row_multiple(matrix, order)
    add_col_multiple(matrix, order)

    return Case(matrix=matrix, det=det)

def main():
    n = 4
    print(f"Генерация матрицы порядка {n}")
    result = generate_matrix_and_det(n)
    print("\nОпределитель сгенерированной матрицы равен", result.det)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in result.matrix]))


if __name__ == "__main__":
    main()