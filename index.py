#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from app import app
from apps import inp
import io
import base64

###Add code to use external css
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]


###Create a instance of Dash class
app = dash.Dash(__name__, external_stylesheets = [external_stylesheets])
app.title = "Data visualization"



app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])




#define all calllback that will be used
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "#":
        return 404
    elif pathname == "#":
        return 404
    else:
        return inp.layout


def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decode  = base64.b64decode(content_string)
    try:
        df = pd.read_csv(
            io.StringIO(decode.decode("utf-8")))
    except:
        pass
    return df
    
if __name__ == '__main__':
    app.run_server(debug = True)
