import datetime

import pandas_datareader.data as web

from zipline.api import order_target, record, symbol, history, set_commission, commission
from zipline.algorithm import TradingAlgorithm

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


def initialize(context):
    set_commission(commission.PerDollar(cost=0.00165))


def handle_data(context, data):
    sym = symbol('GS')
    order_target(sym, 1)

start = datetime.datetime(2016, 6, 1)
end = datetime.datetime.now() - datetime.timedelta(3)
data = web.DataReader("078930.KS", "yahoo", start, end)
data = data[['Adj Close']]
data.columns = ["GS"]
data = data.tz_localize("UTC")

algo = TradingAlgorithm(capital_base=100000000, initialize=initialize, handle_data=handle_data)
results = algo.run(data)
print(results[['starting_cash', 'ending_cash', 'ending_value']].head())

results[['starting_cash', 'ending_cash', 'ending_value']].plot()
plt.legend(loc='best')
plt.grid()
plt.show()
