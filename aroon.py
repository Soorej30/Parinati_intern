import requests
import time
import datetime
import json
import numpy as np
import talib
import matplotlib.pyplot as plt

class get_data_from_binance:
    def __init__(self):
        self.url_used= "https://api.binance.com/api/v1/klines?symbol=BTCUSDT&interval=1d&limit=180"
        
    def get_data(self):
        function_received=requests.get(self.url_used)
        return function_received.json()


class AroonOscillator:
    def __init__(self, high, low, time_period):
        self.values = talib.AROONOSC( high, low, timeperiod = time_period)

    def get_values(self):
        return self.values

binance_data = get_data_from_binance()
data_received=binance_data.get_data()


btc_high = np.array(data_received)[:, 2].copy().astype(np.float)
btc_low = np.array( data_received)[:, 3].copy().astype(np.float)

aroon_values = AroonOscillator(btc_high, btc_low, 25).get_values()

plt.plot(aroon_values, 'ro',aroon_values, 'g--')
plt.ylabel('Aroon values')
plt.xlabel('Days')
plt.show()

