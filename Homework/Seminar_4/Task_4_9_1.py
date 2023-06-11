'''
Задача 1 Напишите функцию для транспонирования матрицы .
'''


print('Задача1')
matrix = [[1, 2, 8, 7],
          [6, 12, 10, 5]]

print("исходная матрица:\n", matrix)

# 1 вариант решения
def matrix_transposition_1(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]  # структура транспонированной матцы
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)

# 2 вариант решения
def matrix_transposition_2(matrix):
    trans_matrix = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(trans_matrix)

print("транспонированная матрица по варианту решения 1:")
matrix_transposition_1(matrix)
print("транспонированная матрица по варианту решения 2:")
matrix_transposition_2(matrix)