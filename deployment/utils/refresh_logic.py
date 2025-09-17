from utils.data_loader import load_orders, orders_count, load_notifications, notif_count
from utils.chart_builder import *

def ympp_chart_refresh():
    # YMPP Bar + Line Chart Refresh #
    order_df = load_orders('YMPP', 'Basic fin. date')
    orders_total = orders_count('YMPP')
    ympp_barline_fig = build_bar_line_chart(order_df, orders_total)
    return ympp_barline_fig

def ympp_table_refresh():
    # YMPP Table Refresh#
    table_df = load_orders('YMPP', 'Basic fin. date')
    ympp_table_fig = order_table(table_df, 'Basic fin. date')
    return ympp_table_fig

def ymcm_chart_refresh():
    # YMCM Bar + Line Chart Refresh #
    order_df = load_orders('YMCM', 'Sched. finish')
    orders_total = orders_count('YMCM')
    ymcm_barline_fig = build_bar_line_chart(order_df, orders_total)
    return ymcm_barline_fig

def ymcm_table_refresh():
    # YMCM Table Refresh#
    table_df = load_orders('YMCM', 'Sched. finish')
    ymcm_table_fig = order_table(table_df, 'Sched. finish')
    return ymcm_table_fig

def notif_chart_refresh():
    # Notification Bar + Line Chart Refresh #
    order_df = load_notifications()
    notif_total = notif_count()
    notif_barline_fig = notif_build_bar_line_chart(order_df, notif_total)
    return notif_barline_fig

def notif_table_refresh():
    # Notfications Table Refresh
    table_df = load_notifications()
    notif_table_fig = notif_table(table_df)
    return notif_table_fig