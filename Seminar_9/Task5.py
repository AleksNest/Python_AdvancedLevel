'''
Задание №5
Объедините функции из прошлых задач.
Функцию угадайку задекорируйте: (задача 1)
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.

'''

import json
import random
from typing import Callable


def save_param_deco(func):                                              #декоратор для сохранения параметров функции в json
    def wrapper(*args, **kwargs ):
        result = func(*args, **kwargs)
        filename = f'{func.__name__}.json'
        dump_dict = {}
        dump_dict["arguments"] = [*args]
        for key, value in kwargs.items():
            dump_dict[key] = value
        dump_dict["result"] = result
        json.dump(dump_dict, open(filename, 'a', encoding="utf-8"), indent=4, ensure_ascii=False)       #indent=4 - переносит и ставит 4 пробела,  ensure_ascii=False - корректно выводит кириллицу
        return result
    return wrapper


def param_control_deco(fun: Callable) -> Callable:                      #декоратор для контроля пределов значений функции

   def wrapper(guess: int, attempts: int):
       guess = guess if 1 < guess < 100 else random.randint(1, 100)
       attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
       return fun(guess, attempts)

   return wrapper


def counter_deco(num: int):                                                  #декоратор длоя многократного запуска функции
    def level_one(func: Callable):
        cache = []

        def wrapper(*args, **kwargs):
            for _ in range(num):
                cache.append(func(*args, **kwargs))
            return cache

        return wrapper
    return level_one


# декорируемся: в следующей последовательности
@counter_deco(3)                                                        # 3 раза вызываепт функцию guess_game
@param_control_deco                                                     # проверяет параметры на вхождение в диапазон
@save_param_deco                                                        # записывает результаты в Json
def guess_game(guess: int, attempts: int):                              # сама функция угадай число с n попыток раз
    while attempts > 0:
        attempts -= 1
        val = int(input("Угодай число"))
        if val == guess:
            return "вы победили"
    return "кол попыток исчерпано"


print(guess_game(5, 2))
