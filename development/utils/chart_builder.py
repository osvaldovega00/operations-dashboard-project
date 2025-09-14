import plotly.graph_objects as go
import dash_bootstrap_components as dbc

def build_bar_line_chart(bar_x, bar_y, bar_name, bar_text, line_x, line_y, line_name):
    """Bar + Line Chart"""
    fig = go.Figure()

    # Bar chart trace
    fig.add_trace(go.Bar(
        x=bar_x,
        y=bar_y,
        name=bar_name,
        marker_color='steelblue',
        text=bar_text,
        textposition='outside'
    ))

    # Line chart trace
    fig.add_trace(go.Scatter(
        x=line_x,
        y=line_y,
        name=line_name,
        mode='lines+markers',
        line=dict(color='darkorange', width=2),
        marker=dict(size=6)
    ))

    return fig

def dataframe_table(df):
    """Table built using pandas dataframes"""
    table = dbc.Table.from_dataframe(
        df,  #DataFrame
        striped=True,
        bordered=True,
        hover=True,
        responsive=True,
        className='mt-4'
    )
    return table
