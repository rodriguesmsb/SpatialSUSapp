#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(
    children = [
        html.Div(
            children = [html.P("VizSUSapp", className = "h1"),
                        html.P("Aplicativo para visualização de dados agregados", className = "h2")],
            className = "header"),
        html.Div(
            children = [html.P("NavBar", className = "text")],
            className = "nav-bar"),
        html.Div(
            children = [html.P("MainBody", className = "text")],
            className = "main-body"
        )

    ]   
)


