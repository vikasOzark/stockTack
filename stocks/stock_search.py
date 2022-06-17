from django.http import JsonResponse
import requests
import datetime

def get_stock_search(search_value, date_from=None):
    API_KEY_polygon =  'U7mOPE6UZjmXOUDzWC84pNWz1hwJTDeC'
    API_KEY_alphavantage = '2S3HAXUPTY554T7C'

    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ search_value }&apikey={API_KEY_alphavantage}'
    response = requests.get(url).json()
    symbol = response.get('bestMatches')[0].get('1. symbol')
    
    previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
    previous_date = previous_date.strftime('%Y-%m-%d')
            
    
    if date_from is not None:
        try:
            url = f'https://api.polygon.io/v1/open-close/{symbol}/{date_from}?adjusted=true&apiKey={API_KEY_polygon}'
            response = requests.get(url).json()
            return response
        except:
            return 'NOT_FOUND from date is no none'
    else:
        try:
            url = f'https://api.polygon.io/v1/open-close/{symbol}/{previous_date}?adjusted=true&apiKey={API_KEY_polygon}'
            response = requests.get(url).json()            
            return response
        except:
            return 'NOT_FOUND'

