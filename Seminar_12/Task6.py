'''
Задание №6 (Тема дескриптор: класс в классе)
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину
на дескриптор с валидацией размера.
То есть создать треугольник, у которого есть ограничения по длине и ширине
'''


class Valid:                    #дескриптор

    def __init__(self, min_value: float = None, max_value: float = None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):        # делаем атрибуты защищенными _min_value  _max_value
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{value} is lesser than {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{value} is greater than {self.max_value}')



# атрибуты в init Rectangle в являются объектами класса Valid и при инициализации проверяются на диапазон в классе Valid
# в принципе вместо дескриптора можно было проверку атрибутов прописать в init Rectangle:
# if 1<width<100:
#     self.width=width
# else:
#     raise
class Rectangle:
    width = Valid(1, 100)           #ограничивает ширину для вычисления прямоугольника через класс Valid
    length = Valid(1, 200)


    def __init__ (self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.length)

    def get_area(self) -> float:
        return self.width * self.length  # вызывает property c length и возвращает _length

    def __str__(self):
        return f'Rectangle({self.width}, {self.length})' \
               f'\nPerimetr {self.get_perimeter()}' \
               f'\nArea {self.get_area()}'

    def __repr__(self):
        return f'Rectangle({self.width, self.length})'

def main():
    rect = Rectangle(10,20)
    print(rect.__str__())

    rect = Rectangle(10, 10)
    print(f'{rect=}')           # представление через __repr__
    print(rect.__str__())       # представление через __str__

    some_rect = Rectangle(10, 20)
    print(f'{some_rect=}')
    some_rect.length = 200
    some_rect.width = 100
    print(f'{some_rect=}')
    try:
        some_rect.length = 300
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    try:
        some_rect.width = -100
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    print(f'{some_rect=}')
    try:
        some_rect.length = 0.99
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    try:
        some_rect.width = 1.1
    except Exception as exc:
        print(f'\033[31m{exc.__class__.__name__}:{exc}\033[0m')
    print(f'{some_rect=}')


if __name__ == '__main__':
    main()


