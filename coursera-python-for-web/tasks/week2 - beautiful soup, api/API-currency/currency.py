from bs4 import BeautifulSoup
from decimal import Decimal
import sys


def str_to_decimal(string):
    """Преобразование строки в Decimal"""
    return Decimal(string.replace(',', '.'))


def get_single_value(values, code):
    """Получение стоимости в рублях одной единицы валюты с заданным кодом"""
    result = None
    for v in values:
        if v.charcode.text == code:
            value = str_to_decimal(v.value.text)
            nominal = str_to_decimal(v.nominal.text)
            result = value / nominal
            break
    return result


def convert(amount, cur_from, cur_to, date, requests):
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    # sys.stdout.buffer.write(soup.prettify().encode('utf-8'))

    values = list(soup.html.body.valcurs.children)

    result = None
    if cur_from == 'RUR':
        value_to = get_single_value(values, cur_to)
        result = round(amount / value_to, 4)
    else:
        value_from = get_single_value(values, cur_from)
        value_to = get_single_value(values, cur_to)
        result = round(amount * (value_from / value_to), 4)

    return result  # не забыть про округление до 4х знаков после запятой
