def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.
    :return: значение определителя.
    """
    if not isinstance(matrix, list):
        raise ValueError("Матрица должна быть массивом массивов")
    n = len(matrix)
    if n == 0:
        raise ValueError("Матрица не должна быть пустой")
    if any(not isinstance(row, list) or len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    for i in range(n):
        for j in range(n):
            if not isinstance(matrix[i][j], int):
                raise ValueError("Каждый элемент матрицы должен быть целым числом")
            if j < i - 1 or j > i + 1:
                if matrix[i][j] != 0:
                    raise ValueError("Матрица должна быть трёхдиагональной")
    a = [matrix[i][i] for i in range(n)]
    if any(x != a[0] for x in a):
        raise ValueError("Неверные значения на главной диагонали")
    if n > 1:
        b = [matrix[i][i + 1] for i in range(n - 1)]
        c = [matrix[i + 1][i] for i in range(n - 1)]
        if any(x != b[0] for x in b):
            raise ValueError("Неверные значения на верхней диагонали")
        if any(x != c[0] for x in c):
            raise ValueError("Неверные значения на нижней диагонали")
    else:
        b = []
        c = []
    determinant = [0] * (n + 1)
    determinant[0] = 1
    determinant[1] = a[0]
    for i in range(2, n + 1):
        determinant[i] = a[i - 1] * determinant[i - 1] - b[i - 2] * c[i - 2] * determinant[i - 2]
    return determinant[n]


def main():
    matrix = [
        [2, -3, 0, 0],
        [5, 2, -3, 0],
        [0, 5, 2, -3],
        [0, 0, 5, 2],
    ]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)
    print(get_tridiagonal_determinant(matrix))


if __name__ == "__main__":
    main()
