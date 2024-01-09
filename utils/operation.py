from datetime import datetime

import json

from pathlib import Path


def get_list():
    file = Path('..', 'operations.json')
    """Функция получает список словарей из json-файла"""
    with open(file, encoding='UTF-8') as j_file:
        file_info = json.load(j_file)

        return file_info


l_file = get_list()


def remove_bad_dictionary(l_file):
    """Удаляет словарь не имеющий ключа 'date' из списка"""
    for i in range(len(l_file)):
        if 'date' not in l_file[i - 1].keys():
            del l_file[i - 1]
        continue
    return l_file


new_l_file = remove_bad_dictionary(l_file)


def sorted_list(new_l_file):
    """Сортирует список по дате начиная с последней по времени"""
    sort_list = sorted(new_l_file, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sort_list


s_list = sorted_list(new_l_file)


def get_new_list(s_list):
    """Получаем список из пяти последних операций со статусом 'EXECUTED'"""
    new_s_list = []
    for i in s_list:
        if i['state'] == 'CANCELED':
            del i
        else:
            new_s_list.append(i)
    return new_s_list[:5]


slaced_list = get_new_list(s_list)


def print_info(slaced_list):
    """Вывод информации по пяти последним операциям"""
    for i in slaced_list:
        amount = i['operationAmount']['amount']
        name_amount = i['operationAmount']['currency']['name']
        print(datetime.strftime(datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f'), '%d.%m.%Y'), i['description'])
        if 'from' not in i:
            encrypted_account = i['to'][:5] + '************' + i['to'][-4:]
            print(f"-> {encrypted_account}")
        elif 'Счет' in i['from']:
            encrypted_account = i['from'][:5] + '************' + i['from'][-4:]
            print(f"{encrypted_account} -> {encrypted_account}")
        else:
            encrypted_number = i['from'][-16:-10] + '******' + i['from'][-4:]
            print(
                f"{i['from'][:-17]} {encrypted_number[:4]} {encrypted_number[4:8]} {encrypted_number[8:12]} {encrypted_number[12:16]} "
                f"-> {i['to'][:5]}************{i['to'][-4:]}")

        print(f"{amount} {name_amount}\n")


print_info(slaced_list)
