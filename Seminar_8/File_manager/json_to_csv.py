'''
Задание №3
Напишите функцию, которая сохраняет созданный в
прошлом задании файл в формате CSV.

'''
import csv
import json
import os
from pathlib import Path


def json_to_csv(json_file, csv_file) -> None:
    if os.path.isfile(Path.cwd() / json_file ):                 #проверка на наличие файла
        with open(json_file, 'r', encoding='utf-8') as js:
            if os.path.getsize(json_file) > 0:
                json_dict = json.load(js)
    else:
        print(f'Файл {json_file} не найден')
        return

    list_row = []
    for level, value in json_dict.items():
        for id, name in value.items():
            list_row.append({'level': level, 'user_id': id, 'name': name})          #список словарей

    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']               # заголовок таблицы
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()                                    #сохранение первой строки с заголовком
        writer.writerows(list_row)                              #ссохранение списка сдоварей в формате csv в файл

    print(f'данные сконвертированы с {json_file} в {csv_file}')


