#!/usr/bin/python3.6

import os
import numpy as np
import pandas as pd


out_file_name = os.path.expanduser('~/Documents/data/csv_files/random_prices.csv')

dates_col = ['Time']
df = pd.read_csv(out_file_name, sep=',', parse_dates=dates_col)
df['diff_px'] = df['Ask'] - df['Bid']
df['diff_time'] = df['Time'].shift(-1) - df['Time']


# three ways to drop na
# 1 - explicit check for na
#df = df[df.diff_time.notnull()]

# 2 - assign return of dropna to same dataframe
#df =  df.dropna()

# 3 - set inplace=True
df.dropna(inplace=True)


# two ways to convert timedelta to milliseconds
# 1 - use built-in cast
df['diff_time'] = df['diff_time'].astype('timedelta64[ms]')

# 2 - use numpy type
# df['diff_time'] = df['diff_time'].astype(np.int64) / 10**6

# print(df['diff_px'])
# print(df['diff_time'])


# get sum of times
sum_times = df['diff_time'].sum()

# get time percentage
df['diff_time'] = df['diff_time'] / sum_times

# sort based on price
df = df.sort_values(['diff_px'], ascending=True)

print(df)
