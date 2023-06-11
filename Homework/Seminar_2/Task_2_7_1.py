
'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''
import fractions

print("Задача 2 'Перевод из десятичной в систему исчисления с основанием от 2 до 16'")

number = int(input("введите целое число\n"))
base = int(input("введите основание системы счисления, в которую надо перевести число\n"))
num = abs(number)
number_new = ''


# while num:
#     if num % base == 10:
#         num_char = 'A'
#     elif num % base == 11:
#         num_char = 'B'
#     elif num % base == 12:
#         num_char = 'C'
#     elif num % base == 13:
#         num_char = 'D'
#     elif num % base == 14:
#         num_char = 'E'
#     elif num % base == 15:
#         num_char = 'F'
#     else:
#         num_char = str(num % base)
#     number_new = num_char + number_new
#     num //= base

str_ = "0123456789abcdef"
while num:
    num_char = str_[num % base]

    number_new = num_char + number_new
    num //= base
    print(f' {num_char=}   {num=}   {number_new=}')


if number < 0:
    number_new = "-" + number_new
if number == 0:
    number_new = "0"

print(f'          Число {number} в {base}-ой системе счисления = {number_new}')
print(f'Проверка: число {number} в 16-ой системе счисления = {hex(number)}')