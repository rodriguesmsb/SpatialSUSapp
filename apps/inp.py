#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""
import dash_html_components as html
import dash_core_components as dcc
from components import sec_inp

layout = html.Div(
    id = "main-body",
    children = [
        html.Div(
            id = "header",
            children = [
                html.P("SpatialSUSapp", className = "header-title"),
                html.P("Um aplicação em dash para a visualização de dados agregados", className = "home-text")
            ],
            className = "header"
        ),
        sec_inp.layout,
        html.Div(
            children = [
                html.P("Dados", className = "input-mark"),
                html.Div(id = "output-data-upload")
                
            ])
        
    ],
    className = "body"
)








