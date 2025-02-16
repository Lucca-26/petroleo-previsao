import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Análise", page_icon="📊")

st.title("📊 Análise de Dados")

# Coletar os dados diretamente do Yahoo Finance
brent_data = yf.Ticker("BZ=F").history(period="max")
brent_data.reset_index(inplace=True)
brent_data['Year'] = brent_data['Date'].dt.year

# Filtros interativos
st.sidebar.header("Filtros")
start_date, end_date = st.sidebar.date_input("Selecione o Período", 
                                             value=(brent_data['Date'].min(), brent_data['Date'].max()),
                                             min_value=brent_data['Date'].min(),
                                             max_value=brent_data['Date'].max())
eventos = st.sidebar.selectbox("Selecione o Evento", ["Todos", "Crises Econômicas", "Conflitos Geopolíticos"])

# Filtrar os dados
filtered_data = brent_data[(brent_data['Date'] >= pd.to_datetime(start_date)) & 
                           (brent_data['Date'] <= pd.to_datetime(end_date))]

# Gráfico interativo
fig = px.line(filtered_data, x="Date", y="Close", title="Preço Histórico do Petróleo Brent")
st.plotly_chart(fig)

# Estatísticas gerais
col1, col2, col3 = st.columns(3)
col1.metric("Preço Médio", f"${filtered_data['Close'].mean():.2f}")
col2.metric("Maior Preço", f"${filtered_data['Close'].max():.2f}")
col3.metric("Menor Preço", f"${filtered_data['Close'].min():.2f}")