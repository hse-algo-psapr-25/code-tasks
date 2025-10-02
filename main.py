def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """
    if type(matrix) is not list:
        raise ValueError("Матрица должна быть массивом массивов")
    n = len(matrix)
    if any(len(row) != n for row in matrix):
        raise ValueError("Матрица должна быть квадратичная")
    for i in range(n):
        for j in range(n):
            if j < i - 1 or j > i + 1:
                if matrix[i][j] != 0 :
                    raise ValueError("Матрица должна быть трёхдиагональная")
            if type(matrix[i][j]) is not int:
                raise ValueError("Каждый элемент матрицы должен быть целым числом")
    if n == 0:
        return 1
    
    a = []
    for i in range (n):
        a.append(matrix[i][i])
    b = []
    for i in range(n - 1):
        b.append(matrix[i][i + 1])
    c = []
    for i in range(n - 1):
        c.append(matrix[i + 1][i])

    determinant = [0] * (n + 1)
    determinant[0] = 1
    determinant[1] = a[0]
    for i in range(2, n + 1):
        determinant[i] = a[i - 1] * determinant[i - 1] - b[i - 2] * c[i - 2] * determinant[i - 2]
    return determinant[n]


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
