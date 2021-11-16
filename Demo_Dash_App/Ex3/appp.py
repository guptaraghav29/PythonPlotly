
import dash
import json
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from pandas import json_normalize
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from cleanmod12 import fig_objects

app = dash.Dash(__name__)

colors = {
    'background': '#FFFFFF',
    'text': '#F00000'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


fig = fig_objects[0]

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Demo for hosted web app',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Dropdown(
        id='figure-list',
        options= [{'label': 'graph 1' , 'value' : 'Name of graph one'} , {'label': 'graph 2' , 'value' : 'Name of graph two'} ],
        value = 'Name of graph one'
    ),  
    html.Div(id='dd-output-container', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
     dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    html.Div(id='container'),
    html.Div(
        dcc.Graph( id='empty', figure={'data': []}), 
            style={'display': 'none'}
            )

    

])

@app.callback(
   Output('dd-output-container', 'children'), 
    Input('figure-list', 'value')
)

def update_output(value):
    return 'You have selected "{}"'.format(value)

@app.callback(Output('example-graph-2', 'figure'),
    Input('figure-list', 'value'))

def update_figure_output(value):
    if value == 'Name of graph two':
        figure = fig_objects[1]
    else : figure = fig_objects[0] 
    return figure

@app.callback(Output('container', 'children'),
    Input('figure-list', 'value'))
def addinggraphsfromlist(value):
    if value == 'Name of graph two':
        graphs = []
        for i in range(0,len(fig_objects)):
            graphs.append(dcc.Graph(
                id='graph-{}'.format(i),
                figure= fig_objects[i]
            ))
        return html.Div(graphs)

   


if __name__ == '__main__':
    app.run_server(debug=True)
