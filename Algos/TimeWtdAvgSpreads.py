#!/usr/bin/python3.6

import os
import numpy as np
import pandas as pd


out_file_name = os.path.expanduser('~/Documents/data/csv_files/random_prices.csv')

dates_col = ['Time']
#headers = ['Time', 'Bid', 'Ask']
#dtypes = {'Time': 'str', 'Bid': 'float', 'Ask': 'float'}
#df = pd.read_csv(out_file_name, sep=',', header=0, names=headers, dtype=dtypes, parse_dates=dates_col)
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
# df['diff_time'] = df['diff_time'].astype('timedelta64[ms]')

# 2 - use numpy type
df['diff_time'] = df['diff_time'].astype(np.int64) / 10**6

df['time_weighted'] = df['diff_time'] * df['diff_px']

sum_px = df['time_weighted'].sum()
sum_times = df['diff_time'].sum()

twa_px = sum_px / sum_times

print('sum_px: ' + str(sum_px))
print('sum_times: ' + str(sum_times))
print('twa_px: ' + str(twa_px))
