
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

layout = html.Section(
            id = "painel",
            children = [
                html.Div(
                    id = "shapefile",
                    children = [
                        html.P("1. Carregar mapa (json)", className = "input-mark"),
                        html.P("Carregar arquivo json ou geosjon", className = "input-desc"),
                        dcc.Upload(
                            id = "upload-data",
                            children = 
                                dbc.Button(
                                    id = "file-select",
                                    children = "Select file", 
                                    className = "menu-icon"),
                            multiple = True),

                        #Add dropdowm menus
                        html.Div(children = "Region", className = "menu-title"),
                        dcc.Dropdown(
                            id = "select-region",
                            options = [],
                            value = None,
                            className = "dropdown"),
                        html.Div(children = "Name", className = "menu-title"),
                        dcc.Dropdown(
                            id = "select-name",
                            options = [],
                            value = None,
                            className = "dropdown")


                    ],
                    className = "col"
        ),
                html.Div(
                    id = "up_data",
                    children = [html.P("2. Carregar dados (csv)", className = "input-mark")], 
                    className = "col"),

                html.Div(
                    id = "sel_an", 
                    children = [html.P("3. Selecionar análise", className = "input-mark")], 
                    className = "col"),
            ],
            className = "section"
)
        
        
