'''
расчет площади, периметра прямоугольника,
селадывание и вычитание двух прямоугольников

'''

from My_exception import ValError

class Rectangle:

    def __init__(self, side_a: float, side_b: float | None =None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a

    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)


    def get_area(self):
        return self._side_a * self._side_b

    def __add__(self, other):
        return Rectangle(self._side_a + other._side_a, self._side_b + other._side_b)

    def __sub__(self, other):
        return Rectangle(abs(self._side_a - other._side_a), abs(self._side_b - other._side_b))

    def __str__(self):
        return f"В результате - прямоугольник со сторонами: {self._side_a}   {self._side_b}, периметром: {self.get_perimeter()}, площадью: {self.get_area()}"





if __name__ == '__main__':
    flag = False
    while True:
        if flag:
            choise = input("1 - выход\n2 - продолжить\n")
            if choise == '1':
                break
        flag = True

        try:
            a_1 = float(input('введите первую сторону первого прямоугольника '))
            b_1 = float(input('введите стороны второго прямоугольника '))
            a_2 = float(input('введите первую сторону первого прямоугольника '))
            b_2 = float(input('введите стороны второго прямоугольника'))
        except ValueError as e:
            print(f"\nНеправильный формат ввода данных: {e}.\nПо умолчанию приняты все стороны прямоугольников = 1\n")
            a_1 = a_2 = b_1 = b_2 = 1

        if a_1 <= 0 or b_1 <= 0:
            raise ValError(a_1, b_1)
        if a_2 <= 0 or b_2 <= 0:
            raise ValError(a_2, b_2)

        rectangle_1 = Rectangle(a_1, b_1)
        print(f'{rectangle_1.get_perimeter() = },  {rectangle_1.get_area() = }')
        rectangle_2 = Rectangle(a_2, b_2)
        print(f'{rectangle_2.get_perimeter() = },  {rectangle_2.get_area() = }')
        choise = input("Выберите опреации над прямоугольниками\n1 - сложение\n2 - вычитание\n3 - выход\n")
        match choise:
            case '1':
                rectangle_3 = rectangle_1 + rectangle_2
                print(rectangle_3)

            case '2':
                rectangle_3 = rectangle_1 - rectangle_2
                print(rectangle_3)
            case _:
                break






