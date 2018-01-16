import datetime

import pandas_datareader.data as web

from zipline.api import order_target, record, symbol, history
from zipline.algorithm import TradingAlgorithm

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def initialize(context):
    context.i = 0
    context.investment = False


def handle_data(context, data):
    context.i += 1
    if context.i < 20:
        return

    ma5 = history(5, '1d', 'price').mean()
    ma20 = history(20, '1d', 'price').mean()
    buy = False
    sell = False

    sym = symbol("AAPL")
    if ma5[sym] > ma20[sym] and context.investment is False:
        order_target(sym, 100)
        context.investment = True
        buy = True
    elif ma5[sym] < ma20[sym] and context.investment is True:
        order_target(sym, -100)
        context.investment = False
        sell = True

    record(AAPL=data[sym].price, ma5=ma5[sym], ma20=ma20[sym], buy=buy, sell=sell)

start = datetime.datetime(2013, 1, 1)
end = datetime.datetime.now() - datetime.timedelta(3)
data = web.DataReader("AAPL", "yahoo", start, end)
data = data[['Adj Close']]
data.columns = ["AAPL"]
data = data.tz_localize("UTC")

algo = TradingAlgorithm(initialize=initialize, handle_data=handle_data)
results = algo.run(data)
print(results['portfolio_value'].tail())

results[['ma5', 'ma20']].plot()
# plt.plot(data.index, results.ma5, label='ma5')
# plt.plot(data.index, results.ma20, label='ma20')
# plt.plot(data.index, results.ending_cash, label='ending_cash')
# plt.plot(data.index, results.ending_value, label='ending_value')
# plt.plot(data.index, results.portfolio_value, label='portfolio_value')
plt.plot(results.ix[results.buy == True].index, results.ma5[results.buy == True], '^')
plt.plot(results.ix[results.sell == True].index, results.ma5[results.sell == True], 'v')
plt.legend(loc='best')
plt.grid()
plt.show()
