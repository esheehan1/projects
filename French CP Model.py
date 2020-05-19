import numpy as np
import pandas as pd
import plotly_express as px
from plotly.subplots import make_subplots


fig = make_subplots(rows=3, cols=1)

#Import and create the dataframes:
# Note need to delete 2 cells and replace , with . in the CSV files

def import_data():
    raw_data_df = pd.read_csv('FR_CP.csv', header=2, encoding = 'unicode_escape')
    return raw_data_df

result = import_data()

def import_data_2():
    raw_data_df2 = pd.read_csv('FR_CP_Rate.csv', header=2, encoding = 'unicode_escape')
    return raw_data_df2

result2 = import_data_2()

#Merge the two CSV's
df = pd.merge(result, result2, on='Unnamed: 0', how='left')

#Drop Unwanted Columns
df = df.drop(columns=['1 jour_x', '1 semaine_x', '2 semaines_x', '1 mois_x',
       '2 mois_x', '4 mois_x', '6 mois_x', '9 mois_x',
       '1 jour.4_y', '1 semaine.4_y', '2 semaines.4_y', '1 mois.4_y',
       '2 mois.4_y', '3 mois.4_y', '4 mois.4_y', '6 mois.4_y', '9 mois.4_y',
       '12 mois.4_y', '3 mois_x', '12 mois_x', '1 jour.1_x', '1 semaine.1_x',
       '2 semaines.1_x', '1 mois.1_x', '2 mois.1_x',
       '4 mois.1_x', '6 mois.1_x', '9 mois.1_x', '12 mois.1_x', '1 jour.2_x',
       '1 semaine.2_x', '2 semaines.2_x', '1 mois.2_x', '2 mois.2_x',
       '3 mois.2_x', '4 mois.2_x', '6 mois.2_x', '9 mois.2_x', '12 mois.2_x',
       '1 jour.3_x', '1 semaine.3_x', '2 semaines.3_x', '1 mois.3_x',
       '2 mois.3_x', '3 mois.3_x', '4 mois.3_x', '6 mois.3_x', '9 mois.3_x',
       '12 mois.3_x', '1 jour.4_x', '1 semaine.4_x', '2 semaines.4_x',
       '1 mois.4_x', '2 mois.4_x', '3 mois.4_x', '4 mois.4_x', '6 mois.4_x',
       '9 mois.4_x', '12 mois.4_x', '1 jour_y', '1 semaine_y', '2 semaines_y',
       '1 mois_y', '2 mois_y', '3 mois_y', '4 mois_y', '6 mois_y', '9 mois_y',
       '12 mois_y', '1 jour.1_y', '1 semaine.1_y', '2 semaines.1_y',
       '1 mois.1_y', '2 mois.1_y', '4 mois.1_y', '6 mois.1_y',
       '9 mois.1_y', '12 mois.1_y', '1 jour.2_y', '1 semaine.2_y',
       '2 semaines.2_y', '1 mois.2_y', '2 mois.2_y', '3 mois.2_y',
       '4 mois.2_y', '6 mois.2_y', '9 mois.2_y', '12 mois.2_y', '1 jour.3_y',
       '1 semaine.3_y', '2 semaines.3_y', '1 mois.3_y', '2 mois.3_y',
       '3 mois.3_y', '4 mois.3_y', '6 mois.3_y', '9 mois.3_y', '12 mois.3_y'])



df = df.rename(columns={
    'Unnamed: 0': 'Date', '3 mois.1_x': 'A1 3m Vol', '3 mois.1_y': 'A1 3m Rate'

})

#Clean data
df=df.dropna()

#Select Timeframe
n = 100
df = df.tail(n)

fig = px.scatter(df, x="Date", y="A1 3m Rate", size="A1 3m Vol", size_max=60, title="French Weekly CP levels (Bubble Size = Volume traded)")
fig.show()

#Can plot individually

#fig = px.scatter(df, x="Date", y="A1 3m Rate")
#fig.show()
#fig = px.scatter(df, x="Date", y="A1 3m Vol")
#fig.show()

