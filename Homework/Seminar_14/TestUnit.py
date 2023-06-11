from Homework.Seminar_14.Matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(str(Matrix([[1, -2], [25, -5]]) + Matrix([[11, -8], [15, 0]])), '[12, -10][40, -5]')

    def test_mul(self):
        self.assertEqual(str(Matrix([[1, -2], [25, -5]]) * Matrix([[11, -8], [15, 0]])), '[-19, -8][200, -200]')


if __name__ == '__main__':
    unittest.main(verbosity=2)