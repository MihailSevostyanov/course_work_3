from bank_operations import sort_last_5_operations, card_chek, codify_card_number
from datetime import datetime


def main():
    sorted_list = sort_last_5_operations()
    for operation in sorted_list:
        """
        Вытягиваю сразу дату в нужном формате для дальнейшего использования
        """
        struct_time = datetime.strptime(str(operation['date'].split('T')[0]), '%Y-%m-%d')
        get_date = struct_time.strftime('%d.%m.%Y')
        operation_to = card_chek(operation['id'])
        operation_from = codify_card_number(operation['id'])
        if 'from' not in operation:
            print(
                f"{get_date} {operation['description']}\n{operation_to}\n{operation['operationAmount']['amount']}, {operation['operationAmount']['currency']['name']}\n"
            )
        else:
            print(
                f"{get_date} {operation['description']}\n{operation_from} -> {operation_to}\n{operation['operationAmount']['amount']}, {operation['operationAmount']['currency']['name']}\n"
            )


if __name__ == '__main__':
    main()
