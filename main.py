def get_matrix(n, m, value):
    matrix = []
    """
    :param n:количество строк.
    :param m:количество столбцов.
    :param value:значение для заполнения матрицы
    :return:вложенный список
    """
   
    for i in range(n):
        row =  [value]*m    #- создаем строку с нужными значениями.
        matrix.append(row)

    return matrix

matrix1 = get_matrix(2,2,10)
print(matrix1)
matrix2 = get_matrix(3,5,42)
print(matrix2)
matrix3 = get_matrix(4,2,13)
print(matrix3)



