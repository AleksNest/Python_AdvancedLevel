'''
Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
'''

class Rectangle:

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

rectangle1 = Rectangle(5)
rectangle2 = Rectangle(5, 2)

print(f'{rectangle1.get_perimeter() = },  {rectangle1.get_area() = }')
print(f'{rectangle2.get_perimeter() = },  {rectangle2.get_area() = }')