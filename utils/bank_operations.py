import json


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
    stocks = sort_operations()
    stocks_sorted = sorted(stocks, key=lambda x: x['date'], reverse=True)
    return stocks_sorted[:5]












