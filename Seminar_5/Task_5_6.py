'''Задание №6
✔ Выведите в консоль таблицу умножения
от 2х2 до 9х10 как на школьной тетрадке.
✔ Таблицу создайте в виде однострочного
генератора, где каждый элемент генератора —
отдельный пример таблицы умножения.
✔ Для вывода результата используйте «принт»
без перехода на новую строку
'''

# 1 вариант
my_gen = (f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(2, 12))
my_gen_1 = (f'\n' if j == 6 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(2, 7))
my_gen_2 = (f'\n' if j == 11 else f' {j}*{i}={i * j:2d} ' for i in range(2, 10) for j in range(6, 12))
print(*my_gen)
print(*my_gen_1)
print(*my_gen_2)

#2 вариант
min_num = 2
max_num = 10
column = 4

[[print(f'{k:>} * {j:>2} = {k * j:>2}\n\n', end='') if (j == max_num and k == i + column - 1)
  else print(f'{k:>} * {j:>2} = {k * j:>2}\n', end='') if k == i + column - 1
else print(f'{k:>} * {j:>2} = {k * j:>2}\t\t', end='') for k in range(i, i + column)]
 for i in range(min_num, max_num, column) for j in range(min_num, max_num + 1)]
