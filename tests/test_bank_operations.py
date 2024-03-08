from utils import bank_operations



def test_read_operations():
    assert type(bank_operations.read_operations()) == list


def test_sort_operations():
    assert type(bank_operations.sort_operations()) == list


def test_sort_last_5_operations():
    assert type(bank_operations.sort_last_5_operations()) == list


def test_card_chek():
    assert bank_operations.card_chek(863064926) == 'Счет **5907'
    assert bank_operations.card_chek(114832369) == 'Счет **3655'
    assert bank_operations.card_chek(154927927) == 'Счет **2869'
    assert bank_operations.card_chek(482520625) == 'Счет **8125'
    assert bank_operations.card_chek(801684332) == 'Счет **8381'


def test_codify_card_number():
    assert bank_operations.codify_card_number(863064926) == None
    assert bank_operations.codify_card_number(114832369) == 'Visa Classic 2842 87** **** 9012'
    assert bank_operations.codify_card_number(154927927) == 'Maestro 7810 84** **** 5568'
    assert bank_operations.codify_card_number(482520625) == 'Счет **9794'
    assert bank_operations.codify_card_number(801684332) == None


