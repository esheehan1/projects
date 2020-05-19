import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller, kpss, acf, grangercausalitytests
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf,month_plot,quarter_plot
from scipy import signal
import matplotlib.pyplot as plt
import seaborn as sns
import panormus.data.bbg as bbg
import datetime as dt
import panormus.utils.chrono as chrono

sns.set_style("whitegrid")
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)

# Code
# Import Data

#data = pd.read_csv('UST10Y.csv')

# Via BB

#bbg_client = bbg.BbgClient()

#ed = chrono.now()
#sd = ed - dt.timedelta(days=3500)

#tickers = ['USGG10YR Index']

#data = bbg_client.get_historical_data(tickers,['PX_LAST'],sd,ed)
#data.columns = ['d','ticker','value']

#data = data.set_index(['d','ticker']).unstack('ticker')
#data.columns = data.columns.droplevel()
#data.columns.names = ['']
#data = data.reset_index()
#data = data.set_index('d')
#data.rename(columns={'USGG10YR Index':'UST 10y'}, inplace=True)
#data = pd.DataFrame(data)
#data['date'] = pd.to_datetime(data['d'])
#print(data.head())

# Via CSV
data = pd.read_csv('CAD.csv')
#data.rename(columns={'USD 10Y Par Swap Rate':'UST 10y'}, inplace=True)
data['date'] = pd.to_datetime(data['Dates'])
data['year'] = data['date'].dt.year
data['month'] = data['date'].dt.month
data['week'] = data['date'].dt.weekofyear
print(data.head(35))

# Plot TS

fig, ax = plt.subplots(figsize=(15, 6))
#d = data[data['obs_id']==2]
sns.lineplot(data['date'], data['ASWABUND Curncy'] )

ax.set_title('Security TS', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
ax.set_xlabel('Year', fontsize = 16, fontdict=dict(weight='bold'))
ax.set_ylabel('bp', fontsize = 16, fontdict=dict(weight='bold'))
plt.tick_params(axis='y', which='major', labelsize=16)
plt.tick_params(axis='x', which='major', labelsize=16)
#plt.show()

# Seasonal Plots

variable = 'ASWABUND Curncy'

fig, ax = plt.subplots(figsize=(15, 6))

palette = sns.color_palette("muted",11)
sns.lineplot(data['month'], data[variable], hue=data['year'], palette=palette)
ax.set_title('Seasonal plot', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
ax.set_xlabel('Month', fontsize = 16, fontdict=dict(weight='bold'))
ax.set_ylabel('Bps', fontsize = 16, fontdict=dict(weight='bold'))

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))

sns.boxplot(data['week'], data[variable], ax=ax[0])
ax[0].set_title('Year-wise Box Plot\n(The Trend)', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
ax[0].set_xlabel('Year', fontsize = 16, fontdict=dict(weight='bold'))
ax[0].set_ylabel('Security', fontsize = 16, fontdict=dict(weight='bold'))

sns.boxplot(data['month'], data[variable], ax=ax[1])
ax[1].set_title('Month-wise Box Plot\n(The Seasonality)', fontsize = 20, loc='center', fontdict=dict(weight='bold'))
ax[1].set_xlabel('Month', fontsize = 16, fontdict=dict(weight='bold'))
ax[1].set_ylabel('Security', fontsize = 16, fontdict=dict(weight='bold'))
fig.tight_layout()


plt.show()