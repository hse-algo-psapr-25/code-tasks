def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.
    :return: значение определителя.
    """
    
    if not isinstance(matrix, list):
        raise Exception("Переменная должна быть списком")
    n = len(matrix)
    if n == 0:
        raise Exception("Список должен быть ненулевым")

    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Каждая строка должна являться списком")
        if len(row) != n:
            raise Exception("Матрица не является квадратной")
        for item in row:
            if not isinstance(item, int):
                raise Exception("Матрица не является целочисленной")

    
    for i in range(n):
        for j in range(n):
            if abs(i - j) > 1 and matrix[i][j] != 0:
                raise Exception("Матрица не является трехдиагональной")

    
    if n == 1:
        return matrix[0][0]

    a = matrix[0][0]
    b = matrix[0][1]      
    c = matrix[1][0]      

    
    for i in range(1, n):
        if matrix[i][i] != a:
            raise Exception("Матрица не является трехдиагональной")

    
    for i in range(0, n - 1):
        if matrix[i][i + 1] != b:
            raise Exception("Матрица не является трехдиагональной")

    
    for i in range(1, n):
        if matrix[i][i - 1] != c:
            raise Exception("Матрица не является трехдиагональной")

    
    if n == 2:
        return a * a - b * c

    
    prev = a
    curr = a * a - b * c
    for _ in range(3, n + 1):
        nxt = a * curr - (b * c) * prev
        prev, curr = curr, nxt

    return curr


def main():
    matrix = [[2, -3, 0, 0],
              [5, 2, -3, 0],
              [0, 5, 2, -3],
              [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)
    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
