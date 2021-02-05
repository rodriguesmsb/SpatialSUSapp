#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 26 2021
@author: Moreno rodrigues rodriguesmsb@gmail.com
"""

import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(
    id = "container",
    children = [
        html.Div(
            id = "header",
            children = ["header"],
            className = "header"
        ),
        html.Div(
            id = "nav-bar",
            children = ["Navigation"],
            className = "nav-bar"
        ),
        html.Div(
            id = "main-body",
            children = ["Main body"],
            className = "main-body"
        ),

        html.Div(
            id = "side-bar",
            children = ["Side bar"],
            className = "side-bar"
        ),
        html.Div(
            id = "sid-graph",
            children = ["Side Graph"],
            className = "side-graph"
        ),

        html.Div(
            id = "footer",
            children = [
                html.A(
                    children = html.I(className="fa fa-github"),
                    href ="#"
                )
            ],
            className = "footer"
        )
    ],
    className = "container"
)


