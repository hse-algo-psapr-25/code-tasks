def check_matrix(matrix: list[list[int]]) -> int:
    if matrix is None:
        raise Exception("Matrix is None")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Empty matrix")

    order = len(matrix)

    for i in range(len(matrix)):
        if order != len(matrix[i]):
            raise Exception("Not square")

        for j in range(len(matrix[i])):
            if abs(i - j) > 1 and matrix[i][j]:
                raise Exception("Not zero by value")

    if order >= 2:
        a, b, c = matrix[0][0], matrix[0][1], matrix[1][0]

        for i in range(order):
            if a != matrix[i][i]:
                raise Exception("Wrong value on main diagonal")
            if i < order - 1 and b != matrix[i][i + 1]:
                raise Exception("Wrong value on upper diagonal")
            if i and c != matrix[i][i - 1]:
                raise Exception("Wrong value on lower diagonal")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    check_matrix(matrix)

    order = len(matrix)
    det = 1

    a = matrix[0][0]
    if order >= 1:
        d_prev2 = det = a

    if order >= 2:
        b, c = matrix[0][1], matrix[1][0]
        d_prev1 = det = a * a - b * c

    if order >= 3:
        for _ in range(2, order):
            d_prev2, d_prev1 = d_prev1, a * d_prev1 - b * c * d_prev2

        det = d_prev1

    return det


def main():
    matrix = [
        [2, -3, 0, 0],
        [5, 2, -3, 0],
        [0, 5, 2, -3],
        [0, 0, 5, 2]
    ]

    print("Трехдиагональная матрица")

    for row in matrix:
        print(row)

    return f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}"


if __name__ == "__main__":
    print(main())