import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly
import plotly.express as px
import plotly.io as pio
from flask import Flask
import figures


server=Flask(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server)

app.layout = figures.displayfig

@server.route("/hello")
def get():
    return "Hello,World!"

@server.route("/dash")
def dashboard():
    return app.index()


if __name__ == '__main__':
    app.run_server(debug=True)

