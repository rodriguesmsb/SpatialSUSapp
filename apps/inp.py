#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc



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
                    children = [
                        html.P("1. Carregar mapa (json)", className = "input-mark"),
                        html.P("Carregar arquivo json ou geosjon", className = "input-desc"),
                        dcc.Upload(
                            id = "upload-json",
                            children = [
                                dbc.Button(
                                    id = "file-select",
                                    children = "Select file", 
                                    className = "menu-icon")]
                            )

                        
                    ],
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



