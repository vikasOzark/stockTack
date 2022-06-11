from pandas import DataFrame
import pandas as pd
import numpy as np
import requests


API_KEY='U7mOPE6UZjmXOUDzWC84pNWz1hwJTDeC'

url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120&apiKey=U7mOPE6UZjmXOUDzWC84pNWz1hwJTDeC'

response = requests.get(url)
print(response.json())