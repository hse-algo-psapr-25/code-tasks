from matrix_generator import generate_matrix_and_det

def validation_matrix(matrix: list[list[int]]):
    if not isinstance(matrix, list):
       raise TypeError("Matrix must be a list of lists")
    
    order = len(matrix)

    if order == 0:
        raise ValueError("Matrix must be non-empty")
    
    for row in matrix:
        if len(row) != order:
            raise ValueError("Matrix must be square")
        if not all(isinstance(x, int) for x in row):
            raise TypeError("Matrix must contain only integers")
        

def calculate_determinant(matrix: list[list[int]]) -> int:
    """Вычисляет определитель целочисленной квадратной матрицы

    :param matrix: целочисленная квадратная матрица
    :raise Exception: если значение параметра не является целочисленной
    квадратной матрицей
    :return: значение определителя
    """
    validation_matrix(matrix)
    return _rec_det(matrix)

def _rec_det(matrix: list[list[int]]) -> int:
    '''
    Рекурсивное вычисление определителя
    '''
    order = len(matrix)

    if order == 1:
        return matrix[0][0]
    
    det = 0
    for idx, item in enumerate(matrix[0]):
        det += item * (-1)**idx * _rec_det(_get_minor(0, idx, matrix))

    return det

def _get_minor(idx_row, idx_col, matrix):
    '''
    Возвращаем минор (матрицу без строки idx_row и столбца idx_col)
    '''
    return [[item for j, item in enumerate(row) if j != idx_col] for i, 
            row in enumerate(matrix) if i != idx_row]


def main():
    matrix = [[1, 2], [3, 4]]
    print("Матрица")
    for row in matrix:
        print(*row)

    print(f"Определитель матрицы равен {calculate_determinant(matrix)}")

    print("\nПроверка генератора случайных матриц")
    case = generate_matrix_and_det(4)
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in case.matrix]))
    print("Заранее известный определитель матрицы:", case.det)
    print("Определитель матрицы, вычисленный рекурсивно:", calculate_determinant(case.matrix))

if __name__ == "__main__":
    main()