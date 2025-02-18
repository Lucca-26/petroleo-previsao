import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Análise dos Eventos no Preço do Petróleo Brent e Insights", page_icon="📊")

st.title("📊 Análise dos Eventos no Preço do Petróleo Brent e Insights")

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
    "Todos os Eventos": (brent_data['Date'].min().strftime("%Y-%m-%d"), brent_data['Date'].max().strftime("%Y-%m-%d")),
    "Colapso do Lehman Brothers (2008)": ("2008-09-15", "2008-12-31"),
    "Crise da Dívida Europeia e Avanços no Petróleo de Xisto (2010–2013)": ("2010-01-01", "2013-12-31"),
    "Primavera Árabe (2010–2012)": ("2010-12-18", "2012-12-31"),
    "Acordo de Paris (2015)": ("2015-12-12", "2016-03-31"),
    "Acordo de Corte de Produção da OPEP (2017 em diante)": ("2017-01-01", brent_data['Date'].max().strftime("%Y-%m-%d")),
    "Reimposição de Sanções Econômicas ao Irã (2018–2019)": ("2018-05-08", "2019-12-31"),
    "Ataques a Petroleiros e Tensões Militares (2019)": ("2019-05-01", "2019-12-31"),
    "Lockdowns Globais devido à COVID-19 (2020–2021)": ("2020-03-01", "2021-12-31"),
    "Guerra na Ucrânia (2022)": ("2022-02-24", brent_data['Date'].max().strftime("%Y-%m-%d")),
    "Crise Bancária de 2023": ("2023-03-01", "2023-05-01"),
}

# Sidebar para seleção de eventos
st.sidebar.header("Listamos Alguns Eventos")
evento_selecionado = st.sidebar.selectbox("Selecione o Evento", list(eventos.keys()))

# Filtrar dados com base no evento selecionado
data_inicio, data_fim = eventos[evento_selecionado]
data_inicio = pd.to_datetime(data_inicio).date()
data_fim = pd.to_datetime(data_fim).date()

if evento_selecionado == "Todos os Eventos":
    dados_filtrados = brent_data
else:
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
titulo_grafico = "Preço do Petróleo Brent ao Longo do Tempo" if evento_selecionado == "Todos os Eventos" else f"Preço do Petróleo Brent durante {evento_selecionado}"
fig = px.line(dados_filtrados, x='Date', y='Close', title=titulo_grafico)
st.plotly_chart(fig, use_container_width=True)

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Menu Inicial"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Ir Para Modelo"):
        st.switch_page("pages/5_Modelo.py")

# Insights Relevantes Sobre a Variação do Preço do Petróleo
st.markdown("## Insights Relevantes Sobre a Variação do Preço do Petróleo")
st.write("""
A análise dos dados e o contexto histórico mostram que a variação do preço do petróleo é influenciada por uma combinação de fatores econômicos, geopolíticos, de oferta e demanda, e avanços na energia. Abaixo estão os insights mais relevantes:

### 1. Situações Geopolíticas
- **Conflitos e Tensões Geopolíticas**: Eventos como guerras, sanções econômicas e tensões no Oriente Médio impactam diretamente os preços.
  - Exemplo: A Guerra do Golfo (1990-1991) gerou um aumento abrupto nos preços.
  - Conflito Rússia-Ucrânia (2022) causou um salto nos preços devido a sanções.

- **Políticas da OPEP**: A organização controla parte da produção global, influenciando os preços.
  - Exemplo: Em 2020, cortes na produção estabilizaram os preços.

### 2. Crises Econômicas
- **Crise Financeira de 2008**: Reduziu a demanda e levou à queda drástica nos preços.
- **Pandemia de COVID-19 (2020)**: O colapso econômico gerou queda histórica na demanda.

### 3. Demanda Global
- **Atividade Econômica**: O crescimento econômico global impulsiona os preços.
- **Mudanças Sazonais**: Aumento da demanda no inverno e verão pode gerar picos temporários.

### 4. Oferta e Produção
- **Descobertas e Tecnologia**: Fracking nos EUA aumentou a oferta e reduziu os preços.
- **Desastres Naturais**: Furacões podem reduzir a oferta e aumentar preços.

### 5. Transição Energética
- **Energias Renováveis**: A adoção de fontes limpas reduz a demanda por petróleo.
- **Políticas Climáticas**: Acordos internacionais afetam a demanda a longo prazo.

### 6. Comportamento do Mercado
- **Especulação**: Movimentos de investidores exacerbam variações nos preços.
- **Correlação de Variáveis**: O volume tem correlação negativa moderada com os preços.

### Resumo
- Geopolítica e crises econômicas impactam preços no curto prazo.
- A oferta e a demanda global são os maiores direcionadores a longo prazo.
- A transição energética pode reduzir a demanda futuramente.
- O mercado de petróleo é altamente especulativo e volátil.
""")