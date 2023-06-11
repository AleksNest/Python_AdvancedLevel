'''
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
'''


my_string = input('введите строку').split()

my_string.sort()
print(my_string)

longest = len(max(my_string, key=len))  # max возвращает самую длиную строку
#longest = len(max(my_string))
for num, element in enumerate(my_string, 1):
    print(f'{num} {element:>{longest}}')