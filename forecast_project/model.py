# model.py

from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta
import pandas as pd
from config import ARIMA_ORDER, FORECAST_STEPS

def generate_forecast(df):
    df = df.asfreq('D')
    model = ARIMA(df['price'], order=ARIMA_ORDER)
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=FORECAST_STEPS)

    future_dates = [
        df.index[-1] + timedelta(days=i)
        for i in range(1, FORECAST_STEPS + 1)
    ]

    forecast_df = pd.DataFrame({
        "date": future_dates,
        "forecast_price": forecast
    })

    return forecast_df