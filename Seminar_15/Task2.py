'''
Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.
'''

import logging
import  random

logging.basicConfig(filename='Task2.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def one(func):                      # декоратор на функцию three
    def two(*args, **kwargs):
        rezult = func(*args)
        logger.info(f'Аргументы функции: {args}, результат: {rezult}')
        return rezult

    return two

@one
def three(a, b):
    return a + b

if __name__ == '__main__':
    print(three(random.randint(1, 11), random.randint(1, 11)))