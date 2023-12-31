"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение.

"""
from sys import argv
from my_pacage_task8.module_task2_task3 import func


if __name__ == '__main__':
    min_val, max_val, triers = map(int, argv[1:])   # переводим в Int
    func(min_val, max_val, triers)

# Здесь также работает программа, что и в task2, только ввод осущствляется не через консоль, а через
# терминал (командную строку), в которой надо набрать команду python task3.py 10 20 5
# где 10, 20, 5 - это min_val, max_val, triers