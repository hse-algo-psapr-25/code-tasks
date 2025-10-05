def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.
    :return: значение определителя.
    """

    if matrix is None or not isinstance(matrix, list):
        raise Exception("Матрица должна быть списком списков")

    n = len(matrix)
    if n == 0:
        raise Exception("Матрица пуста")

    for row in matrix:
        if not isinstance(row, list) or len(row) != n:
            raise Exception("Матрица не квадратная")
        for val in row:
            if not isinstance(val, int):
                raise Exception("Матрица должна быть целочисленной")


    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Матрица не является трёхдиагональной")


    main_val = matrix[0][0]
    for i in range(n):
        if matrix[i][i] != main_val:
            raise Exception("Неверное значение на главной диагонали")

    if n > 1:
        upper_val = matrix[0][1]
        for i in range(n - 1):
            if matrix[i][i + 1] != upper_val:
                raise Exception("Неверное значение на верхней диагонали")

        lower_val = matrix[1][0]
        for i in range(1, n):
            if matrix[i][i - 1] != lower_val:
                raise Exception("Неверное значение на нижней диагонали")


    if n == 1:
        return main_val
    if n == 2:
        return main_val * main_val - upper_val * lower_val

    d = [0] * n
    d[0] = main_val
    d[1] = main_val * main_val - upper_val * lower_val
    for k in range(2, n):
        d[k] = main_val * d[k - 1] - upper_val * lower_val * d[k - 2]

    return d[-1]


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]

    print("Трехдиагональная матрица:")
    for row in matrix:
        print(row)

    det = get_tridiagonal_determinant(matrix)
    print(f"Определитель матрицы равен {det}")


if __name__ == "__main__":
    main()
