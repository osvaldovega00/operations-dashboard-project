from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utils.data_loader import load_notifications, notif_count
from utils.chart_builder import notif_build_bar_line_chart, notif_table

### Bar + Line Chart Section ###
order_df = load_notifications()
notif_total = notif_count()
notif_barline_fig = notif_build_bar_line_chart(order_df, notif_total)

### Table Section ###
table_df = load_notifications()
notif_table_fig = notif_table(table_df)

### Dash Layout Section ###
notifications_layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H5('SAP Notifications'),
            dcc.Loading(
                id="loading-notif",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[dcc.Graph(id="notif-graph", figure=notif_barline_fig)],
                fullscreen=False
            ),
            html.Hr(),
            html.H5('Open Notifications'),
            dcc.Loading(
                id="loading-notif-table",
                type="default",  # Options: "default", "circle", "dot", "cube"
                children=[html.Div(id="notif-table", children=[notif_table_fig])],
                fullscreen=False
            ),
            
        ])
    ], style={'width': '100%', 'margin': '0', 'padding': '0'})
])