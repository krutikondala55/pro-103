import pandas as pd 
import plotly.express as px
df=pd.read_csv('data.csv')
fig=px.data(df,x='cases',y='country')
fig.show()