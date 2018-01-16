import pandas as pd
import pandas_datareader.data as web

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")
new_gs = gs[gs['Volume'] != 0].copy()
new_gs['MA5'] = pd.rolling_mean(new_gs['Adj Close'], 5)
new_gs['MA20'] = pd.rolling_mean(new_gs['Adj Close'], 20)
new_gs['MA60'] = pd.rolling_mean(new_gs['Adj Close'], 60)
new_gs['MA120'] = pd.rolling_mean(new_gs['Adj Close'], 120)

plt.plot(new_gs.index, new_gs['Adj Close'], label="Adj Close")
plt.plot(new_gs.index, new_gs['MA5'], label="MA5")
plt.plot(new_gs.index, new_gs['MA20'], label="MA20")
plt.plot(new_gs.index, new_gs['MA60'], label="MA60")
plt.plot(new_gs.index, new_gs['MA120'], label="MA120")
plt.legend(loc='best')
plt.grid()
plt.show()
