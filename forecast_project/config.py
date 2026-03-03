# config.py

BUCKET_NAME = "my-forecast-bucket-123"
INPUT_FILE = "stock_data.csv"

OUTPUT_FILE_PREFIX = "forecast_output"

ARIMA_ORDER = (5, 1, 0)
FORECAST_STEPS = 7