import json

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

app = dash.Dash(__name__)

app.layout = html.Div([

    dcc.Graph(
        id='chart-1',
        figure={
            'data': [
                {
                    'x': [1, 2, 3, 4],
                    'y': [4, 1, 3, 5],
                    'text': ['a', 'b', 'c', 'd'],
                    'customdata': ['c.a', 'c.b', 'c.c', 'c.d'],
                    'name': 'Trace 1',
                    'mode': 'markers',
                    'marker': {'size': 20}
                }, {
                    'x': [1, 2, 3, 4],
                    'y': [9, 4, 1, 4],
                    'text': ['w', 'x', 'y', 'z'],
                    'customdata': ['c.w', 'c.x', 'c.y', 'c.z'],
                    'name': 'Trace 2',
                    'mode': 'markers',
                    'marker': {'size': 12}
                }
            ],
            'layout': {
                'clickmode': 'event+select'
            }
        }
    ),

    html.Div(className='row', children=[

        html.Div([
            dcc.Markdown("""
                        **Hover Data**
                    """),
            html.Pre(id='hover-data')
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Click Data**
            """),
            html.Pre(id='click-data')
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Selection Data**
            """),
            html.Pre(id='selection-data')
        ], className='three columns'),
        html.Div([
            dcc.Markdown("""
                **Zoom and Relayout Data**
            """),
            html.Pre(id='relayout-data')
        ], className='three columns'),

    ])
])


@app.callback(Output('hover-data', 'children'), [Input('chart-1', 'hoverData')])
def display_hover_data(hover_data):
    return json.dumps(hover_data, indent=2)


@app.callback(Output('click-data', 'children'), [Input('chart-1', 'clickData')])
def display_click_data(click_data):
    return json.dumps(click_data, indent=2)


@app.callback(Output('selection-data', 'children'), [Input('chart-1', 'selectedData')])
def display_selection_data(selection_data):
    return json.dumps(selection_data, indent=2)


@app.callback(Output('relayout-data', 'children'), [Input('chart-1', 'relayoutData')])
def display_selected_data(relayout_data):
    return json.dumps(relayout_data)


if __name__ == '__main__':
    app.run_server(debug=True)
