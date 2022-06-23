import requests

def get_headlines():
    API_KEY='55b47185930f4563a3c20cd775b10fd1'
    url = f'https://newsapi.org/v2/top-headlines?country=in&category=business&pageSize=4&page=2&apiKey={API_KEY}'

    response = requests.get(url)
    return response.json()


v= [{'source': {'id': None, 'name': 'Hindustan Times'}, 'author': 'HT Auto Desk', 'title': '2022 Kawasaki Ninja 400 India launch tomorrow: Price expectation - HT Auto', 'description': 'The Ninja 400 will be re-introduced in India on June 24th in an updated BS 6-spec avatar.', 'url': 'https://auto.hindustantimes.com/auto/two-wheelers/2022-kawasaki-ninja-400-india-launch-tomorrow-price-expectation-41655957956573.html', 'urlToImage': 'https://images.hindustantimes.com/auto/img/2022/06/23/1600x900/Untitled_1620744549128_1655962204910.jpg', 'publishedAt': '2022-06-23T05:48:51Z', 'content': 'After teasing the motorcycle previously on social media, Kawasaki has now announced the launch date of the Ninja 400 which will go on sale in India tomorrow (June 24th). The Ninja 400 will be re-intr… [+1768 chars]'}]

print(v[0]['title'])
