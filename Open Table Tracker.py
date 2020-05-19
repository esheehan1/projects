import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import plotly.express as px
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
cf.set_config_file(theme='white')
init_notebook_mode(connected=True)

# Data Source: https://www.opentable.com/state-of-industry

input_data = pd.read_csv('state_of_industry_data.csv')
x = input_data.head()
#print(x)

countries_data = input_data[input_data['Type'] == 'country'].drop(columns=['Type']).set_index('Name').T
countries_data
print(countries_data.head)

countries_data.plot()
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.ylabel('Resturamt Reservations, YoY Change', fontsize = 15) #for y label
plt.xlabel('Date', fontsize = 15) #for x label
plt.show()




