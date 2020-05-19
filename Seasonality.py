
import panormus.data.bbg as bbg
import datetime as dt
import panormus.utils.chrono as chrono
import pandas as pd
import seaborn as sns
import numpy as np

bbg_client = bbg.BbgClient()

ed = chrono.now()
sd = ed - dt.timedelta(days=2000)

tickers = ['NETHER 2.75 01/47 Corp']

data = bbg_client.get_historical_data(tickers,['BLP_Z_SPRD_MID'],sd,ed)
data.columns = ['d','ticker','value']

data = data.set_index(['d','ticker']).unstack('ticker')
data.columns = data.columns.droplevel()
data.columns.names = ['']
data = data.reset_index()

data = data.set_index('d')

print(data.tail(3))
df = pd.DataFrame(data)


import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 10, 6
import requests, pandas as pd, numpy as np
from pandas import DataFrame
from io import StringIO
import time, json
from datetime import date
import statsmodels
from statsmodels.tsa.stattools import adfuller, acf, pacf
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import mean_squared_error
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


#df2 = data
#df2.reset_index(inplace=True)
#df2 = df2.rename(columns={'d':'ds','USYC1030 Index':'Y'})
#print(df2.head())

#plt.plot(data.index.to_pydatetime(), data.values)
#plt.show()

data_w = data.resample('W').mean()
data_m = data.resample('M').mean()

data_week = data_w['NETHER 2.75 01/47 Corp']
data_month = data_m['NETHER 2.75 01/47 Corp']
plt.plot(data_w.index.to_pydatetime(), data_w.values)
#plt.show()

"""
def check_stationarity(timeseries):
    # Determing rolling statistics
    rolling_mean = timeseries.rolling(window=52, center=False).mean()
    rolling_std = timeseries.rolling(window=52, center=False).std()

    # Plot rolling statistics:
    original = plt.plot(timeseries.index.to_pydatetime(), timeseries.values, color='blue', label='Original')
    mean = plt.plot(rolling_mean.index.to_pydatetime(), rolling_mean.values, color='red', label='Rolling Mean')
    std = plt.plot(rolling_std.index.to_pydatetime(), rolling_std.values, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dickey_fuller_test = adfuller(timeseries, autolag='AIC')
    dfresults = pd.Series(dickey_fuller_test[0:4],
                          index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dickey_fuller_test[4].items():
        dfresults['Critical Value (%s)' % key] = value
    print(dfresults)


#check_stationarity(data_week)
#plt.show()
"""
ts_euro_week_log = data_w

decomposition = seasonal_decompose(data_w)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

Seasonal_score = seasonal.std()/data_week.std()
print(data.std())
print(Seasonal_score)

# Select the most recent weeks
ts_euro_week_log_select = ts_euro_week_log[-364:]



plt.subplot(411)
plt.plot(ts_euro_week_log_select.index.to_pydatetime(), ts_euro_week_log_select.values, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(ts_euro_week_log_select.index.to_pydatetime(), trend[-364:].values, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(ts_euro_week_log_select.index.to_pydatetime(), seasonal[-364:].values,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(ts_euro_week_log_select.index.to_pydatetime(), residual[-364:].values, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.show()


plt.figure()
plt.subplot(211)
Seasonality1=seasonal[seasonal.index.year == 2018]
MA1=Seasonality1.rolling(window=2).mean()
MA2=Seasonality1.rolling(window=6).mean()
plt.plot(Seasonality1, label='Seasonality')
plt.plot(MA1, label='10D MA')
plt.plot(MA2, label='30D MA')
plt.title("Seasonality", fontsize=10, fontweight='bold')
plt.tight_layout()
plt.legend()
plt.subplot(212)
observation = data[-250:]
M_A1=observation.rolling(window=10).mean()
M_A2=observation.rolling(window=23).mean()
plt.plot(observation, label='Current')
plt.plot(M_A1, label='10D MA')
plt.plot(M_A2, label='23D MA')
plt.title("Latest", fontsize=10, fontweight='bold')
plt.tight_layout()
plt.legend()
plt.show()


#data_month['mon'] = data_month.index.month
#print(data_month.head(5))

"""
data_m = data.pct_change().dropna()

data_monthly = data_m.groupby([data_m.index.year.rename('year'), data_m.index.month.rename('month')]).mean()
print(data_monthly.head(10))

from pylab import rcParams
rcParams['figure.figsize'] = 20, 10


Monthly_Returns_List=[]
for i in range(len(data_monthly)):
    Monthly_Returns_List.append({'year':data_monthly.index[i][0],'month':data_monthly.index[i][1],'monthly_Return':data_monthly[i]})

Monthly_Returns_List=pd.DataFrame(Monthly_Returns_List,columns=('year','month','monthly_Return'))

Monthly_Returns_List.boxplot(column='Monthly_Return', by='Month')
ax = plt.gca()
labels = [item.get_text() for item in ax.get_xticklabels()]
labels=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

ax.set_xticklabels(labels)

plt.tick_params(axis='both', which='major', labelsize=15)
plt.show()

"""
data_c = data.pct_change(fill_method='ffill')

data_c['mon'] = data.index.month
#print(data_c.head(10))
fig, ax5 = plt.subplots()
fig.set_size_inches((6,20))
monmean = data_c.groupby('mon')
monmean.boxplot(column=['TUAISPO Comdty'], by='mon', showfliers=False, ax=ax5, patch_artist=True)
#plt.show()

data_c['day'] = data_c.index.dayofweek
fig, ax6 = plt.subplots()
fig.set_size_inches((6,20))
daybox = data_c.groupby('day')
daybox.boxplot(column=['TUAISPO Comdty'], by='day', showfliers=False, ax=ax6, patch_artist=True)
#plt.show()

