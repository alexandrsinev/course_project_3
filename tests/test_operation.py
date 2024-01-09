from utils.operation import get_list, remove_bad_dictionary, sorted_list, get_new_list

import json

from pathlib import Path

def test_get_list():
    file = Path('..', 'operations.json')
    with open(file, encoding='UTF-8') as j_file:
        file_info = json.load(j_file)
    for i in file_info:
        assert type(i) == dict
    assert type(get_list()) == list


l_file = get_list()

new_l_file = remove_bad_dictionary(l_file)



s_list = sorted_list(new_l_file)


def test_get_new_list():
    assert len(get_new_list(s_list)) == 5
    assert get_new_list(s_list) == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
                                     'operationAmount': {'amount': '41096.24',
                                                         'currency': {'name': 'USD', 'code': 'USD'}},
                                     'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
                                    {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890',
                                     'operationAmount': {'amount': '48150.39',
                                                         'currency': {'name': 'USD', 'code': 'USD'}},
                                     'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012',
                                     'to': 'Счет 35158586384610753655'},
                                    {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
                                     'operationAmount': {'amount': '30153.72',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод организации', 'from': 'Maestro 7810846596785568',
                                     'to': 'Счет 43241152692663622869'},
                                    {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051',
                                     'operationAmount': {'amount': '62814.53',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794',
                                     'to': 'Счет 46765464282437878125'},
                                    {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725',
                                     'operationAmount': {'amount': '21344.35',
                                                         'currency': {'name': 'руб.', 'code': 'RUB'}},
                                     'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]
