'''
 Задание 1
Сущуствует треугольник и если да, то какорй: разностороннй, равнобедренный или равносторонний.
'''

print('Задание 1\n')
a = 20
b = 20
c = 5
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует ")
    if a == b and b == c and a == c:
        print("треугольник - равносторонний")
    elif a == b or b == c or a == c:
        print("треугольник - равнобедренный")
    else:
        print("треугольник - разносторонний")
else:
    print("Треугольник не существует")


'''
Задание 2
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

print('\nЗадание 2\n')
limit = 100000

while True:
    input_number = int(input("Введите целое число: "))
    if input_number < 0 or input_number > limit:
        print("Введите число в диапазоне от 0 до 100000")
    else:
        break

if input_number == 0 or input_number == 1:
    print("число", input_number, "является ни простым ни составным")
else:
    count = 0
    for i in range(1, input_number):
        if input_number % i == 0:
            count += 1
    if count >= 3:
        print("число", input_number, "является составным")
    else:
        print("число", input_number, "является простым")


'''
Задание 3
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать «больше» или «меньше» после каждой попытки.
'''

print('\nЗадание 3\n')
from random import randint

lower_limit = 0
upper_limit = 1000
number_attempts = 10

while True:
    num_user = int(input("загадайте число: "))
    if num_user < lower_limit or num_user > upper_limit:
        print("Введите число в диапазоне от ", lower_limit, "до ", upper_limit)
    else:
        break

# решение задачи способ 1
print('\nЗадание 3, способ 1\n')
counter_1 = 0

while counter_1 < number_attempts:
    counter_1 += 1
    num_bot = randint(lower_limit, upper_limit)
    print("попытка №", counter_1, "от бота  число: ", num_bot)
    if num_bot == num_user:
        print("бот угодал число с количеством попыток: ", counter_1)
        break
    elif num_bot > num_user:
        print("загаданное число меньше")
        upper_limit = num_bot - 1
    else:
        print("загаданное число больше")
        lower_limit = num_bot + 1
else:
    print("попытки бота исчерпаны, бот не угодал число")
    counter_1 = -1


#  решение задачт способ 2
print('\nЗадание 3, способ 2\n')
counter_2 = 0
num_bot = randint(lower_limit, upper_limit)

while counter_2 < number_attempts:
    counter_2 += 1

    print("попытка №", counter_2, "от бота  число: ", num_bot)
    if num_bot == num_user:
        print("бот угодал число с количеством попыток: ", counter_2)
        break
    elif num_bot > num_user:
        print("загаданное число меньше")
        upper_limit = num_bot
        num_bot = (lower_limit + upper_limit) // 2
    else:
        print("загаданное число больше")
        lower_limit = num_bot
        num_bot = (lower_limit + upper_limit) // 2
else:
    print("попытки бота исчерпаны, бот не угодал число")
    counter_2 = -1


# сравнение способов 1 и 2 решения задачи 3
print("\nсравнение двух способов угадывания числа, какой лучше?\n")
if counter_1 == -1 and counter_2 == -1:
    print("в обоих способах попытки исчерпаны, число не угадано")
elif counter_2 > counter_1:
    if counter_1 == -1:
        print("способ 2 лучше ")
    else:
        print("способ 1 лучше")
elif counter_2 < counter_1:
    if counter_2 == -1:
        print("способ 1 ")
    else:
        print("способ 2 лучше")
else:
    print("способы 1 и 2 одинаково сработали")