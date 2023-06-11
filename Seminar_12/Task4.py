'''
Задание №4
Доработайте класс прямоугольник из прошлых семинаров.
Добавьте возможность изменять длину и ширину
прямоугольника и встройте контроль недопустимых значений
(отрицательных).
Используйте декораторы свойств

Задание №5
Доработаем прямоугольник и добавим экономию памяти
для хранения свойств экземпляра без словаря __dict__
'''


class Rectangle:
    __slots__ = ('_width', '_length')         # чтобы сэкономить память, но при пользуемся только проинициализированными атрибутами
    #Property создает словарь __dict__, где хранится все инфо(объекты) о классе,
    # где можно добавлять через объект атрибуты  для класса бесконечно раз
    #При использовании __slots__ - в __dict__  буду уже хранится только проинициализированные в классе переменные  width, length и
    # создать новый атрибут в классе невозможно, напрмер, rect.mass = 7,


    def __init__ (self, width: float, length: float = None) -> None:
        self._width = width
        self._length = length if length else width    # если длина None, то получаем квадрат


    @property                           # делает self._length как self.length - как гетерр работает, только обращаемся напрямую через свойства- инкапсуляция
    def width(self):
        return self._width

    @property
    def length(self):
        return self._length

    @length.setter      # декоратор задает длину
    def length(self, new_len):                          # изменить можно length с помощью декоратора предварительно проверив - рпаботает как сетер
        if new_len <= 0:
            raise ValueError("Length must not be than 0")
        self._length = new_len

    @width.setter  # декоратор задает длину
    def width(self, new_widht):
        if new_widht <= 0:
            raise ValueError("Length must not be than 0")
        self._width = new_widht


    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length                 # вызывает property c length и возвращает _length

    def __str__(self):
        return (f'\nRectangle: {self.width} X {self.length}' 
                f'\nPerimeter: {self.get_perimeter()}')

    def __repr__(self):
        return f'Rectangle({self.width}, {self.length})'

def main():
    rect = Rectangle(10, 20)
    print(f'{rect=}')
    print(rect.__str__())

    rect.length = 100           # обращается к  @length.setter чтобы изменить
    rect.width = 200
    print(f'{rect=}')
    print(rect.__str__())

    print(rect.__slots__)

    try:
        rect.length = 0
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    try:
        rect.length = -100
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    print(f'{rect=}')

if __name__ == '__main__':
    main()