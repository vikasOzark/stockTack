from django.http import JsonResponse
from idna import valid_contextj
import requests
import datetime

def get_stock_search(search_value, date_from=None, date_to=None):
    try:
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={ search_value }&apikey=2S3HAXUPTY554T7C'
        response = requests.get(url).json()
        symbol = response.get('bestMatches')[0].get('1. symbol')
        
        previous_date = datetime.datetime.today() - datetime.timedelta(days=1)
        previous_date = previous_date.strftime('%Y-%m-%d')

        url = f'https://api.polygon.io/v1/open-close/{ symbol }/{ previous_date }?adjusted=true&apiKey=U7mOPE6UZjmXOUDzWC84pNWz1hwJTDeC'
        response = requests.get(url).json()

        print(response)
        return response
        
    except:
        return 'NOT_FOUND'


# url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=demo'
# response = requests.get(url).json()
# print(response)