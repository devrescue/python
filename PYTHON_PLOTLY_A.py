import plotly.express as px
import pandas as pd
  
d = {'CLASS_TYPE': ['A','B','C','D','E'], 
     'STUDENTS': [120,225,30,109,308]}

df = pd.DataFrame(data=d)

fig = px.bar(df, x='CLASS_TYPE', y='STUDENTS')
fig.show()

fig = px.bar(df, x='STUDENTS', y='CLASS_TYPE')
fig.show()

fig = px.bar(df, x='STUDENTS', y='CLASS_TYPE', color='CLASS_TYPE', title='Students by Class')
fig.show()

fig = px.bar(df, x='STUDENTS', y='CLASS_TYPE', color='CLASS_TYPE', title='Students by Class',text='STUDENTS')
fig.show()
