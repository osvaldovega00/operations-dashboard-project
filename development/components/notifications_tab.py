from dash import html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from utils.data_loader import load_notifications, notif_count
from utils.chart_builder import build_bar_line_chart, dataframe_table

order_df = load_notifications()
notif_total = notif_count()

### Bar + Line Chart Section ###
monthly_counts_bar = order_df[order_df['System status'].str.contains('DSCL')]
monthly_counts_bar = monthly_counts_bar.groupby('Date_MMMYY').size().reset_index(name='Count')
monthly_counts_line = order_df.groupby('Date_MMMYY').size().reset_index(name='Count')

notif_barline_fig = build_bar_line_chart(
    bar_x = monthly_counts_bar['Date_MMMYY'],
    bar_y = monthly_counts_bar['Count'],
    bar_name = 'Monthly Notifications',
    bar_text = monthly_counts_bar['Count'],
    line_x = monthly_counts_line['Date_MMMYY'],
    line_y = monthly_counts_line['Count'],
    line_name = 'Total Notifications',
)

notif_barline_fig.update_layout(
    title=f'Total Notifications - {notif_total}<br><br>Notifications per Month:',
    xaxis_title='Month-Year',
    yaxis_title='Notification Count',
    xaxis_tickangle=-45,
    legend_title='Chart Type',
    barmode='overlay'
)

### Table Section ###
table_df = load_notifications()
table_df['Notif. Date'] = table_df['Notif. Date'].dt.strftime('%d-%b-%y')
table_df = table_df[~table_df['System status'].str.contains('DSCL')]
table_df = table_df[['Notification', 'Order', 'System status', 'Description', 'Notif. Date']]
table_df.rename(columns={'System status':'System Status', 'Notif. Date':'Notification Date'}, inplace=True)
notif_table = dataframe_table(table_df)

### Dash Layout Section ###
notifications_layout = html.Div([
    dbc.Card([
        dbc.CardBody([
            html.H5('SAP Notifications'),
            dcc.Graph(figure=notif_barline_fig),
            html.Hr(),
            html.H5('Open Notifications'),
            notif_table
        ])
    ], style={'width': '100%', 'margin': '0', 'padding': '0'})
])