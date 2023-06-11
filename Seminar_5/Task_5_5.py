'''
Задание №5
✔ Напишите программу, которая выводит
на экран числа от 1 до 100.
✔ При этом вместо чисел, кратных трем,
программа должна выводить слово «Fizz»
✔ Вместо чисел, кратных пяти — слово «Buzz».
✔ Если число кратно и 3, и 5, то программа
должна выводить слово «FizzBuzz».
✔ *Превратите решение в генераторное выражение.
'''

# for i in range (1, 101):
#     if i % 3 == 0 and i %5  == 0: # можно записать как if i % 3 == i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)

my_gen = ("fizzbuzz" if i % 3 == i % 5 == 0 else 'fizz' if i % 3 == 0  else "buzz" if i % 5 == 0 else i for i in range(1, 101))
print(*my_gen)
# for i in my_gen:
#     print(i)
