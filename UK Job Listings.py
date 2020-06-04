# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from pandas.plotting import register_matplotlib_converters
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import datetime

# data frame

def import_data():
    raw_data_df = pd.read_csv('UK_Jobs.csv', header=3, index_col=0, parse_dates=True, squeeze=True, dtype=float)
    return raw_data_df

online_jobs = import_data()


#online_jobs.set_index('Date', inplace=True)
online_jobs = online_jobs.dropna()
#online_jobs = online_jobs.drop(['Education'])
print(online_jobs.columns)


for col in online_jobs.columns:
    register_matplotlib_converters()
    fig,ax = plt.subplots(figsize=(10.6/2,4.3))
    plt.plot(online_jobs.index, online_jobs[col].values, color='red')
    plt.gca().xaxis.set_major_locator(mdates.DayLocator((1)))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
    plt.ylabel('Online Jobs Posted', fontsize=12)
    ax.set_xlim('2019-12-01','2020-06-01')
    ax.axvline('2020-03-01', color="black",linewidth=0.5)
    plt.legend([col],
               loc='upper center', bbox_to_anchor=(0.5, 1.11), frameon=False, fontsize=12, ncol=6)

#plt.show()
# UK Shipping data/chart

daily_shipping_data = pd.read_excel('shippingdata (1).xlsx', sheet_name='Weekly all visits', skiprows=4)
daily_shipping_data.rename(columns={'Unnamed: 2': 'All UK'}, inplace=True) #Rename column we need
daily_shipping_data = daily_shipping_data[['Week commencing', 'All UK']] #Filter
daily_shipping_data.set_index('Week commencing', inplace=True)
daily_shipping_data['7dMA'] = daily_shipping_data.rolling(5).mean()

print(daily_shipping_data.head())

register_matplotlib_converters()
fig,ax = plt.subplots(figsize=(10,4.3))
plt.plot(daily_shipping_data.index, daily_shipping_data['All UK'].values)
plt.plot(daily_shipping_data.index, daily_shipping_data['7dMA'].values)
plt.gca().xaxis.set_major_locator(mdates.DayLocator((1)))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d %b"))
plt.ylabel('Number of visits to Ports ', fontsize=12)
# ax.axvline('2020-03-01', color="black",linewidth=0.5)
plt.legend(['Weekly Shipping Activity', '5 Week Average'],
           loc='upper center', bbox_to_anchor=(0.5, 1.11), frameon=False, fontsize=12, ncol=6)

plt.show()