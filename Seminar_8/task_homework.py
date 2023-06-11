'''
Напишите функцию, которая получает на вход директорию и рекурсивно
обходит её и все вложенные директории. Результаты обхода сохраните в
файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций
пакет для работы с файлами разных форматов.

'''

import json
import csv
import pickle
import os
from pathlib import Path


def jsn_writer(data_dict: dict, path: str, file_name: str) -> None:                             #запись словаря в json файл
    file_path = os.path.join(path, file_name + '.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=4)


def csv_writer(data_dict: dict, path: str, file_name: str) -> None:                             #запись словаря в csv файл
    file_path = os.path.join(path, file_name + '.csv')
    data = [['Path', 'object_type',  'object_name', 'object_size', 'parant_directory']]
    for key, value in data_dict.items():
        data.append([key, *value.values()])
    print(data)

    with open(file_path, 'w', encoding='utf-8') as f:
        write_csv = csv.writer(f, dialect='excel', delimiter=' ')
        write_csv.writerows(data)


def pcl_writer(data_dict: dict, path: str, file_name: str) -> None:                                #запись словаря в pickle файл
    file_path = os.path.join(path, file_name + '.pickle')
    with open(file_path, 'wb') as f:
        pickle.dump(data_dict, f)


def dct_formatter1(total_dct: dict[str, dict[str]], path: str, item_name: str, item_type: str) -> None:
    if item_type == 'F':
        total_dct[path] = dict(object_type='File',
                               object_name=item_name,
                               object_size=os.path.getsize(os.path.join(path, item_name)),
                               parant_directory=os.path.split(path)[-1])
    elif item_type == 'D':
        total_dct[path] = dict(object_type='Directory',
                               object_name=item_name,
                               object_size=count_size(os.path.join(path, item_name)),
                               parant_directory=os.path.split(os.path.abspath(path))[-1])
    else:
        pass


def count_size(count_path: str, dir_size: int = 0) -> float:
    for sub_item in os.walk(count_path):

        if sub_item[2]:
            dir_size += sum([os.path.getsize(os.path.join(sub_item[0], file))for file in sub_item[2]])  # размер всех файлов в директории

        if sub_item[1]:
            dir_size += sum([count_size(os.path.join(sub_item[0], subdir))for subdir in sub_item[1]])

    return dir_size


def dir_walker(aim_path: str, total_dct: dict = None) -> dict[str, dict[str]]:
    if total_dct is None:
        total_dct = {}
        basic_path = os.path.split(os.path.abspath(aim_path))                                           #('C:\\Users\\Алексей\\Desktop\\GreekBrains\\СЕМИНАРЫ\\Python_advanced', 'Seminar_8')

        dct_formatter1(total_dct, os.path.join(*basic_path[:-1]), basic_path[-1], 'D')


    for item in os.listdir(aim_path):
        check_path = os.path.join(aim_path, item)
        if os.path.isfile(check_path):
            dct_formatter1(total_dct, aim_path, item, 'F')
        elif os.path.isdir(check_path):
            dct_formatter1(total_dct, aim_path, item, 'D')
            dir_walker(os.path.join(aim_path, item), total_dct)
    return total_dct


# def dict_printer(in_dict: dict) -> None:
#     for i_key, i_val in sorted(in_dict.items()):
#         print(i_key, end=':')
#         if isinstance(i_val, dict):
#             print()
#             dict_printer(i_val)
#         else:
#             print('\t', i_val)


def main():

    tst_path = str(Path.cwd()) + '\\'
    #tst_path = '\\Users\\Алексей\\Desktop\\GreekBrains\\СЕМИНАРЫ\\Python_advanced\\Seminar_8\\'

    result = dir_walker(tst_path)
    jsn_writer(result, os.getcwd(), 'result1')
    pcl_writer(result, os.getcwd(), 'result1')
    csv_writer(result, os.getcwd(), 'result1')
    # dict_printer(result)


if __name__ == '__main__':
    main()

