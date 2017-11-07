#!/usr/bin/python3.6

from dateutil import parser
import os
import pandas as pd
import matplotlib.pyplot as plt


print ('-------------------------------------')
# ig_file_path = 'E:\\data\\PMS\\pm-hack\\FxFeedMergeInIG.csv'
# pl_file_path = 'E:\\data\\PMS\\pm-hack\\FxFeedMergeInPLUS500.csv'
# fm_file_path = 'E:\\data\\PMS\\pm-hack\\FxFeedMergeOut_201711020800.csv'

ig_file_path = os.path.expanduser('~/Documents/data/files/FxFeedMergeInIG.csv')
pl_file_path = os.path.expanduser('~/Documents/data/files/FxFeedMergeInPLUS500.csv')
fm_file_path = os.path.expanduser('~/Documents/data/files/FxFeedMergeOut_201711020800.csv')

# ig
cols_to_read = ['receivedAt', 'bid', 'ask']
dates_col = ['receivedAt']
dtypes = {'bid': 'float', 'ask': 'float'}
df_ig = pd.read_csv(ig_file_path, sep=',', header=0, usecols=cols_to_read, dtype=dtypes, parse_dates=dates_col)

# pl
cols_to_read = ['receivedAt', 'bid', 'ask']
dates_col = ['receivedAt']
dtypes = {'bid': 'float', 'ask': 'float'}
df_pl = pd.read_csv(pl_file_path, sep=',', header=0, usecols=cols_to_read, dtype=dtypes, parse_dates=dates_col)

# fm
cols_to_read = ['PublishedAt', 'Bid', 'Ask']
dates_col = ['PublishedAt']
dtypes = {'Bid': 'float', 'Ask': 'float'}
df_fm = pd.read_csv(fm_file_path, sep=',', header=0, usecols=cols_to_read, dtype=dtypes, parse_dates=dates_col)


# set time column as index
df_ig.set_index('receivedAt', inplace=True)
df_pl.set_index('receivedAt', inplace=True)
df_fm.set_index('PublishedAt', inplace=True)

df_final = df_ig.join(df_pl, lsuffix='_ig', rsuffix='_pl', how='outer').join(df_fm, lsuffix='_ig11', rsuffix='_fm', how='outer')

# print(df_final)

# plot IG
# simple plot
ig_chart = df_ig.plot(title='IG prices', lw=1, marker='.', markersize=10)
ig_chart.set_xlabel("Received At (local time)")
ig_chart.set_ylabel("Prices (GBP)")

# plot with legend
# df_ig_data = {'ig_bid': df_ig['bid'], 'ig_ask': df_ig['ask']}
# df_ig_new = pd.DataFrame(df_ig_data)
# df_ig_new.plot()


# plot all in one chart
# all_data = {'ig_bid': df_ig['bid'], 'ig_ask': df_ig['ask']
#    , 'pl_bid': df_pl['bid'], 'pl_ask': df_pl['ask']
#    , 'fm_bid': df_fm['Bid'], 'fm_ask': df_fm['Ask']}
#all_df = pd.DataFrame(all_data)
#all_df.plot()

plt.show()
