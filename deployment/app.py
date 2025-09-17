import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
from utils.refresh_logic import *
import os

# Import tab layouts from components
from components.ympp_tab import ympp_layout
from components.ymcm_tab import ymcm_layout
from components.notifications_tab import notifications_layout

# Initialize Dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title='Work Orders'
)

# Define layout
app.layout = html.Div([
    dbc.Navbar(
        dbc.Container([
            dbc.Button("Refresh", id="refresh-btn", color="primary", className="ms-2"),
            dbc.NavbarBrand('Plant Engineering Work Orders', className='mx-auto'),
        ], fluid=True),
        color='steelblue',
        dark=True,
        className='mb-4'
    ),

    # Tab structure
    dbc.Tabs([
        dbc.Tab(label='YMPP', tab_id='ympp', children=[ympp_layout]),
        dbc.Tab(label='YMCM', tab_id='ymcm', children=[ymcm_layout]),
        dbc.Tab(label='Notifications', tab_id='notif', children=[notifications_layout])
    ], id='tabs', active_tab='ympp', className='mb-4')
])

@app.callback(
        Output('ympp-graph', 'figure'),
        Output('ympp-table', 'children'),
        Output('ymcm-graph', 'figure'),
        Output('ymcm-table', 'children'),
        Output('notif-graph', 'figure'),
        Output('notif-table', 'children'),
        Input('refresh-btn', 'n_clicks')
)
def refresh_dashboard(n_clicks):
    if n_clicks:
        ympp_fig = ympp_chart_refresh()
        ympp_table = ympp_table_refresh()
        ymcm_fig = ymcm_chart_refresh()
        ymcm_table = ymcm_table_refresh()
        notif_fig = notif_chart_refresh()
        notif_table = notif_table_refresh()
        return ympp_fig, ympp_table, ymcm_fig, ymcm_table, notif_fig, notif_table
    else:  
        return dash.no_update

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run_server(host='0.0.0.0', port=port, debug=False)