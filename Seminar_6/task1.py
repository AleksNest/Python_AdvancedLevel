'''
Задача 1 Вспомните какие модули вы уже проходили на курсе.
Создайте файл, в котором вы импортируете встроенные в модуль функции под псевдонимами.
(3-7 строк импорта).
'''

from decimal import Decimal as D
from random import randint as rnd
from math import sqrt as sq
from sys import argv as arguments
from fractions import Fraction as F


'''
Задача 0 Проверка ключа на неизменяемость в словаре
'''

my_dict = {(4, 5, 6): [3, 4, 5]}
new_dict = {}

for key, value in my_dict.items():
    try:
        hash(value)
        new_dict[value] = key
    except:
        new_dict[str(value)] = key

print(new_dict)
