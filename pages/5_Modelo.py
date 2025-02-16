import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Modelo", page_icon="📈")

st.title("📈 Modelo de Previsão")

# Coletar os dados diretamente do Yahoo Finance
brent_data = yf.Ticker("BZ=F").history(period="max")
brent_data.reset_index(inplace=True)

# Treinar o modelo de Regressão Linear
brent_data['Target'] = brent_data['Close'].shift(-1)
X = brent_data[['Open', 'High', 'Low', 'Close']].dropna()
y = brent_data['Target'].dropna()

model = LinearRegression()
model.fit(X, y)

# Previsão para os próximos 7 dias
last_7_days = X.iloc[-7:]
predictions = model.predict(last_7_days)

# Exibir previsões
st.write("### Previsão para os Próximos 7 Dias")
st.write(predictions)

# Gráfico interativo
fig = px.line(brent_data, x="Date", y="Close", title="Previsão do Modelo Linear")
st.plotly_chart(fig)