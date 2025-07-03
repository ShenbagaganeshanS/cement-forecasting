import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go

# Load and prepare data
df = pd.read_csv("cement_bag_loading_data.csv")
df.columns = [col.strip().lower() for col in df.columns]
df = df.rename(columns={"date": "ds", "count": "y"})
df['ds'] = pd.to_datetime(df['ds'])
df['y'] = pd.to_numeric(df['y'])

# Train model
model = Prophet()
model.fit(df)

# Make forecast for next 7 days
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# Split forecast into past and future
historical = forecast[forecast['ds'] <= df['ds'].max()]
future_forecast = forecast[forecast['ds'] > df['ds'].max()]

# Plot using Plotly manually
fig = go.Figure()

# Actual data line
fig.add_trace(go.Scatter(
    x=df['ds'],
    y=df['y'],
    mode='lines+markers',
    name='Actual',
    line=dict(color='blue')
))

# Forecasted (future) line
fig.add_trace(go.Scatter(
    x=future_forecast['ds'],
    y=future_forecast['yhat'],
    mode='lines+markers',
    name='Forecast',
    line=dict(color='green', dash='dash')  # Dashed green line
))

# Confidence interval
fig.add_trace(go.Scatter(
    x=future_forecast['ds'],
    y=future_forecast['yhat_upper'],
    mode='lines',
    line=dict(width=0),
    showlegend=False
))
fig.add_trace(go.Scatter(
    x=future_forecast['ds'],
    y=future_forecast['yhat_lower'],
    mode='lines',
    fill='tonexty',
    fillcolor='rgba(0, 255, 0, 0.1)',  # light green
    line=dict(width=0),
    showlegend=False
))

# Layout
fig.update_layout(
    title="Cement Bag Count Forecast",
    xaxis_title="Date",
    yaxis_title="Bag Count",
    template="plotly_white"
)

# Show plot
fig.show()
# Print future forecast (last 7 days only)
print("\nNext 7 Days Forecast:")
print(future_forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_string(index=False))
