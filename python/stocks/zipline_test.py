import datetime

import pandas_datareader.data as web

from zipline.api import order, symbol
from zipline.algorithm import TradingAlgorithm

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 1)


start = datetime.datetime(2013, 1, 1)
end = datetime.datetime.now() - datetime.timedelta(3)
data = web.DataReader("AAPL", "yahoo", start, end)

data = data[['Adj Close']]
data.columns = ["AAPL"]
data = data.tz_localize("UTC")
algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
results = algo.run(data)

plt.plot(data.index, results.ending_cash, label='ending_cash')
plt.plot(data.index, results.ending_value, label='ending_value')
plt.plot(data.index, results.portfolio_value, label='portfolio_value')
plt.legend(loc='best')
plt.grid()
plt.show()
