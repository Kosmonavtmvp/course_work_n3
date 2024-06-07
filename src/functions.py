import json


def get_txt():
    """Функция чтения файла json"""
    with open('operations.json', encoding='UTF-8') as file:
        return json.load(file)


def date_form(srt_date: str):
    """Форматирование даты в нормальный вид"""
    my_date = srt_date.split('T')[0].split('-')
    return '.'.join(my_date[::-1])


def get_from_card(card: str):
    """Функция перевода строки в список"""
    my_number_card = card.split(' ')
    return my_number_card


def mask_card_number(card_number):
    """Маскировка номера карты или счета"""
    if len(card_number) == 16:
        masked_number = card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]
        return masked_number
    elif len(card_number) >= 20:
        masked_number = '**' + card_number[-4:]
        return masked_number
