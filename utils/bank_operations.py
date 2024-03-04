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

