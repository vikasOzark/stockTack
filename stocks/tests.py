import requests
from stock_search import previous_date
v = 'adani ports'

symbol = v.replace(' ', '').upper()


print(previous_date(symbol)['price'])

