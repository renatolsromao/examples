import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

from multipage.app import app
from multipage.apps import app1, app2


index_page = app1.page_1_layout

# Update the index
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return app1.page_1_layout
    elif pathname == '/page-2':
        return app2.page_2_layout
    else:
        return index_page


if __name__ == '__main__':
    app.run_server(debug=True)
