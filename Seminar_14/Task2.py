
'''Задание №2
Напишите для задачи 1 тесты doctest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)
'''

import re                                       # модуль регулярных выражений


def checkstr(text: str):
    '''Удаляет из текста все символы, кроме букв латинского алфавита и пробелов
    >>> checkstr('hello geekbrains')
    'hello geekbrains'
    >>> checkstr('HeLlo GeekBrains')
    'hello geekbrains'
    >>> checkstr('HeLlo, GeekBrains!')
    'hello geekbrains'
    >>> checkstr('hello geekbrains')
    'hello geekbrains'
    >>> checkstr('Hello% Geek!Brain&!s!')
    'hello geekbrains'
    '''

    regex = re.compile('[^a-zA-Z ]')         #задаеется что нужно оставить буквы и пробел
    return regex.sub('', text).lower()      # из строки убирается все, кроме того, что указали в прпед строке


if __name__ == '__main__':
    print(checkstr('Hello% Geek!Brain&!s!'))
    import doctest
    doctest.testmod(verbose=True)                       #вывод подробный результата тестов

