import dash
import dash_html_components as html
import dash_core_components as dcc

from multipage import layout

app = dash.Dash(__name__)

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    layout.header,
    layout.menu,
    html.Div(id='page-content')
])
