'''
Задание №5
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися целыми числами.
✔ Сформируйте список с порядковыми номерами
нечётных элементов исходного списка.
✔ Нумерация начинается с единицы.
'''


my_list = [1, 2, 3, 5, 7, 8, 9, 10, 9, 8, 10]
new_list = []
for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        new_list.append(i + 1)
print([i + 1 for i in range(len(my_list)) if my_list[i] % 2 != 0])          # короткий вариант записис (однострочник)
print(new_list)
