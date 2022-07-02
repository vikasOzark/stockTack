import requests

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=TATAMOTORS&apikey=2S3HAXUPTY554T7C'
r = requests.get(url)
data = r.json()

print(data)

data = {
    'Symbol': 'TTM',
    'AssetType': 'Common Stock',
    'Name': 'Tata Motors Limited ADR',
    'Description':
    'Tata Motors Limited designs, develops, manufactures and sells a range of motor vehicles. The company is headquartered in Mumbai, India.',
    'CIK': '926042',
    'Exchange': 'NYSE',
    'Currency': 'USD',
    'Country': 'USA',
    'Sector': 'MANUFACTURING',
    'Industry': 'MOTOR VEHICLES & PASSENGER CAR BODIES',
    'Address': '24 HOMI MODY ST, HUTATMA CHOWK, IN',
    'FiscalYearEnd': 'March',
    'LatestQuarter': '2022-03-31',
    'MarketCapitalization': '19812100000',
    'EBITDA': '132671398000',
    'PERatio': 'None',
    'PEGRatio': '0',
    'BookValue': '581.87',
    'DividendPerShare': '0',
    'DividendYield': '0',
    'EPS': '-1.915',
    'RevenuePerShareTTM': '3636.2',
    'ProfitMargin': '-0.0411',
    'OperatingMarginTTM': '0.0075',
    'ReturnOnAssetsTTM': '0.0039',
    'ReturnOnEquityTTM': '-0.212',
    'RevenueTTM': '2784536297000',
    'GrossProfitTTM': '1132875900000',
    'DilutedEPSTTM': '-1.915',
    'QuarterlyEarningsGrowthYOY': '0',
    'QuarterlyRevenueGrowthYOY': '-0.115',
    'AnalystTargetPrice': '33.1',
    'TrailingPE': '-',
    'ForwardPE': '17.12',
    'PriceToSalesRatioTTM': '0.0071',
    'PriceToBookRatio': '3.954',
    'EVToRevenue': '0.0109',
    'EVToEBITDA': '0.115',
    'Beta': '2.083',
    '52WeekHigh': '35.38',
    '52WeekLow': '18.48',
    '50DayMovingAverage': '26.98',
    '200DayMovingAverage': '29.42',
    'SharesOutstanding': '765833000',
    'DividendDate': '2016-08-29',
    'ExDividendDate': '2016-07-14'
}
