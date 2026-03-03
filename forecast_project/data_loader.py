# data_loader.py

import pandas as pd
import io
from google.cloud import storage
from config import BUCKET_NAME, INPUT_FILE, OUTPUT_FILE_PREFIX

def download_data():
    client = storage.Client(project="project-cfd0578a-68eb-49ae-82d")
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(INPUT_FILE)

    data = blob.download_as_text()
    df = pd.read_csv(io.StringIO(data))
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)

    return df

from datetime import datetime

def upload_forecast(forecast_df):
    client = storage.Client(project="project-cfd0578a-68eb-49ae-82d" )
    bucket = client.bucket(BUCKET_NAME)

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    output_file = f"{OUTPUT_FILE_PREFIX}_{timestamp}.csv"

    output_blob = bucket.blob(output_file)

    buffer = io.StringIO()
    forecast_df.to_csv(buffer, index=False)

    output_blob.upload_from_string(
        buffer.getvalue(),
        content_type="text/csv"
    )

def upload_forecast_local(forecast_df):
    forecast_df.to_csv('output_1.csv', index=False)

def download_data_local():
    df = pd.read_csv('stock_data.csv')
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df
