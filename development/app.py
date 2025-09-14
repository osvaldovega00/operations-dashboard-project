import dash
import dash_bootstrap_components as dbc
from dash import html

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
            dbc.NavbarBrand('Plant Engineering Work Orders', className='mx-auto')
        ]),
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

# Run the app
if __name__ == '__main__':
    app.run(debug=False)