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
from dash.dependencies import Input, Output, State
from app import app
from apps import spatio_temporal
import pandas as pd







###Add code to use external css

###Create a instance of Dash class
app = dash.Dash(__name__, 
external_stylesheets = ["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
                        "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500&display=swap"])
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
        return spatio_temporal.layout

if __name__ == '__main__':
    app.run_server(debug = True)
