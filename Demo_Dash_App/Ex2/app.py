# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go

import dash_bootstrap_components as dbc


#########################
# Dashboard Layout / View
#########################
app = dash.Dash(
    external_stylesheets=[dbc.themes.SUPERHERO]
)

navbar = dbc.Navbar(
    [html.H1('Project Header')], 
    color="dark",
    dark=True,
)

card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            )
        ]
    ),
    style={"width": "18rem"},
)

app.layout = html.Div([

    # Page Header
    html.Div([
         navbar , dbc.Row(card),
        html.Div('Select Division', className='three columns'),
                html.Div(dcc.Dropdown(id='division-selector',
                className='nine columns') ) 
    ])
])




if __name__ == "__main__":
    app.run_server()