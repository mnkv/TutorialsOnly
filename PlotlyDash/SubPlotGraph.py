import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('InputData.csv')
df1 = df.loc[:, ["First Motion", "Second Motion", "Third Motion"]]
df1_T= df1.add([2, 1, 0.5], axis = 'columns')
df1_B = df1.sub([2, 1, 0.5], axis = 'columns')

fig2 = make_subplots(rows=1, cols=3, start_cell="top-left")
# Plot first motion, mean, upper and lower limits on the first subplot row = 1, col = 1
fig2.add_trace(go.Scatter(x=df['TIME'], y=df['First Motion'],
                         mode = 'lines', line = (dict(color = 'red')), name = 'Mean First Motion'), row = 1, col =1)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['First Motion'],
                         mode = 'lines', line = dict(color = 'red'), name = 'Upper Limit First Motion'), row = 1, col = 1)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['First Motion'],
                         mode = 'lines', name = 'Lower Limit First Motion',
                         fill='tonexty', line = dict(color = 'red')), row = 1, col = 1)

# Plot first motion, mean, upper and lower limits on the first subplot row = 1, col = 2
fig2.add_trace(go.Scatter(x=df['TIME'], y=df['Second Motion'],
                         mode = 'lines', line = (dict(color = 'blue'))), row = 1, col = 2)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['Second Motion'],
                         mode = 'lines', line = dict(color = 'blue')), row = 1, col = 2)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['Second Motion'],
                         mode = 'lines',
                         fill='tonexty', line = dict(color = 'blue')), row = 1, col = 2)

fig2.add_trace(go.Scatter(x=df['TIME'], y=df['Third Motion'],
                         mode = 'lines', line = (dict(color = 'green'))), row = 1, col = 3)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_T['Third Motion'],
                         mode = 'lines', line = dict(color = 'green')), row = 1, col = 3)
fig2.add_trace(go.Scatter(x=df['TIME'], y=df1_B['Third Motion'],
                         mode = 'lines',
                         fill='tonexty', line = dict(color = 'green')), row = 1, col = 3)


fig2.update_xaxes(
        tickangle = 90,
        title_text = "TIME [units]",
        title_font = {"size": 20},
        title_standoff = 25)

fig2.update_yaxes(
        title_text = "Angle Value [units]",
        title_standoff = 25)


plotly.offline.plot(fig2, filename='SubPlotGraph.html')