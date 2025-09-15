import plotly.graph_objects as go
import dash_bootstrap_components as dbc

def build_bar_line_chart(order_df, orders_total):
    """Bar + Line Chart"""

    monthly_counts_bar = order_df[order_df['System status'].str.contains('TECO')]
    monthly_counts_bar = monthly_counts_bar.groupby('Date_MMMYY').size().reset_index(name='Count')
    monthly_counts_line = order_df.groupby('Date_MMMYY').size().reset_index(name='Count')

    fig = go.Figure()

    # Bar chart trace
    fig.add_trace(go.Bar(
        x=monthly_counts_bar['Date_MMMYY'],
        y=monthly_counts_bar['Count'],
        name='Open Orders',
        marker_color='steelblue',
        text=monthly_counts_bar['Count'],
        textposition='outside'
    ))

    # Line chart trace
    fig.add_trace(go.Scatter(
        x=monthly_counts_line['Date_MMMYY'],
        y=monthly_counts_line['Count'],
        name='Total Orders',
        mode='lines+markers',
        line=dict(color='darkorange', width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title=f'Total Orders - {orders_total}<br><br>Orders per Month:',
        xaxis_title='Month-Year',
        yaxis_title='Order Count',
        xaxis_tickangle=-45,
        legend_title='Chart Type',
        barmode='overlay'
)
    return fig

def order_table(table_df, date_df):
    """Table built using pandas dataframes"""

    table_df[date_df] = table_df[date_df].dt.strftime('%d-%b-%y')
    table_df = table_df[~table_df['System status'].str.contains('TECO')]
    table_df = table_df[['Order', 'Notification', 'System status', 'Description', 'Basic fin. date']]
    table_df.rename(columns={'System status':'System Status', 'Basic fin. date':'Due Date'}, inplace=True)

    table = dbc.Table.from_dataframe(
        table_df,  #DataFrame
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className='mt-4'
    )
    return table

def notif_build_bar_line_chart(order_df, orders_total):
    """Bar + Line Chart"""

    monthly_counts_bar = order_df[order_df['System status'].str.contains('DSCL')]
    monthly_counts_bar = monthly_counts_bar.groupby('Date_MMMYY').size().reset_index(name='Count')
    monthly_counts_line = order_df.groupby('Date_MMMYY').size().reset_index(name='Count')

    fig = go.Figure()

    # Bar chart trace
    fig.add_trace(go.Bar(
        x=monthly_counts_bar['Date_MMMYY'],
        y=monthly_counts_bar['Count'],
        name='Open Notifications',
        marker_color='steelblue',
        text=monthly_counts_bar['Count'],
        textposition='outside'
    ))

    # Line chart trace
    fig.add_trace(go.Scatter(
        x=monthly_counts_line['Date_MMMYY'],
        y=monthly_counts_line['Count'],
        name='Total Notifications',
        mode='lines+markers',
        line=dict(color='darkorange', width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title=f'Total Notifications - {orders_total}<br><br>Notifications per Month:',
        xaxis_title='Month-Year',
        yaxis_title='Notification Count',
        xaxis_tickangle=-45,
        legend_title='Chart Type',
        barmode='overlay'
)
    return fig

def notif_table(table_df):
    """Table built using pandas dataframes"""

    table_df['Notif. Date'] = table_df['Notif. Date'].dt.strftime('%d-%b-%y')
    table_df = table_df[~table_df['System status'].str.contains('DSCL')]
    table_df = table_df[['Notification', 'Order', 'System status', 'Description', 'Notif. Date']]
    table_df.rename(columns={'System status':'System Status', 'Notif. Date':'Notification Date'}, inplace=True)

    table = dbc.Table.from_dataframe(
        table_df,  #DataFrame
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className='mt-4'
    )
    return table