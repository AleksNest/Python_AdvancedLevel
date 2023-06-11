'''
Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь.

'''
import math

class Circle:

    def __init__(self, radius: int = 1):
        self._radius = radius

    def get_lenth(self):
        return 2 + math.pi * self._radius

    def area(self):
        return math.pi * self._radius ** 2


circle = Circle(3)
print(f'{circle.get_lenth() = :2f},   {circle.area() = :2f}')