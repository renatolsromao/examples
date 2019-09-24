import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='my-input-id', value='Initial value', type='text'),
    html.Div(id='my-div-id')
])

@app.callback(
    Output(component_id='my-div-id', component_property='children'),
    [Input(component_id='my-input-id', component_property='value')]
)
def update_output_div(input_value):
    return f"You've entenred: {input_value}"


if __name__ == '__main__':
    app.run_server()