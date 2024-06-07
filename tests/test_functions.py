import pytest

from src.functions import mask_card_number, date_form, get_from_card


def test_mask_card_number():
    assert mask_card_number('1308795367077170') == '1308 79** **** 7170'
    assert mask_card_number('96527012349577388612') == '**8612'


def test_date_form():
    assert date_form('2019-07-13T18:51:29.313309') == '13.07.2019'

def test_get_from_card():
    assert get_from_card('Счет 71687416928274675290') == ['Счет', '71687416928274675290']





