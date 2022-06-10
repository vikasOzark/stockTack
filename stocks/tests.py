from pandas import DataFrame
import pandas as pd
import numpy as np

read = pd.read_excel('/home/vikas/Desktop/test.ods', engine='odf')

print(read['Date'])