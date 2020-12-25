import pandas as pd 
import plotly.express as px

df=pd.read_csv('CovidData.csv')
fig=px.bar(df,x="country", y="date", color="cases", title='Covid 19 cases')
fig.show()