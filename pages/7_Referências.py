import streamlit as st

st.set_page_config(page_title="Referências", page_icon="📚")

st.title("📚 Referências")
st.write(
    """
    ## Modelos de Previsão
    
    *   **Forecasting: Principles and Practice (2nd ed) by Rob J Hyndman and George Athanasopoulos**
        *   Descrição: Um livro completo sobre métodos de previsão, incluindo modelos de séries temporais como ARIMA, Exponential Smoothing e redes neurais.
        *   Link: [https://otexts.com/fpp2/](https://otexts.com/fpp2/)
    *   **Time Series Forecasting with Deep Learning: A Review by Ismail Fawaz, et al.**
        *   Descrição: Uma revisão abrangente sobre o uso de deep learning para previsão de séries temporais, incluindo RNNs, LSTMs e Transformers.
        *   Link: [https://arxiv.org/abs/1911.09362](https://arxiv.org/abs/1911.09362)
    *   **A Gentle Introduction to Long Short-Term Memory Networks by Jason Brownlee**
        *   Descrição: Uma introdução prática às redes LSTM, um tipo de rede neural recorrente frequentemente usado para previsão de séries temporais.
        *   Link: [https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks/](https://machinelearningmastery.com/gentle-introduction-long-short-term-memory-networks/)
    
    ---
    
    ## Eventos no Mercado de Petróleo
    
    *   **U.S. Energy Information Administration (EIA)**
        *   Descrição: A EIA fornece dados, análises e previsões sobre energia, incluindo petróleo.
        *   Link: [https://www.eia.gov/](https://www.eia.gov/)
    *   **Organization of the Petroleum Exporting Countries (OPEC)**
        *   Descrição: O site da OPEC fornece informações sobre a produção, preços e políticas de petróleo dos países membros.
        *   Link: [https://www.opec.org/](https://www.opec.org/)
    *   **What Drives Crude Oil Prices? by Atil Kılınç**
        *   Descrição: Este artigo discute os fatores que influenciam os preços do petróleo, incluindo oferta e demanda, eventos geopolíticos e especulação.
        *   Link: [https://www.investopedia.com/articles/economics/08/determining-oil-prices.asp](https://www.investopedia.com/articles/economics/08/determining-oil-prices.asp)
    
    ---
    
    ## Utilização do GitHub
    
    *   **GitHub Docs**
        *   Descrição: A documentação oficial do GitHub, com guias sobre como usar o Git, criar repositórios, colaborar e gerenciar projetos.
        *   Link: [https://docs.github.com/](https://docs.github.com/)
    *   **Pro Git by Scott Chacon and Ben Straub**
        *   Descrição: Um livro completo sobre o Git, com explicações detalhadas sobre todos os comandos e funcionalidades.
        *   Link: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
    
    ---
    
    ## Utilização do Streamlit
    
    *   **Streamlit Docs**
        *   Descrição: A documentação oficial do Streamlit, com guias sobre como criar aplicativos interativos, usar widgets e implantar no Streamlit Cloud.
        *   Link: [https://docs.streamlit.io/](https://docs.streamlit.io/)
    *   **Streamlit — The Fastest Way to Build and Share Data Apps by Adrien Treuille, et al.**
        *   Descrição: O artigo original que introduz o Streamlit, descrevendo sua arquitetura e funcionalidades.
        *   Link: [https://arxiv.org/abs/1910.11824](https://arxiv.org/abs/1910.11824)
    
    ---
    
    ## Outras Ferramentas e Bibliotecas
    
    *   **Pandas**
        *   Descrição: Documentação oficial da biblioteca Pandas, utilizada para manipulação e análise de dados.
        *   Link: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)
    *   **Scikit-learn**
        *   Descrição: Documentação oficial da biblioteca Scikit-learn, utilizada para modelos de machine learning.
        *   Link: [https://scikit-learn.org/stable/documentation.html](https://scikit-learn.org/stable/documentation.html)
    *   **Plotly**
        *   Descrição: Documentação oficial da biblioteca Plotly, utilizada para visualização de dados.
        *   Link: [https://plotly.com/python/](https://plotly.com/python/)
    *   **Yfinance**
        *   Descrição: Página do projeto yfinance no PyPI, utilizada para obter dados financeiros do Yahoo Finance.
        *   Link: [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)
    
    ---
    
    ## Referências Adicionais (Específicas do Projeto)
    
    1.  Dados históricos do Brent Crude Oil: [Yahoo Finance](https://finance.yahoo.com/).
    2.  Impactos geopolíticos no preço do petróleo: [Artigo da Reuters](https://www.reuters.com/).
    3.  Crise de 2008: [Publicação no IMF](https://www.imf.org/).
    """
)

# Botões de navegação
col1 = st.columns([1])[0]  # Acessar o primeiro elemento da lista

with col1:
    if st.button("⬅ Ir para Menu"):
        st.switch_page("main.py")