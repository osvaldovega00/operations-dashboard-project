from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utils.data_loader import load_orders, orders_count
from utils.chart_builder import build_bar_line_chart, order_table

### Bar + Line Graph Section ###
order_df = load_orders('YMPP', 'Basic fin. date')
orders_total = orders_count('YMPP')
ympp_barline_fig = build_bar_line_chart(order_df, orders_total)

### Table Section ###
table_df = load_orders('YMPP', 'Basic fin. date')
ympp_table_fig = order_table(table_df, 'Basic fin. date')

### Dash Layout Section ###
ympp_layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H5('Periodic Maintenance Orders'),
            dcc.Loading(
                id="loading-ympp",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[dcc.Graph(id="ympp-graph", figure=ympp_barline_fig)],
                fullscreen=False
            ),
            html.Hr(),
            html.H5('Open Orders'),
            dcc.Loading(
                id="loading-ympp-table",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[html.Div(id="ympp-table", children=[ympp_table_fig])],
                fullscreen=False
            ),
            
        ])
    ], style={'width': '100%', 'margin': '0', 'padding': '0'})
])