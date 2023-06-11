'''
Задание №1
Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток
Внутри есть функция, которая запрашивает у пользователя число
'''
import random
from typing import Callable


def guess_function(guess: int, attempts: int) -> Callable:      # внешняя функция для замыкания
    count = attempts
    val = -1

    def attempts_count():                               #внутрення функция  угадайка делает основной функционал
        nonlocal count
        nonlocal val
        while count > 0:
            count -= 1
            val = int(input("Угодай число"))
            if val == guess:
                return "Вы выигрвли"
        return "Кол попыток исчерпано"
    return attempts_count                               # обязательно должна возвращать имя внутренней функции


game1 = guess_function(5, 3)                            # переменная типа функция
game2 = guess_function(10, 3)


print(game1())
print(game2())