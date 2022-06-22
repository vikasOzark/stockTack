# import csv
# import requests

# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=TTM&interval=15min&slice=year1month1&apikey= 2S3HAXUPTY554T7C'

# with requests.Session() as s:
#     download = s.get(CSV_URL)
#     decoded_content = download.content.decode('utf-8')
#     cr = csv.reader(decoded_content.splitlines(), delimiter=',')
#     my_list = list(cr)
#     for row in my_list:
#         print(row)

i  = {
    'hello': 'world',
    'dic2': {
        'hello in dits2': 'world in idct',
    }
}

i['dic2']

print(i)