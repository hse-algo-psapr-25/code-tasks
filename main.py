def validation(matrix: list[list[int]]):
    if not isinstance(matrix, list):
       raise TypeError("Матрица должна быть списком с вложенными списками")
    
    order = len(matrix)

    if order == 0:
        raise ValueError("Матрица не должна быть пустой")
    
    for row in matrix:
        if len(row) != order:
            raise ValueError("Матрица должна быть квадратной")
        if not all(isinstance(x, int) for x in row):
            raise TypeError("Матрица должна содержать только целочисленные значения")
        
def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validation(matrix)
    n = len(matrix)
    match n:
        case 1:
            return matrix[0][0]
        case 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        case n:
            det = 0
            for i in range(n):
                minor = []
                for j in range(n):
                    a = []
                    for k in range(n):
                        if j != 0 and k != i:
                            a += [matrix[j][k]]
                    if a != []:
                        minor += [a]
                det += matrix[0][i] * calculate_determinant(minor) * (-1)**i
            return det


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")


if __name__ == "__main__":
    main()
