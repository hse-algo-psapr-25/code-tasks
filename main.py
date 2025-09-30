def get_tridiagonal_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель трехдиагональной целочисленной квадратной матрицы.
    :param matrix: целочисленная трехдиагональная квадратная матрица.

    :return: значение определителя.
    """

    if not isinstance(matrix, list):
        raise Exception("Переменная должна быть списком")
    
    if len(matrix) == 0:
        raise Exception("Список должен быть ненулевым")
    
    for row in matrix:
        if not isinstance(row, list):
            raise Exception("Каждая строка должна являться списком")
        if len(row) == 0:
            raise Exception("Каждая строка должна быть ненулевой")
        if len(row) != len(matrix):
            raise Exception("Матрица не является квадратной")
        for i in row:
            if not isinstance(i, int):
                raise Exception("Матрица не является целочисленной")
    
    n = len(matrix)

    if n == 1:
        return matrix[0][0]
    
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    
    for i in range(n):
        for j in range(n):
            if abs(i-j) > 1 and matrix[i][j] != 0:
                raise Exception("Матрица не является трехдиагональной")
            
    for i in range(1, n):
        if matrix[i][i] != a:
            raise Exception("Матрица не является трехдиагональной")
   
    if n == 2:
        return a * a - b * c
    
    for i in range(1, n-1):
        if matrix[i][i+1] != b:
            raise Exception("Матрица не является трехдиагональной")
        
    for i in range(2, n):
        if matrix[i][i-1] != c:
            raise Exception("Матрица не является трехдиагональной")
        

    def calculate_tridiagonal_determinant(a, b, c,  order):

        if order == 1:
            return a

        if order == 2:
            return a * a - b * c
        
        return a * calculate_tridiagonal_determinant(a, b, c, order-1) - b * c * calculate_tridiagonal_determinant(a, b, c, order-2)
        
    return calculate_tridiagonal_determinant(a, b, c, n)


def main():
    matrix = [[2, -3, 0, 0], [5, 2, -3, 0], [0, 5, 2, -3], [0, 0, 5, 2]]
    print("Трехдиагональная матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {get_tridiagonal_determinant(matrix)}")


if __name__ == "__main__":
    main()
