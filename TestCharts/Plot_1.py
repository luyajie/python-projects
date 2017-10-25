#!/usr/bin/python3.6

import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

#matplotlib.style.use('ggplot')

#ts = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
print(ts)

ts1 = ts.cumsum()
ts.plot()
ts1.plot()


d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two' : pd.Series([2., 2.1, 2.1, 5.], index=['a', 'b', 'c', 'd'])}
#d = {'one' : pd.Series([1., 2., 3.], index=[1, 2, 3]), 'two' : pd.Series([1., 2., 3., 4.], index=[1, 2, 3, 4])}
df = pd.DataFrame(d)
print(df)

pd.DataFrame(d).assign(SepalRatio = lambda x: 1 / 2, PetalRatio = lambda x: 1 / 2).plot(kind='scatter', x='SepalRatio', y='PetalRatio')
#pd.DataFrame(d).plot(kind='line')


angles = [a/20 for a in range(200)]
print(angles)
sine = [math.sin(x) for x in angles]
cos = [math.cos(x) for x in angles]

d1 = {'sine' : pd.Series(sine, index=angles), 'cosine' : pd.Series(cos, index=angles)}
df1 = pd.DataFrame(d1)
df1.plot()

plt.show()
