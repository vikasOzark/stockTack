import requests

def get_headlines():
    API_KEY='55b47185930f4563a3c20cd775b10fd1'
    url = f'https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=20&page=2&apiKey={API_KEY}'

    response = requests.get(url)
    return response.json()