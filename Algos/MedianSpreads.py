#!/usr/bin/python3.6

import os
import numpy as np
import pandas as pd


out_file_name = os.path.expanduser('~/Documents/data/csv_files/random_prices.csv')

df = pd.read_csv(out_file_name, sep=',')
df['diff_px'] = df['Ask'] - df['Bid']
median = df['diff_px'].median()

print('median: ' + str(median))
