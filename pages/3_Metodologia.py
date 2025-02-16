import streamlit as st

st.set_page_config(page_title="Metodologia", page_icon="🛠️")

st.title("🛠️ Metodologia")
st.write(
    """
    Este projeto utilizou as seguintes ferramentas e etapas:
    - **Coleta de Dados**: Utilizamos a biblioteca `yfinance` para obter dados históricos do Brent Crude Oil.
    - **Pré-Processamento**: Tratamos os outliers e adicionamos variáveis derivadas, como médias móveis e variação diária.
    - **Modelagem**: Treinamos modelos como Regressão Linear e LSTM para prever o preço futuro do petróleo.
    - **Visualização**: Criamos gráficos interativos para análise exploratória e previsão.
    """
)