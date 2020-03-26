import dash as dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initiate application.

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title = 'Dash on AWS EB!'

# Set up layout
