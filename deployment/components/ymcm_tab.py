from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utils.data_loader import load_orders, orders_count
from utils.chart_builder import build_bar_line_chart, order_table

### Bar + Line Chart Section ###
order_df = load_orders('YMCM', 'Sched. finish')
orders_total = orders_count('YMCM')
ymcm_barline_fig = build_bar_line_chart(order_df, orders_total)

### Table Section ###
table_df = load_orders('YMCM', 'Sched. finish')
ymcm_table_fig = order_table(table_df, 'Sched. finish')

### Dash Layout Section ###
ymcm_layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H5('Corrective Maintenance Orders'),
            dcc.Loading(
                id="loading-ymcm",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[dcc.Graph(id="ymcm-graph", figure=ymcm_barline_fig)],
                fullscreen=False
            ),
            html.Hr(),
            html.H5('Open Orders'),
            dcc.Loading(
                id="loading-ymcm-table",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[html.Div(id="ymcm-table", children=[ymcm_table_fig])],
                fullscreen=False
            ),
            
        ])
    ], style={'width': '100%', 'margin': '0', 'padding': '0'})
])