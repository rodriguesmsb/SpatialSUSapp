import io
import base64
import dash_html_components as html
import pandas as pd
import dash_table



#Function to parse csv data and retun dataTable
def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(
            io.StringIO(decoded.decode('utf-8')))
        df.to_csv("data/file.csv")
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'])
    return html.Div([
        dash_table.DataTable(
            data = df.head().to_dict('records'),
            columns = [{'name': i, 'id': i} for i in df.columns]
        )  
    ])




