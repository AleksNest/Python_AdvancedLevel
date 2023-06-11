'''
Задание №3
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

'''

import logging
import  random
from functools import wraps

logging.basicConfig(filename='Task3.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def one(func):
    @wraps(func)                            #декоратор «functool.wraps», чтобы декорировать нашу внутреннюю функцию, функцию «wrapper». Применяя этот декоратор «wraps» к нашей внутренней функции, мы копируем имя, строку документации и сигнатуру функции в нашу внутреннюю функцию, избегая проблем, с которыми мы сталкивались ранее:
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