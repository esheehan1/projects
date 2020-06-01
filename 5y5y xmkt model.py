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

df_5y5y = df[['CZK 5Y X 5Y Fwd Swap Rate','PLN 5Y X 5Y Fwd Swap Rate','ILS 5Y X 5Y Fwd Swap Rate','HUF 5Y X 5Y Fwd Swap Rate','5Y X 5Y CHF Fwd Swap Rate','5Y X 5Y EUR Fwd Swap Rate','5Y X 5Y GBP Fwd Swap Rate','5Y X 5Y SEK Fwd Swap Rate']][:-150]
avg_5y5y = df_5y5y.sum(axis=1)/8

legend = ['CZK','PLN','ILS','HUF','CHF','EUR','GBP','SEK']
M_A1=df_5y5y.rolling(window=10).mean()
M_A2=df_5y5y.rolling(window=23).mean()
ax1.plot(df_5y5y)
ax1.plot(avg_5y5y, c='black')
ax1.legend(legend, loc='upper left')
ax1.set_title('5Y5Y X-Market')

# Correlation Plot
#ax2 = sns.heatmap(df_5y5y.corr(), xticklabels=legend, yticklabels=legend, cmap='RdYlGn', center=0, annot=True)
spread = df['PLN 5Y X 5Y Fwd Swap Rate'] - avg_5y5y
ax2.plot(spread)

# Decorations
#ax2.title('Historical Correlations', fontsize=22)
#ax2.xticks(fontsize=8)
#ax2.yticks(fontsize=4)

print(df_5y5y.corr())

x1 = avg_5y5y
y1 = df_5y5y['PLN 5Y X 5Y Fwd Swap Rate']

ax4 = sns.regplot(x=x1, y=y1, marker="+")
#plt.show()


colors = np.linspace(0.1, 1, len(df_5y5y))
mymap = plt.get_cmap("winter")
ax3 = ax3.scatter(x1 , y1 , c=colors, cmap=mymap, lw=0)
cb = plt.colorbar(ax3)
#plt.subplot(x1[-1],y1[-1],'ro')
cb.ax.set_yticklabels([str(p.date()) for p in df_5y5y [::len(df_5y5y)//10].index]);
fig.tight_layout()
plt.show()
