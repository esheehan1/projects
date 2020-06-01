
# Calling bloomberg code

import panormus.data.bbg as bbg
import datetime as dt
import panormus.utils.chrono as chrono
from matplotlib import pyplot as plt

bbg_client = bbg.BbgClient()

ed = chrono.now()
sd = ed - dt.timedelta(days=600)

tickers = ['.CADSEK Curncy']

data = bbg_client.get_historical_data(tickers,['PX_LAST'],sd,ed)
data.columns = ['d','ticker','value']

data = data.set_index(['d','ticker']).unstack('ticker')
data.columns = data.columns.droplevel()
data.columns.names = ['']
data = data.reset_index()

data = data.set_index('d')

print(data.tail())
SD = data.diff()[-100:]. std()
SD2 = data.diff()[-30:]. std()
print(SD)
print(SD2)

Stop = data[-1:] - 3*SD
print(Stop)

