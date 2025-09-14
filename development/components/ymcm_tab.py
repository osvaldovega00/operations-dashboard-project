from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utils.data_loader import load_orders, orders_count
from utils.chart_builder import build_bar_line_chart, dataframe_table

### Bar + Line Chart Section ###
order_df = load_orders('YMCM', 'Sched. finish')
orders_total = orders_count('YMCM')

monthly_counts_bar = order_df[order_df['System status'].str.contains('TECO')]
monthly_counts_bar = monthly_counts_bar.groupby('Date_MMMYY').size().reset_index(name='Count')
monthly_counts_line = order_df.groupby('Date_MMMYY').size().reset_index(name='Count')

ymcm_barline_fig = build_bar_line_chart(
    bar_x = monthly_counts_bar['Date_MMMYY'],
    bar_y = monthly_counts_bar['Count'],
    bar_name = 'Open Orders',
    bar_text = monthly_counts_bar['Count'],
    line_x = monthly_counts_line['Date_MMMYY'],
    line_y = monthly_counts_line['Count'],
    line_name = 'Total Orders',
)

ymcm_barline_fig.update_layout(
    title=f'Total Orders - {orders_total}<br><br>Orders per Month:',
    xaxis_title='Month-Year',
    yaxis_title='Order Count',
    xaxis_tickangle=-45,
    legend_title='Chart Type',
    barmode='overlay'
)

### Table Section ###
table_df = load_orders('YMCM', 'Sched. finish')
table_df['Sched. finish'] = table_df['Sched. finish'].dt.strftime('%d-%b-%y')
table_df = table_df[~table_df['System status'].str.contains('TECO')]
table_df = table_df[['Order', 'Notification', 'System status', 'Description', 'Sched. finish']]
table_df.rename(columns={'System status':'System Status', 'Sched. finish':'Due Date'}, inplace=True)
ymcm_table = dataframe_table(table_df)

### Dash Layout Section ###
ymcm_layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H5('Corrective Maintenance Orders'),
            dcc.Graph(figure=ymcm_barline_fig),
            html.Hr(),
            html.H5('Open Orders'),
            ymcm_table
        ])
    ], style={'width': '100%', 'margin': '0', 'padding': '0'})
])