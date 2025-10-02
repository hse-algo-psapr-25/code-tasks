def check_matrix(matrix: list[list[int]]) -> int:
    if matrix is None:
        raise Exception("Matrix is None")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise Exception("Empty matrix")

    matrix_size = len(matrix)

    for i in range(len(matrix)):
        if matrix_size != len(matrix[i]):
            raise Exception("Not square")

        for j in range(len(matrix[i])):
            if abs(i - j) > 1 and matrix[i][j]:
                raise Exception("Not zero by value")

    if matrix_size >= 2:
        a_diag, b_diag, c_diag = matrix[0][0], matrix[0][1], matrix[1][0]

        for i in range(matrix_size):
            if a_diag != matrix[i][i]:
                raise Exception("Wrong value on main diagonal")
            if i < matrix_size - 1 and b_diag != matrix[i][i + 1]:
                raise Exception("Wrong value on upper diagonal")
            if i and c_diag != matrix[i][i - 1]:
                raise Exception("Wrong value on lower diagonal")


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    check_matrix(matrix)

    matrix_size = len(matrix)
    result_det = 1

    if matrix_size >= 1:
        a_diag = matrix[0][0]
        d_1 = result_det = a_diag

    if matrix_size >= 2:
        b_diag, c_diag = matrix[0][1], matrix[1][0]
        result_det = a_diag ** 2 - b_diag * c_diag

    if matrix_size >= 3:
        for k in range(2, matrix_size):
            result_det, d_1 = a_diag * result_det - b_diag * c_diag * d_1, result_det

    return result_det


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
