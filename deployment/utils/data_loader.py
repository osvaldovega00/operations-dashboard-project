import pandas as pd
from utils.gcs_loader import download_order_dataset
from io import BytesIO


def load_orders(order_type, end_date):
    """Load and filter SAP work orders based on order type and end date column.
    Parameters:
        order_type (str): The type of order to filter (e.g., 'YMPP', 'YMCM').
        end_date_col (str): The name of the column containing end dates.
    Returns:
        pd.DataFrame: A filtered DataFrame containing only the specified order type,
        with valid end dates formatted as 'YYYY-MM'.
"""
    order_file = download_order_dataset('SAP_Report.xlsx')
    order_df = pd.read_excel(BytesIO(order_file))
    filtered_df = order_df[order_df['Main WorkCtr'].str.contains('ZIBE1', na=False)]
    filtered_df = filtered_df[filtered_df['Order Type'] == order_type]
    filtered_df['Date_MMMYY'] = filtered_df[end_date].dt.strftime('%b-%y')
    unique_dates_sorted = sorted(filtered_df[end_date].dt.strftime('%Y-%m').unique())
    month_order = [pd.to_datetime(d).strftime('%b-%y') for d in unique_dates_sorted]
    filtered_df['Date_MMMYY'] = pd.Categorical(filtered_df['Date_MMMYY'], categories=month_order, ordered=True)
    filtered_df = filtered_df.sort_values(by='Date_MMMYY')    
    return filtered_df

def load_notifications():
    """Load and filter SAP notifications based on work center and end date column.
    Returns:
        pd.DataFrame: A filtered DataFrame containing only the specified order type,
        with valid end dates formatted as 'YYYY-MM'.
"""
    notif_file = download_order_dataset('SAP_Notification.xlsx')
    notif_df = pd.read_excel(BytesIO(notif_file))
    filtered_notif_df = notif_df[notif_df['Main WorkCtr'].str.contains('ZIBE1', na=False)]
    filtered_notif_df['Date_MMMYY'] = filtered_notif_df['Notif. Date'].dt.strftime('%b-%y')
    unique_dates_sorted = sorted(filtered_notif_df['Notif. Date'].dt.strftime('%Y-%m').unique())
    month_order = [pd.to_datetime(d).strftime('%b-%y') for d in unique_dates_sorted]
    filtered_notif_df['Date_MMMYY'] = pd.Categorical(filtered_notif_df['Date_MMMYY'], categories=month_order, ordered=True)
    filtered_notif_df = filtered_notif_df.sort_values(by='Date_MMMYY')  
    return filtered_notif_df

def orders_count(order_type):
    """Load and filter SAP work orders based on work center and calculates closed vs total amount.
    Returns:
        String that contains the closed vs total amount and its percentage for completion KPI reference.
"""
    order_file = download_order_dataset('SAP_Report.xlsx')
    order_df = pd.read_excel(BytesIO(order_file))
    filtered_df = order_df[order_df['Main WorkCtr'].str.contains('ZIBE1')]
    filtered_df = filtered_df[filtered_df['Order Type'] == order_type]
    total = (filtered_df[filtered_df['Order Type'] == order_type]).shape[0]
    closed = filtered_df[filtered_df['System status'].str.contains('TECO')].shape[0]
    count = int(closed/total*100)
    total = f'{closed}/{total} = {count}%'
    return total

def notif_count():
    """Load and filter SAP notifications based on work center and calculates closed vs total amount.
    Returns:
        String that contains the closed vs total amount and its percentage for completion KPI reference.
"""
    notif_file = download_order_dataset('SAP_Notification.xlsx')
    order_df = pd.read_excel(BytesIO(notif_file))
    order_df = order_df[order_df['Main WorkCtr'].str.contains('ZIBE1', na=False)]
    total = order_df.shape[0]
    closed = order_df[order_df['System status'].str.contains('DSCL')].shape[0]
    count = int(closed/total*100)
    total = f'{closed}/{total} = {count}%'
    return total