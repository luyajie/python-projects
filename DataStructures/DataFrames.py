#!/usr/bin/python3.6

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print ('-------------------------------------')
file1_path = os.path.expanduser('~/Documents/data/files/file1.csv')
file2_path = os.path.expanduser('~/Documents/data/files/file2.csv')

def get_missing_price(df_in, col_name):
    max_depth = df_in[col_name].index
    print('ddd : ' + str(type(max_depth)))
    idx = 1
    while (idx - max_depth).any():
        df_tmp = df_in[col_name].shift(idx)
        if not df_tmp[col_name].isnull():
            return df_tmp[col_name]
        idx = idx + 1



# read file1
cols_to_read = ['time', 'ask', 'bid']
dates_col = ['time']
dtypes = {'bid': 'float', 'ask': 'float'}
df_file1 = pd.read_csv(file1_path, sep=',', header=0, usecols=cols_to_read, dtype=dtypes, parse_dates=dates_col)

print(df_file1['ask'].index[2])
# print(df_file1)

df_file1.set_index('time', inplace=True)

# print(df_file1['ask'])
df_file1['ask'] = np.where(df_file1['ask'].isnull(), get_missing_price(df_file1, 'ask'), df_file1['ask'])

# print(df_file1)

