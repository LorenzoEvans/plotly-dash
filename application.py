import dash as dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initiate application.

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.title = 'Dash on AWS EB!'

# Set up layout

html_children = [
  html.H1(children='Hello Dash!'),
  html.Div(children=''' This Dash is running on Elastic Beanstalk '''),
  dcc.Graph(
    id= 'example-graph',
    figure={
      'data': [
        {'x': ['left', 'center', 'right'], 'y': [3,7,6], 'type': 'bar', 'name': 'category 1'},
        {'x': ['left', 'center', 'right'], 'y': [4,2,5], 'type': 'bar', 'name': 'category 2'},
      ],
      'layout': {
        'plot_bgcolor': 'lightgray',
        'title': 'Graph Title',
        'xaxis': {'title': 'x-axis label'},
        'yaxis': {'title': 'y-axis label'}
      }
    }
  )
]
app.layout = html.Div(children=html_children)
