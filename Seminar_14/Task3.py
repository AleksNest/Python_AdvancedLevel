'''Задание №3
Напишите для задачи 1 тесты unittest. Проверьте
следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери
символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов
(кроме п. 1)'''

from Seminar_14.Task1 import checkstr
import unittest


class TestCaseName(unittest.TestCase):                      # название класса  начинаться нужно обязательно со слова Test

    def test_method(self):                                       # название метода начинаться нужно обязательно со слова test
        self.assertEqual(checkstr('hello geekbrains'),      # сравнение строк
                         'hello geekbrains')

        self.assertEqual(checkstr('HeLlo GeekBrains'),
                         'hello geekbrains')

        self.assertEqual(checkstr('HeLlo, GeekBrains!'),
                         'hello geekbrains')

        self.assertEqual(checkstr('Hello% Geek!Brain&!s!'),
                         'hello geekbrains')


if __name__ == '__main__':
    unittest.main(verbosity=2)                                  # запуск теста с ключом 2 - подробное описание рез теста
