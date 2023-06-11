"""
сравнение, умножение, сложение двух матриц
"""
from My_exception import ValFormatError

class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError("+")
            # return f'Error: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            raise ValFormatError("*")
            # return f'Error: невозможно перемножить матрицы'
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError("eq")
            # return f'Error: матрицы разных размеров'
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s


if __name__ == '__main__':

    m_1 = [[1, 2, 4],
              [5, 6,  8],
              [2, 5, -2],
              [10, 5, 0]]

    m_2 = [[1, 2, 4],
              [5, 6,  8],
              [5, 6,  8],
              [-2, 2, 0]]

    m_3 = [[1, 2, 4, 5],
              [5, 6, 8, 0],
              [5, 0, -7, 1]]

    m_4 = [[1, 2, 4, 5, 0],
              [5, 6, 8, 0, 0],
              [5, 0, -7, 1, 0]]

    matr_1 = Matrix(m_1)
    matr_2 = Matrix(m_2)
    matr_3 = Matrix(m_3)
    matr_4 = Matrix(m_4)

    print ("Cложение матриц:")
    matr_sum = matr_1 + matr_2
    print(matr_sum)

    print ("Умножение матриц:")
    matr_mul = matr_1 * matr_3
    print(matr_mul)
    print(matr_1 * matr_4)

    print ("Cравнение матриц:")
    print(matr_1 == matr_3)
    print(matr_1 == matr_2)
