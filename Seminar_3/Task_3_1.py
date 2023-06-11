'''
Задание №1
✔ Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
✔ *Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.
'''

my_list = [1, 1, 2, 3]

#  короткое решение
# 1 вариант
print(list(set(my_list)))

# длинное решение
# 2 вариант
my_list = [1, 1, 2, 3]
my_set = {my_list[0]}
list_new = []
for i in my_list:
    my_set.add(i)
for i in my_set:
    list_new.append(i)
print(my_set)
print(list_new)


# 3 вариант
for i in my_list:
    if i not in list_new:
        list_new.append(i)

print(list_new)
