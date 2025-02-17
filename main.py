import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Configurar o layout do app e renomear o item no menu
st.set_page_config(
    page_title="Tech Challenge Fase 4 | Data Analytics | FIAP",  # Título exibido na aba do navegador
    page_icon="⛽",  # Ícone exibido na aba do navegador
    layout="wide",  # Layout do app
    menu_title="Tech Challenge Fase 4 | Data Analytics | FIAP"  # Nome no menu lateral
)

# Título Principal
st.title("⛽ Eventos Importantes que Afetaram os Preços do Petróleo Brent")

# 🔹 Coletar os dados diretamente do Yahoo Finance
@st.cache_data
def get_brent_data():
    brent_data = yf.Ticker("BZ=F").history(period="max")
    brent_data.reset_index(inplace=True)

    # Remover fuso horário da coluna Date para evitar erros de comparação
    if brent_data['Date'].dtype == "datetime64[ns, America/New_York]":
        brent_data['Date'] = brent_data['Date'].dt.tz_convert(None)

    brent_data['Year'] = brent_data['Date'].dt.year
    return brent_data

brent_data = get_brent_data()

# --- SIDEBAR ---
st.sidebar.header("Filtros")

# 🔹 Filtro por intervalo de anos usando um slider
min_year = int(brent_data['Year'].min())
max_year = int(brent_data['Year'].max())

selected_year_range = st.sidebar.slider(
    "Selecione o intervalo de anos",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# 🔹 Filtragem dos dados baseada no intervalo de anos selecionado
filtered_data = brent_data[
    (brent_data['Year'] >= selected_year_range[0]) & (brent_data['Year'] <= selected_year_range[1])
]

# --- MÉTRICAS ---
col1, col2, col3 = st.columns(3)
col1.metric("Total de Registros", len(filtered_data))
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