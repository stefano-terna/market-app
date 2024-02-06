# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 17:17:04 2023

@author: A393167
"""

import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl
import trade_functions as fn

### DOWNLOAD DATI
data_stocks = yf.download("aapl msft goog", period='20y')
data_etf=yf.download("SPY",period='20y')

### ELABORAZIONI
    # APPLE
apple=pd.DataFrame(data_stocks['Adj Close']['AAPL'])
apple['SMA_200']=fn.SMA(apple,200)
apple['BBand_UP_50']=fn.BBand(apple['AAPL'], 50, 2)
apple['BBand_LO_50']=fn.BBand(apple['AAPL'], 50, -2)

# Date di inizio e fine visualizzazione
current_date = datetime.now().date()
start_date=pd.to_datetime('1-1-2020')
end_date=pd.to_datetime(current_date - timedelta(days=1))
### GRAFICI
    # STORICO E DISTRIB PREZZI
fig,ax=plt.subplots(1,2,figsize=(14,6), dpi=100)
ax[0].hist(apple['AAPL'].loc[start_date:end_date],
           bins=80,
           orientation='horizontal',
           alpha=0.7,
           label='AAPL')
ax[0].set_title('Distribuzione prezzi')
ax[0].legend()
ax[1].plot(apple['AAPL'].loc[start_date:end_date],
           label='AAPL')
ax[1].tick_params(labelsize=10)
ax[1].legend()
ax[1].set_ylabel('Adj Closing')
plt.show()

    # GRAFICO APPLE
mpl.rcParams['font.size']=16
plt.figure(figsize=(14,6), 
           dpi=100, )
plt.plot(apple.loc[start_date:end_date],
         )
plt.grid(True, linestyle='--', 
         color='gray', 
         linewidth=0.5)

plt.legend(apple.columns)
plt.show()

