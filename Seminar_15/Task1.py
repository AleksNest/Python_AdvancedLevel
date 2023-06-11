'''
Задание №1
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.

'''

import logging

logging.basicConfig(filename='Task1.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.ERROR)
logger = logging.getLogger(__name__)

def div(a, b):
    try:
        res = a/b
    except:
        logger.error(f'Ошибка деления на ноль! Число {a} нельзя поделить на число {b}')
        return float('inf')         # возврат бесконечности
    return res

if __name__ == '__main__':
    print(div(2, 0))