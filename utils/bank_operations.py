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










