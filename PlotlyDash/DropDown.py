import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

def SetUpData(time_x, mean_value, top_value, bot_value, color):
    
    m = go.Scatter(x=time_x, y=mean_value, name = ('Mean ' + mean_value.name),
                         mode = 'lines', line = (dict(color = color)))
    t = go.Scatter(x=time_x, y=top_value, name = ('Upper Limit ' + top_value.name),
                         mode = 'lines', line = dict(color = color))
    b = go.Scatter(x=time_x, y=bot_value, name = ('Lower Limit ' + bot_value.name),
                         mode = 'lines',
                         fill='tonexty', line = dict(color = color))

    return [m, t, b]

df = pd.read_csv("InputData.csv")
df1 = df.loc[:, ["First Motion", "Second Motion", "Third Motion"]]
df1_T= df1.add([2, 1, 0.5], axis = 'columns')
df1_B = df1.sub([2, 1, 0.5], axis = 'columns')

First = SetUpData(df['TIME'], df['First Motion'], df1_T['First Motion'], df1_B['First Motion'], 'red')
Second = SetUpData(df['TIME'], df['Second Motion'], df1_T['Second Motion'], df1_B['Second Motion'], 'blue')
Third = SetUpData(df['TIME'], df['Third Motion'], df1_T['Third Motion'], df1_B['Third Motion'], 'green')

table_1 = [go.Table( 
    header=dict(values=list(df.columns)), 
    cells=dict(values = [df['TIME'], df['Raw'], df['First Motion'], df['Second Motion'], df['Third Motion']], font=dict( size=12)), visible = False)]

data = [*First, *Second, *Third, *table_1]



updatemenus = list([
    dict(active=0,
         buttons= [
            dict(label = 'All Angles',
                 method = 'update',
                 args = [{'visible': [True, True, True, True, True, True, True, True, True, False]},
                         {'title': 'All Graphs'}]),

            dict(label = 'First Angle',
                 method = 'update',
                 args = [{'visible': [True, True, True, False, False, False, False, False, False, False]},
                         {'title': 'First'}]),

            dict(label = 'Second Angle',
                 method = 'update',
                 args = [{'visible': [False, False, False, True, True, True, False, False, False, False]},
                         {'title': 'Second'}]), 
            
            dict(label = 'Third Angle',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, True, True, True, False]},
                         {'title': 'Third'}]), 

            dict(label = 'Raw Data',
                 method = 'update',
                 args = [{'visible': [False, False, False, False, False, False, False, False, False, True]},
                         {'title': 'Raw Data Table'},])],
    )
])


font = dict(family="Courier New, monospace",
        size=18,
        color="black")

layout = dict( xaxis_title = 'TIME [units]', yaxis_title = 'Angle Value [units]', font = font, template = 'simple_white', showlegend=True,
              updatemenus=updatemenus)

config=dict({'modeBarButtonsToAdd':['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]})

fig = dict(data = data, layout = layout)


plotly.offline.plot(fig, filename='Buttons.html', config = config)