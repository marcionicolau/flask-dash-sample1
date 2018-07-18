import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from flask import Flask, redirect

# app = dash.Dash(__name__)
# server = app.server
server = Flask(__name__)
app = dash.Dash(__name__, server=server, url_base_pathname='/dash')


@server.route('/plotly_dashboard')
def render_dashboard():
    return redirect('/dash')


@server.route('/')
def hello():
    return '<h1 class="ui header">Hello from Flask!</h1>'


def main_layout():
    return html.Div([
        html.H2('Hello World!', className="ui header"),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL', 'RS', 'SC', 'PR']
            ],
            value='LA'
        ),
        html.Div(id='display-value', className="ui segment")
    ])


app.layout = main_layout()

lst_css = ['https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/1.11.8/semantic.min.css',
           "https://codepen.io/chriddyp/pen/bWLwgP.css"]

lst_js = ['https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js',
          'https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/1.11.8/semantic.min.js']


for css in lst_css:
    app.css.append_css({"external_url": css})

for js in lst_js:
    app.scripts.append_script({'external_url': js})


@app.callback(Output('display-value', 'children'),
              [Input('dropdown', 'value')])
def display_value(value):

    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True)
