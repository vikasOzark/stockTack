import pandas as pd
import numpy as np

file_path = '/home/vikas/Desktop/Book.xlsx'

df = pd.read_excel(io=file_path, sheet_name=0)
print('====> :',df['A']) 

