from logging import raiseExceptions


def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    if matrix is None:
        raise ValueError("Матрица не может быть None")

    if len(matrix) == 0:
        raise ValueError("Матрица не может быть пустой")

    n = len(matrix)

    for row in matrix:
        if len(row) != n:
            raise ValueError("Матрица должна быть квадратной и не ступенчатой")

    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise ValueError("Элементы вне диагонали должны быть нулями")

    a = matrix[0][0]
    b = matrix[0][1] if n > 1 else None
    c = matrix[1][0] if n > 1 else None

    for i in range(n):
        if matrix[i][i] != a:
            raise ValueError("Элементы главной диагонали должны быть одинаковыми")

    if n > 1:
        for i in range(n - 1):
            if matrix[i][i + 1] != b:
                raise ValueError("Элементы верхней диагонали должны быть одинаковыми")
        for i in range(n - 1):
            if matrix[i + 1][i] != c:
                raise ValueError("Элементы нижней диагонали должны быть одинаковыми")

    if n == 1:
        return a
    elif n == 2:
        return a*a - b*c
    else:
        return a * get_tridiagonal_determinant([row[:-1] for row in matrix[:-1]]) \
               - b * c * get_tridiagonal_determinant([row[:-2] for row in matrix[:-2]])


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
