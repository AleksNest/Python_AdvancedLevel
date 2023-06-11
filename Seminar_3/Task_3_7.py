'''
Задание №7
Погружение в Python | Коллекции
✔ Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.
✔ Обратите внимание на порядок ключей.
Объясните почему они совпадают
или не совпадают в ваших решениях.
'''


string = input("введите текст")
my_set = set(string)
my_dict_1 = {}
my_dict_2 = {}
my_dict_3 = {}
my_dict_4 = {}
# for i in range(len(string)):
#     my_set.add(string[i])

# с count
for i in my_set:
    #my_dict_1[i] = string.count(i)
    my_dict_1.setdefault(i, string.count(i))
print(my_dict_1)

# без count
count = 0
for i in my_set:
    for j in range(len(string)):
        if string[j] == i:
            count +=1
    my_dict_2[i] = count
    count = 0
print(my_dict_2)

# еще вариант
for char in string:
    my_dict_3[char] = my_dict_3.get(char, 0) + 1
print (my_dict_3)

# еще вариант
for i in string:
    my_dict_4[i] = string.count(i)
print (my_dict_4)