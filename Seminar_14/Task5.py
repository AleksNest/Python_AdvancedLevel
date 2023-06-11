'''
Задание №5
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.
'''

from Seminar_14.Rentagle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):

    def test_1_area(self):
        self.assertEqual(Rectangle.get_area(Rectangle(2)), 4)       # проверяем что при вызове метода с экземпляром = 2, площадь = 4

    def test_2_perimeter(self):
        self.assertEqual(Rectangle.get_perimeter(Rectangle(2, 3)), 10)

    def test_2_sub(self):
        self.assertEqual(str(Rectangle(3, 4) - Rectangle(2, 3)), str(Rectangle(1, 1)))    #вывод должен быть как в классе Rectangle прописанный в repr: return f"Rectangle({self._side_a}, {self._side_b})"

    def test_2_sum(self):
        self.assertEqual(str(Rectangle(3, 4) + Rectangle(2, 3)), str(Rectangle(5, 7)))


if __name__ == '__main__':
    unittest.main(verbosity=2)
