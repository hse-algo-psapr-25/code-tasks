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

    middle = matrix[0][0]
    for i in range(1, n):
        if matrix[i][i] != middle:
            raise ValueError("Неверные значения на главной диагонали")

    if n == 1:
        return middle

    upper = matrix[0][1]
    for i in range(1, n - 1):
        if matrix[i][i + 1] != upper:
            raise ValueError("Неверные значения на верхней диагонали")

    lower = matrix[1][0]
    for i in range(2, n):
        if matrix[i][i - 1] != lower:
            raise ValueError("Неверные значения на нижней диагонали")

    prev2 = 1
    prev1 = middle

    for i in range(1, n):
        current = middle * prev1 - upper * lower * prev2
        prev2, prev1 = prev1, current

    return prev1


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