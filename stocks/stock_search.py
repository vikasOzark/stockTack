from django.http import JsonResponse
import requests
import datetime

API_KEY_polygon =  'U7mOPE6UZjmXOUDzWC84pNWz1hwJTDeC'
API_KEY_alphavantage = '2S3HAXUPTY554T7C'

def get_symbol(stock_name):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ stock_name }&apikey={API_KEY_alphavantage}'
    response = requests.get(url).json()
    symbol = response.get('bestMatches')[0].get('1. symbol')
    return symbol

def previous_date(stock_name):
    symbol = get_symbol(stock_name)
    try:
        url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={API_KEY_polygon}'
        response = requests.get(url).json()    

        print('response : ', response)      
        return response

    except:
        return 'NOT_FOUND'

def get_stock_search(search_value, date_from=None):
    symbol = get_symbol(search_value)

    previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    previous_date = previous_date.strftime('%Y-%m-%d')

    if date_from is not None:
        try:
            url = f'https://api.polygon.io/v1/open-close/{symbol}/{date_from}?adjusted=true&apiKey={API_KEY_polygon}'
            response = requests.get(url).json()
            return response
        except:
            return 'NOT_FOUND'
    else:
        try:
            url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?adjusted=true&apiKey={API_KEY_polygon}'
            response = requests.get(url).json()    

            print('response : ', response)      
            return response
        except:
            return 'NOT_FOUND'

