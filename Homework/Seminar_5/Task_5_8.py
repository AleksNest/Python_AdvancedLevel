'''
Задача 1
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
'''

import os

print('Задача 1')
string = "C:/Алексей/Desktop/GreekBrains/ДОМАШКА/Python_advanced/Seminar2/seminar.py"

def fun(f_path: str) -> tuple:
    path, filename = os.path.split(f_path)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {string} \nКортеж из пути: {fun(string)}')


'''
Задача 2
✔ Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
'''

print('\nЗадача 2')
names = ['Alex', 'Adam', "eva"]
salaries = [15000, 20000, 25000]
awards = ['10.0%', '7.25%', '5%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Решение:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})

'''
Задача 3
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''
print('\nЗадача 3')
a = int(input('введите число  '))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(a)))
