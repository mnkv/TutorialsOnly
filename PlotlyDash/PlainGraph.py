import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('InputData.csv')
df1 = df.loc[:, ['First Motion', 'Second Motion', 'Third Motion']]
df1_T= df1.add([2, 1, 0.5], axis = 'columns')
df1_B = df1.sub([2, 1, 0.5], axis = 'columns')


# Simple way to plot multiple columns from the data frame through plotly.express 
fig = px.line(df, x='TIME', y=['First Motion', 'Second Motion', 'Third Motion'])\
    .update_traces(dict(line_width=6))

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=df['TIME'], y=df['First Motion'],
                         mode = 'lines', line = (dict(color = 'red'))))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['First Motion'],
                         mode = 'lines', line = dict(color = 'red')))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['First Motion'],
                         mode = 'lines',
                         fill='tonexty', line = dict(color = 'red')))

fig2.add_trace(go.Scatter(x=df['TIME'], y=df['Second Motion'],
                         mode = 'lines', line = (dict(color = 'blue'))))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['Second Motion'],
                         mode = 'lines', line = dict(color = 'blue')))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['Second Motion'],
                         mode = 'lines',
                         fill='tonexty', line = dict(color = 'blue')))

fig2.add_trace(go.Scatter(x=df['TIME'], y=df['Third Motion'],
                         mode = 'lines', line = (dict(color = 'green'))))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['Third Motion'],
                         mode = 'lines', line = dict(color = 'green')))
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['Third Motion'],
                         mode = 'lines',
                         fill='tonexty', line = dict(color = 'green')))

plotly.offline.plot(fig, filename='PlainGraph.html')
plotly.offline.plot(fig2, filename='FillGraph.html')