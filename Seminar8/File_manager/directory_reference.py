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

from pathlib import Path
import csv
import json
import pickle
import os


def dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += dir_size(entry.path)
    return result


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return dir_size(path)


def directory_reference(directory: Path):
    data = {}
    fieldnames = ['object_name', 'path', 'object_size', 'object_type', 'parant_directory']
    rows = []

    with (open('result.json', 'w') as f_json,
            open('result.csv', 'w', newline='', encoding='utf-8') as f_csv,
            open('result.pickle', 'wb') as f_pickle):

        for dir_path, dir_name, file_name in os.walk(directory):
            data.setdefault(dir_path, {})
            for dir in dir_name:
                size = get_size(dir_path + '/' + dir)
                data[dir_path].update({dir: {'object_size': size, 'object_type': 'directory','parant_directory': dir_path.split('\\')[-2]}})
                rows.append({'object_name': dir, 'path': dir_path, 'object_size': size, 'object_type': 'directory', 'parant_directory': dir_path.split('\\')[-2]})
            for i in file_name:
                size = get_size(dir_path + '/' + i)
                data[dir_path].update({i: {'object_size': size, 'object_type': 'file', 'parant_directory': dir_path.split('\\')[-1]}})
                rows.append({'object_name': i, 'path': dir_path, 'object_size': size, 'object_type': 'file', 'parant_directory': dir_path.split('\\')[-1]})
            #print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        json.dump(data, f_json, indent=2)                                                                   # запись в json файл
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()                                                                                #запись словаря заголовка в csv файл
        writer.writerows(rows)                                                                              # Запись словаря в csv файл
        pickle.dump(f'{pickle.dumps(data)}', f_pickle)                                                      #запись словаря в pickle файл


