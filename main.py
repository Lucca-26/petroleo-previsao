import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Configurar o layout do app
st.set_page_config(page_title="Eventos no Preço do Petróleo Brent", page_icon="⛽", layout="wide")

# Título Principal
st.title("⛽ Eventos Importantes que Afetaram os Preços do Petróleo Brent")

# Coletar os dados diretamente do Yahoo Finance
@st.cache
def get_brent_data():
    brent_data = yf.Ticker("BZ=F").history(period="max")
    brent_data.reset_index(inplace=True)
    brent_data['Year'] = brent_data['Date'].dt.year
    return brent_data

brent_data = get_brent_data()

# --- SIDEBAR ---
st.sidebar.header("Filtros")

# Filtro de data
start_date, end_date = st.sidebar.date_input(
    "Selecione o Período",
    value=(brent_data['Date'].min(), brent_data['Date'].max()),
    min_value=brent_data['Date'].min(),
    max_value=brent_data['Date'].max(),
)

# Filtro de eventos
eventos = st.sidebar.selectbox(
    "Selecione o Evento",
    ["Todos", "Crises Econômicas", "Conflitos Geopolíticos", "Mudança na Demanda"],
)

# --- FILTRAR DADOS ---
filtered_data = brent_data[
    (brent_data['Date'] >= pd.to_datetime(start_date)) & (brent_data['Date'] <= pd.to_datetime(end_date))
]

# --- MÉTRICAS ---
col1, col2, col3 = st.columns(3)
col1.metric("Eventos", len(filtered_data))
col2.metric("Maior Preço", f"${filtered_data['Close'].max():.2f}")
col3.metric("Menor Preço", f"${filtered_data['Close'].min():.2f}")

# --- GRÁFICO INTERATIVO ---
fig = px.line(
    filtered_data,
    x="Date",
    y="Close",
    title="Preço Histórico do Petróleo Brent",
    labels={"Close": "Preço de Fechamento (USD)", "Date": "Data"},
)
fig.update_traces(line_color="cyan")
st.plotly_chart(fig, use_container_width=True)

# --- CONCLUSÕES ---
st.markdown("### Conclusões")
st.write(
    """
    O gráfico acima permite observar eventos que impactaram os preços do petróleo Brent ao longo do tempo.
    Utilize os filtros laterais para explorar diferentes períodos e categorias de eventos.
    """
)