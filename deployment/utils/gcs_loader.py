from google.cloud import storage
from io import BytesIO

def download_order_dataset(report_name):
    client = storage.Client()
    bucket = client.bucket('operations-dashboard-datasets')
    blob = bucket.blob(report_name)
    return blob.download_as_bytes()