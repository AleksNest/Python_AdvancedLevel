'''
Задание №3
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в
диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
'''

class FactGenerator:
    def __init__(self, *args):
        self.start, self.stop, self.step = 1, 1, 1
        match args:
            case (stop,):                   # в case обязательно  кортежи, для кортежа в скобках из одного элемента, нужна запятая
                self.stop = stop
            case (start, stop,):
                self.stop = stop
                self.start = start
            case (start, stop, step):
                self.stop = stop
                self.start = start
                self.step = step
            case _:
                raise AttributeError("Function takes up to 3 parameters")

        if self.start > self.stop:
            raise AttributeError("Error start muct be less than stop")

        self.factorial = [*range(self.start, self.stop, self.step)]


    @staticmethod               # статический метод - он объект не передает, а используется внутри класса - здесь self не нужен
    def calc(limit) -> int:     #limit - число до которого считаем факториал
        if limit < 0:
            raise ValueError("Incompatible value")
        if limit in (0, 1):
            return 1
        else:
            result = 1
            for i in range(1, limit + 1):
                result *= i
            return result

    def __iter__(self):
        return self

    def __next__(self):
        if self.factorial:
            return self.calc(self.factorial.pop(0)) # как только factorial список будет пустой, останавливается генератор
        raise StopIteration

    def __str__(self):
        return f'Factorial range: {self.factorial}'


def main():
    factorials = FactGenerator(0, 5, 1)
    print(factorials)
    for i in factorials:
        print(i)



if __name__ == '__main__':
    main()


