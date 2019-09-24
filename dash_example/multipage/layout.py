import dash_html_components as html
import dash_core_components as dcc

header = html.Div(
    html.H1('Mediação Online')
)

menu = html.Div([
    dcc.Link('Go to Page 1', href='/page-1'),
    dcc.Link('Go to Page 2', href='/page-2'),
])
