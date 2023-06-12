"""
Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
командной строки с передачей параметров.
на примере  сравнение, умножение, сложение двух матриц
"""

import logging
from random import randint




logging.basicConfig(filename='Log.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}] ')
            #raise ValFormatError

        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))] for i in range(len(self._matr))])
            logger.info(f' СЛОЖЕНИЕ:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr


    def __mul__(self, other):
        if len(self._matr[0]) != len(other._matr):
            logger.error(f'Не возможно выполнить умножение матриц, размерности матриц несовместимы: [{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            #raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)] for i_row in self._matr]
            logger.info(f' УМНОЖЕНИЕ:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return False
            logger.info(f' РАВЕНСТВО:  {self._matr} = {other._matr} ')
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

    m_1 = [[1, 2, 4],
              [5, 6,  8],
              [2, 5, -2],
              [10, 5, 0]]

    m_2 = [[1, 2, 4.5],
              [5, 6,  8],
              [5, 6,  8],
              [-2, 2, 0]]

    m_3 = [[1, 2, 4, 5, 6],
              [5, 6, 8, 0],
              [5, 0, -7, 1]]

    m_4 = [[1, 2, 4, 5, 0],
              [5, 6, 8, 0, 0],
              [5, 0, -7, 1, 0]]

    print ("Cложение матриц:")
    print(Matrix(m_1) + Matrix(m_2))
    print(Matrix(m_3) + Matrix(m_1))

    print("Cравнение матриц:")
    print(Matrix(m_1) == Matrix(m_1))

    print("Умножение матриц:")
    print(Matrix(m_1) * Matrix(m_3))
    print(Matrix(m_1) * Matrix(m_2))







