from django.http import JsonResponse
import requests
import datetime

FINAGE_DOC_API = 'API_KEY990IVF5LZ2UBQUTMHOTFMJ4XSKTICA01'

def previous_date(stock_name):
    try:
        symbol_for_fin = stock_name.replace(' ', '').upper()
        url = url = f'https://api.finage.co.uk/last/stock/in/{symbol_for_fin}?apikey={FINAGE_DOC_API}'
        response = requests.get(url).json()    

        return response

    except:
        return 'NOT_FOUND'
    
def get_data_with_date(search_value, date_from=None, date_to=None):
    # Get the stock price
    symbol_for_fin = search_value.replace(' ', '').upper()
    try:
        url = url = f'https://api.finage.co.uk/agg/stock/global/in/{symbol_for_fin}/1day/{date_from}/{date_to}?apikey={FINAGE_DOC_API}'
        response = requests.get(url).json()
        print(' Response : ',response)
        return response
    except:
        return 'NOT_FOUND'