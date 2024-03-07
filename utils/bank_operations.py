import json
from datetime import datetime


def read_operations():
    """
    загружаем список операций из файла
    :return:
    """
    with open('operations.json', "r") as f:
        file = f.read()
        operations = json.loads(file)
    return operations


def sort_operations():
    """
    сортирует список по статусу "EXECUTED"
    :return:
    """
    unsorted_list = read_operations()
    sorted_list = []
    for status in unsorted_list:
        if status == {}:
            continue
        elif status['state'] == 'EXECUTED':
            sorted_list.append(status)
    return sorted_list


def sort_last_5_operations():
    """
    сортирует список и сохраняет последние 5 операций по дате
    :return:
    """
    stocks = sort_operations()
    stocks_sorted = sorted(stocks, key=lambda x: x['date'], reverse=True)
    return stocks_sorted[:5]


def card_chek(id):
    """
    Функция берет операции "to" по id всей операции и возвращает заштфрованные счета
    :param id:
    :return:
    """
    data = sort_last_5_operations()
    for item in data:
        if id == item['id']:
            if 'to' in item:
                card_number = item['to']
                card_number_list = card_number.split()
                for element in card_number_list:
                    if len(element) == 20:
                        return (f"{card_number_list[0]} {'*' * len(card_number_list[1][-6:-4]) + card_number_list[1][-4:]}")


def codify_card_number(id):
    """
    Функция берет номера карты по id из "from" и возвращает заштфрованные номера
    :param id:
    :return:
    """
    data = sort_last_5_operations()
    for item in data:
        if id == item['id']:
            if 'from' not in item:
                pass
            elif 'from' in item:
                card_number = item['from']
                card_number_list = card_number.split()
                for element in card_number_list:
                    if len(element) == 20:
                        return (f"{card_number_list[0]} {'*' * len(card_number_list[1][-6:-4]) + card_number_list[1][-4:]}")
                    elif len(element) == 16 and len(card_number_list) == 3:
                        card_number = item['from'].split()[-1]
                        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
                        chunks, chunk_size = len(private_number), len(private_number) // 4
                        return (f'{card_number_list[0]} {card_number_list[1]} {" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])}')
                    elif len(element) == 16 and len(card_number_list) == 2:
                        card_number = item['from'].split()[-1]
                        private_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
                        chunks, chunk_size = len(private_number), len(private_number) // 4
                        return (f'{card_number_list[0]} {" ".join([private_number[i:i + chunk_size] for i in range(0, chunks, chunk_size)])}')