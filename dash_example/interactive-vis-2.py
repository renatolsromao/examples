import pandas

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from dash.dependencies import Output, Input

app = dash.Dash(__name__)

indicators_df = pandas.read_csv('https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/'
                                '8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv')

available_indicators = indicators_df['Indicator Name'].unique()

app.layout = html.Div([

    # Dropdown Filters
    html.Div(
        [
            html.Div(
                dcc.Dropdown(
                    id='filter-charts-xaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Fertility rate, total (births per woman)',
                ),
                style={'width': '20%', 'display': 'inline-block', 'margin-left': '2%', 'margin-right': '2%'}
            ),
            html.Div(
                dcc.Dropdown(
                    id='filter-charts-yaxis-column',
                    options=[{'label': i, 'value': i} for i in available_indicators],
                    value='Life expectancy at birth, total (years)',
                ),
                style={'width': '20%', 'display': 'inline-block', 'margin-left': '2%', 'margin-right': '2%'}
            ),
            html.Div([
                dcc.Slider(
                    id='slider-chart-1-year',
                    min=indicators_df['Year'].min(),
                    max=indicators_df['Year'].max(),
                    value=indicators_df['Year'].max(),
                    marks={str(year): str(year) for year in indicators_df['Year'].unique()}
                )
            ], style={'width': '40%', 'display': 'inline-block', 'margin-left': '2%', 'margin-right': '2%',
                      'padding': '0px 20px 20px 20px'}),

        ],
        style={'width': '100%', 'borderBottom': 'thin lightgrey solid', }
    ),

    # Dispersion Chart
    html.Div([
        dcc.Graph(
            id='chart-1-dispersion',
            hoverData={'points': [{'customdata': 'Japan'}]}
        )
    ]),

    # Line charts
    html.Div([
        html.Div([
            dcc.Graph(id='chart-2-x_time_series', style={'width': '49%', 'display': 'inline-block'}),
            dcc.Graph(id='chart-3-y_time_series', style={'width': '49%', 'display': 'inline-block'}),
        ])
    ])

],
    style={'margin': '40px'}
)


@app.callback(
    Output('chart-1-dispersion', 'figure'),
    [
        Input('filter-charts-xaxis-column', 'value'),
        Input('filter-charts-yaxis-column', 'value'),
        Input('slider-chart-1-year', 'value')
    ]
)
def update_chart_1_dispersion(xaxis_column_name, yaxis_column_name, year):
    year_df = indicators_df[indicators_df['Year'] == year]

    return {
        'data': [go.Scatter(
            x=year_df[year_df['Indicator Name'] == xaxis_column_name]['Value'],
            y=year_df[year_df['Indicator Name'] == yaxis_column_name]['Value'],
            text=year_df[year_df['Indicator Name'] == yaxis_column_name]['Country Name'],
            customdata=year_df[year_df['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )]
    }


@app.callback(
    Output('chart-2-x_time_series', 'figure'),
    [
        Input('chart-1-dispersion', 'hoverData'),
        Input('filter-charts-yaxis-column', 'value')
    ]
)
def update_x_timeseries(hover_data, yaxis_column_name):
    df = indicators_df[indicators_df['Country Name'] == hover_data['points'][0]['customdata']]
    df = df[df['Indicator Name'] == yaxis_column_name]
    return create_time_series(df, yaxis_column_name)


@app.callback(
    Output('chart-3-y_time_series', 'figure'),
    [
        Input('chart-1-dispersion', 'hoverData'),
        Input('filter-charts-xaxis-column', 'value')
    ]
)
def update_y_timeseries(hover_data, xaxis_column_name):
    df = indicators_df[indicators_df['Country Name'] == hover_data['points'][0]['customdata']]
    df = df[df['Indicator Name'] == xaxis_column_name]
    return create_time_series(df, xaxis_column_name)


def create_time_series(df, title):
    return {
        'data': [
            go.Scatter(
                x=df['Year'],
                y=df['Value'],
                mode='lines+markers'
            )
        ],
        'layout': {
            'annotations': [{
                'x': 0, 'y': 0.95, 'xanchor': 'left', 'yanchor': 'bottom',
                'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                'text': title
            }],
            'xaxis': {'showgrid': False}
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)
