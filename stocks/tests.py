from .news import get_headlines

headlines_get = get_headlines()
headlines = headlines_get['articles'][0]
headlines2 = headlines_get['articles'][1]

news_list = []

for news in range(len(headlines_get['articles'])):
    news_list.append(headlines_get['articles'][news])

print(news_list)