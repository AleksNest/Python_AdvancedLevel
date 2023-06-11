"""
сравнение, умножение, сложение двух матриц
"""
from Homework.Seminar_14.Exception import ValFormatError

class Matrix:
    '''
    >>> Matrix([[1, 2, 4],[5, 6,  8],[2, 5, -2],[10, 5, 0]]) + Matrix([[1, 2, 4],[5, 6,  8], [5, 6,  8], [-2, 2, 0]])
    [2, 4, 8][10, 12, 16][7, 11, 6][8, 7, 0]
    >>> Matrix([[1, 2, 4],[5, 6,  8],[2, 5, -2],[10, 5, 0]]) * Matrix([[1, 2, 4, 5],[5, 6, 8, 0],[5, 0, -7, 1]])
    [31, 14, -8, 9][75, 46, 12, 33][17, 34, 62, 8][35, 50, 80, 50]
    >>> Matrix([[1, 2, 4],[5, 6,  8],[2, 5, -2],[10, 5, 0]]) == Matrix([[1, 2, 4],[5, 6,  8],[2, 5, -2],[10, 5, 0]])
    True
    '''

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
            # return f'Error: матрицы разных размеров'
        else:
            return Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])

    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            return True

    # def __str__(self):
    #     s = ''
    #     for i in range(len(self._matr)):
    #         s += str(self._matr[i]) + '\n'
    #     return s

    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)



    # m_1 = [[1, 2, 4],
    #           [5, 6,  8],
    #           [2, 5, -2],
    #           [10, 5, 0]]
    #
    # m_2 = [[1, 2, 4],
    #           [5, 6,  8],
    #           [5, 6,  8],
    #           [-2, 2, 0]]
    #
    # m_3 = [[1, 2, 4, 5],
    #           [5, 6, 8, 0],
    #           [5, 0, -7, 1]]
    #
    # m_4 = [[1, 2, 4, 5, 0],
    #           [5, 6, 8, 0, 0],
    #           [5, 0, -7, 1, 0]]
    #
    # print ("Cложение матриц:")
    # print(Matrix(m_1) + Matrix(m_2))
    #
    # print ("Умножение матриц:")
    # print(Matrix(m_1) * Matrix(m_3))
    #
    # print ("Cравнение матриц:")
    # print(Matrix(m_1) * Matrix(m_1))

