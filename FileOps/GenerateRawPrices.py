#!/usr/bin/python3.6

import os
import numpy as np
import pandas as pd


out_file_name = os.path.expanduser('~/Documents/data/csv_files/random_prices.csv')
list_size = 100
px_base = 20


date_time_list = pd.date_range('1/10/2017', periods=list_size, freq='s')

bid_px_list = []
ask_px_list = []

np_random = np.random
for index in range(list_size):
    rnd_vals = np_random.random(2)

    bid_px = px_base + min(rnd_vals[0], rnd_vals[1])
    ask_px = px_base + max(rnd_vals[0], rnd_vals[1])

    bid_px_list.append(bid_px)
    ask_px_list.append(ask_px)

#print(bid_px_list)
#print(ask_px_list)

# http://pbpython.com/pandas-list-dict.html
# row oriented - pd.DataFrame.from_records
# column oriented - pd.DataFrame.from_items
merge_lists = [('Time', date_time_list),
               ('Bid', bid_px_list),
               ('Ask', ask_px_list)
              ]

df = pd.DataFrame.from_items(merge_lists)
#print(df)

df.to_csv(out_file_name, sep=',', index=False, index_label='Index')

#ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
#print(ts)
