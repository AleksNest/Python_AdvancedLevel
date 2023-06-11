'''
Задание №4
Напишите для задачи 1 тесты pytest. Проверьте следующие
варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)

'''

import pytest                                       # импорт предварительно установленного фреймворка для проведения тестирования

from Seminar_13.Task1 import checkstr

def test():
    assert checkstr('hello geekbrains') =='hello geekbrains', "ошибка текст 1"      # при выплнении функции checkstr должно равняться правой строке, если ошибка печатает "Ошибка 1"

    assert checkstr('HeLlo GeekBrains') == 'hello geekbrains', "ошибка текст 2"

    assert checkstr('HeLlo, GeekBrains!') == 'hello geekbrains', "ошибка текст 3"

    assert checkstr('Hello% Geek!Brain&!s!') == 'hello geekbrains', "ошибка текст 4"

    assert checkstr('Hello%"му Geek!Brain&!s!') == 'hello geekbrains', "ошибка текст 5"

if __name__ == '__main__':
    pytest.main([-v])                   # запуск теста с подробным описанием (ключ v)



