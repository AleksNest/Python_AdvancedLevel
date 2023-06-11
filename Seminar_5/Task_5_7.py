'''
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
'''

from typing import Generator

def primes(n: int) -> Generator:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            yield i


for num, i in enumerate(primes(100), start=1):
    print(f'{num} = {i}')

# Пример отличие return (обычной функции)от yield (функции-генератора)
from typing import Generator


def p(n) -> int:
    for i in range(n):
        return i

def p1(n) -> Generator:
    for i in range(n):
        yield i             # запоминает значение i и каждый раз при вызове функции начитнает соследующего значения i
        print('yield следующий')

gen = p1(10)        # кол значений не должно быть больше 10 иначе выбрасывает исключение при привышении кол генерации

for i in range(10):
    print('return ', p(10))
    print('yield   ', next(gen))