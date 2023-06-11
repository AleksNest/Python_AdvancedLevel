'''
Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.

декоратор должен проверять значения функции угадайка чтобы были в допустимых пределах
то есть в декораторе будет обертка  wrapper  для любой функции (fun), которая будет передана в декоратор
декоратор возвращает обертку wrapper
'''

import random
from typing import Callable

def guess_function(fun: Callable) -> Callable:      # принимает только ссылку на функцию

   def wrapper(guess: int, attempts: int):         #обертка проверяет диапозон параметров функции угадайка
       guess = guess if 1 < guess < 100 else random.randint(1, 100)
       attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
       return fun(guess, attempts)

   return wrapper

@guess_function                                                             #функция теперь будет вызываться через декоратор
def attempts_count(guess: int, attempts: int):                               #внутрення функция  угадайка делает основной функционал
    while attempts > 0:
        attempts -= 1
        val = int(input("Угодай число"))
        if val == guess:
            return "Вы выигрвли"
    return "Кол попыток исчерпано"


print(attempts_count(150, 15))