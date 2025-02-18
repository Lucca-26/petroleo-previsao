import streamlit as st

st.set_page_config(page_title="Objetivo", page_icon="🎯")

st.title("🎯 Objetivo do Projeto")

# Descrição detalhada do objetivo
st.write("""
O objetivo principal deste projeto é desenvolver um modelo de Machine Learning robusto e preciso para prever o preço diário do petróleo Brent.
Para alcançar este objetivo, vamos seguir as seguintes etapas:

1. **Coleta e Pré-Processamento de Dados:**
   - Coletar dados históricos do preço do petróleo Brent de fontes confiáveis, como a API `yfinance`.
   - Limpar e pré-processar os dados, tratando valores ausentes e outliers, para garantir a qualidade dos dados de entrada.

2. **Engenharia de Features:**
   - Criar novas features (variáveis) a partir dos dados existentes, como médias móveis, desvio padrão e variações percentuais, que possam melhorar a capacidade preditiva dos modelos.

3. **Seleção de Modelos:**
   - Avaliar diferentes modelos de Machine Learning, incluindo modelos lineares (como Regressão Linear) e modelos não lineares (como Random Forest, XGBoost e LSTM), para identificar aqueles que melhor se ajustam aos dados.

4. **Treinamento e Validação de Modelos:**
   - Dividir os dados em conjuntos de treinamento e teste para treinar os modelos e avaliar seu desempenho em dados não vistos.
   - Utilizar métricas de avaliação apropriadas, como MAE (Erro Absoluto Médio), RMSE (Raiz do Erro Quadrático Médio) e R² (Coeficiente de Determinação), para quantificar a precisão dos modelos.

5. **Otimização de Hiperparâmetros:**
   - Ajustar os hiperparâmetros dos modelos para otimizar seu desempenho e evitar overfitting (sobreajuste) ou underfitting (subajuste).

6. **Análise de Resultados:**
   - Analisar os resultados dos modelos para identificar os fatores que mais influenciam o preço do petróleo e entender as limitações dos modelos.

7. **Visualização Interativa:**
   - Criar um aplicativo Streamlit interativo que permita aos usuários explorar os dados, visualizar os resultados dos modelos e fazer previsões em diferentes cenários.

Em resumo, o objetivo é fornecer uma ferramenta útil e acessível para entender e prever as oscilações no mercado de petróleo Brent,
utilizando técnicas de Machine Learning e visualização de dados.
""")

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Ir Para Metodologia"):
        st.switch_page("pages/3_Metodologia.py")