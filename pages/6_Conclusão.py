import streamlit as st

st.set_page_config(page_title="Conclusão", page_icon="📝")

st.title("📝 Conclusão")

st.write(
    """
    Este projeto analisa o preço do petróleo Brent ao longo do tempo, identifica padrões históricos e 
    cria um modelo preditivo para ajudar na tomada de decisão. Ele pode ser expandido com mais variáveis, 
    como preço do dólar e indicadores econômicos globais.

    O modelo de Regressão Linear apresentou o melhor desempenho na previsão do preço do petróleo Brent, 
    com um R² de 96.75%. Este projeto demonstrou como fatores econômicos e geopolíticos influenciam diretamente 
    as oscilações no mercado de petróleo.
    """
)

# 🔹 Explicação sobre R² (Coeficiente de Determinação)
with st.expander("📌 O que significa R² (Coeficiente de Determinação)?"):
    st.write(
        """
        O **R²**, ou **coeficiente de determinação**, mede o quão bem um modelo estatístico consegue explicar a 
        variabilidade dos dados. Ele varia de **0 a 1**:
        
        - **R² próximo de 1**: O modelo explica bem os dados.
        - **R² próximo de 0**: O modelo não consegue prever bem os valores.
        
        No contexto deste projeto, um **R² de 96.75%** indica que o modelo consegue explicar **96.75%** 
        da variação no preço do petróleo Brent com base nos fatores analisados.
        
        Para uma explicação mais detalhada, consulte este link: 
        [Wikipedia - Coeficiente de Determinação](https://pt.wikipedia.org/wiki/Coeficiente_de_determinação)
        """
    )

# 🔹 Relacionando com eventos globais
st.subheader("🌍 Eventos Globais e o Impacto no Petróleo")
st.write(
    """
    - **2008 (Crise Financeira Global):** O preço do Brent caiu de **140 USD** (julho) para menos de **40 USD** (dezembro).
    - **2014-2016 (Queda nos preços do petróleo):** Devido ao shale oil nos EUA e à decisão da OPEP, o preço caiu de **115 USD** (junho/2014) para menos de **30 USD** (jan/2016).
    - **2020 (Pandemia de COVID-19):** A demanda despencou e os preços futuros ficaram negativos em abril de 2020, enquanto o Brent ficou abaixo de **20 USD**.
    - **2022 (Invasão da Ucrânia pela Rússia):** O Brent ultrapassou **120 USD** em março devido a sanções e interrupções no fornecimento.
    """
)

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Ir para Menu"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Ir Para Refêrencias"):
        st.switch_page("pages/7_Referências.py")
