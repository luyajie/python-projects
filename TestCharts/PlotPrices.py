#!/usr/bin/python3.6

import os
import pandas as pd
import matplotlib.pyplot as plt


print ('-------------------------------------')
data_file_path = os.path.expanduser('~/Documents/data/csv_files/random_prices.csv')

cols_to_read = ['Time', 'Bid', 'Ask']
dates_col = ['Time']
dtypes = {'Bid': 'float', 'Ask': 'float'}
df = pd.read_csv(data_file_path, sep=',', header=0, usecols=cols_to_read, dtype=dtypes, parse_dates=dates_col)

df['Mid'] = (df['Ask'] + df['Bid']) * 0.5

# set time column as index
df.set_index('Time', inplace=True)

print(df)

marker_char = '.'
# simple plot
chart = df.plot(title='Security price (steps)', lw=1, marker=marker_char, markersize=10, drawstyle="steps-post")
chart.set_xlabel("Received At (local time)")
chart.set_ylabel("GBP")

df2 = df
chart = df2.plot(title='Security price', lw=1, marker=marker_char, markersize=10)
chart.set_xlabel("Received At (local time)")
chart.set_ylabel("GBP")

plt.show()
