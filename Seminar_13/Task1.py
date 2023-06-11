'''
Задание №1
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
'''

#1 вариант решения
def get_number(massage: str) -> int | float:
    while True:
        num = input(massage)
        try:
            return int(num)
        except ValueError as e:
            try:
                return float(num)
            except ValueError as e:
                print ("Неверный формат ввода\n")

def get_number_2():
    while True:
        num = input("введите число")
        try:
            res = int(num)
            print(res)
            break
        except:
            print("Неверный форматввода")



if __name__ == '__main__':
    print("Число на вывод: ", get_number("введите целое число\n"))
    get_number_2()



