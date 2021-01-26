#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""
import dash_html_components as html


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
        html.Section(
            id = "painel",
            children = [
                html.Div(
                    id = "shapefile",
                    children = [],
                    className = "col"
        ),
                html.Div(id = "up_data", children = [], className = "col"),
                html.Div(id = "sel_an", children = [], className = "col"),
            ],
            className = "section"
        )
        

    ],
    className = "body"
)