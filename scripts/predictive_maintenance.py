python
import pandas as pd
from fbprophet import Prophet

# Load data
def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Train predictive maintenance model
def train_model(data, date_col, metric_col):
    df = data[[date_col, metric_col]].rename(columns={date_col: 'ds', metric_col: 'y'})
    model = Prophet()
    model.fit(df)
    return model

# Make future predictions
def make_predictions(model, periods=365):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

# Detect anomalies
def detect_anomalies(forecast):
    forecast['anomaly'] = forecast['yhat_upper'] < forecast['y']
    return forecast

if __name__ == "__main__":
    data = load_data('path_to_your_data.csv')
    model = train_model(data, 'date', 'metric')
    forecast = make_predictions(model)
    anomalies = detect_anomalies(forecast)
    print(f"Anomalies detected: {anomalies[anomalies['anomaly']]}")
