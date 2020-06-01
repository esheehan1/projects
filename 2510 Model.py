import numpy as np
import pandas as pd
import datetime as dt
import time
from pylab import mpl, plt
from pandas import DataFrame
from matplotlib import pyplot as plt
from statistics import mean
import seaborn as sns
#import pymc3 as pm
from scipy import stats

plt.style.use('seaborn')
mpl.rcParams['font.family']='serif'
np.random.seed(1000)

raw = pd.read_csv('2510_input.csv', nrows=300, index_col=0, parse_dates=True).dropna()
df = DataFrame(raw)

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))
fig.tight_layout()


#AVG_2Y5Y10Y = df['CZK 2Y5Y10Y'+'PLN 2Y5Y10Y'+'ILS 2Y5Y10Y'+'HUF 2Y5Y10Y'+'CHF 2Y5Y10Y'+'EUR 2Y5Y10Y'+'GBP 2Y5Y10Y'+'SEK 2Y5Y10Y'][-250:]

df_2510 = df[['CZK 2Y5Y10Y','PLN 2Y5Y10Y','ILS 2Y5Y10Y','HUF 2Y5Y10Y','CHF 2Y5Y10Y','EUR 2Y5Y10Y','GBP 2Y5Y10Y','SEK 2Y5Y10Y']][:-180]
avg_2510 = df_2510.sum(axis=1)/8
print(df_2510.head(5))
print(avg_2510.head(5))
legend = ['CZK','PLN','ILS','HUF','CHF','EUR','GBP','SEK']
M_A1=df_2510.rolling(window=10).mean()
M_A2=df_2510.rolling(window=23).mean()
ax1.plot(df_2510)
ax1.plot(avg_2510, c='black')
ax1.legend(legend, loc='upper left')
ax1.set_title('2510 X-Market')

# Correlation Plot
ax3 = sns.heatmap(df_2510.corr(), xticklabels=legend, yticklabels=legend, cmap='RdYlGn', center=0, annot=True)

spread = df['CZK 2Y5Y10Y'] - avg_2510
ax2.plot(spread)
# Decorations
#ax2.title('Historical Correlations', fontsize=22)
#ax2.xticks(fontsize=8)
#ax2.yticks(fontsize=4)


fig.tight_layout()
plt.show()
