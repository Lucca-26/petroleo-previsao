import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Análise de Eventos no Preço do Petróleo Brent", page_icon="📊")

st.title("📊 Análise de Eventos no Preço do Petróleo Brent")

# Função para obter dados históricos do Brent Crude Oil
@st.cache_data
def get_brent_data():
    brent_data = yf.Ticker("BZ=F").history(period="max")
    brent_data.reset_index(inplace=True)
    brent_data['Date'] = brent_data['Date'].dt.date  # Remover a hora da coluna Date
    return brent_data

# Carregar dados
brent_data = get_brent_data()

# Dicionário de eventos com períodos correspondentes
eventos = {
    "Invasão do Kuwait pelo Iraque (1990)": ("1990-08-02", "1991-03-02"),
    "Invasão do Iraque pelos EUA (2003)": ("2003-03-20", "2003-04-30"),
    "Colapso do Lehman Brothers (2008)": ("2008-09-15", "2008-12-31"),
    "Crise da Dívida Europeia e Avanços no Petróleo de Xisto (2010–2013)": ("2010-01-01", "2013-12-31"),
    "Primavera Árabe (2010–2012)": ("2010-12-18", "2012-12-31"),
    "Acordo de Paris (2015)": ("2015-12-12", "2016-03-31"),
    "Acordo de Corte de Produção da OPEP (2017 em diante)": ("2017-01-01", brent_data['Date'].max().strftime("%Y-%m-%d")),
    "Reimposição de Sanções Econômicas ao Irã (2018–2019)": ("2018-05-08", "2019-12-31"),
    "Ataques a Petroleiros e Tensões Militares (2019)": ("2019-05-01", "2019-12-31"),
    "Lockdowns Globais devido à COVID-19 (2020–2021)": ("2020-03-01", "2021-12-31"),
    "Onze de Setembro (2001)": ("2001-09-11", "2001-09-11")
}

# Sidebar para seleção de eventos
st.sidebar.header("Selecione o Evento")
evento_selecionado = st.sidebar.selectbox("Evento", list(eventos.keys()))

# Filtrar dados com base no evento selecionado
data_inicio, data_fim = eventos[evento_selecionado]
data_inicio = pd.to_datetime(data_inicio).date()
data_fim = pd.to_datetime(data_fim).date()
dados_filtrados = brent_data[(brent_data['Date'] >= data_inicio) & (brent_data['Date'] <= data_fim)]

# Estatísticas gerais
if not dados_filtrados.empty:
    preco_medio = dados_filtrados['Close'].mean()
    preco_maximo = dados_filtrados['Close'].max()
    preco_minimo = dados_filtrados['Close'].min()
else:
    preco_medio = 0
    preco_maximo = 0
    preco_minimo = 0

# Exibir estatísticas
st.write(f"**Período Selecionado:** {data_inicio} até {data_fim}")
st.write(f"**Preço Médio:** ${preco_medio:.2f}")
st.write(f"**Maior Preço:** ${preco_maximo:.2f}")
st.write(f"**Menor Preço:** ${preco_minimo:.2f}")

# Gráfico interativo
fig = px.line(dados_filtrados, x='Date', y='Close', title=f"Preço do Petróleo Brent durante {evento_selecionado}")
st.plotly_chart(fig, use_container_width=True)

# 🔹 Criando os botões de navegação para ir para outra página ou voltar
col1, col2 = st.columns(2)

if col1.button("⬅ Voltar para Início"):
    st.session_state["pagina"] = "main.py"
    st.rerun()

if col2.button("➡ Próxima: Objetivo"):
    st.session_state["pagina"] = "pages/2_Objetivo.py"
    st.rerun()