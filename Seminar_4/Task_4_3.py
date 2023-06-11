'''Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.'''

def string_to_dict(nums: str) -> dict[str, int]:

    start, stop = map(int, nums.split())
    if start > stop:
        start, stop = stop, start
    res = {}

    for i in range(start, stop+1):
        res[chr(i)] = i

    return res

print(string_to_dict("65 97"))
print(string_to_dict("97 65"))