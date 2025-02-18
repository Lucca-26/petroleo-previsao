import streamlit as st

st.set_page_config(page_title="Introdução", page_icon="📖")

st.title("📖 Introdução")

# Introdução sobre o projeto e o mercado de petróleo
st.write("""
O mercado de petróleo é um dos mais dinâmicos e influentes do mundo, com impactos que se estendem desde a economia global até a geopolítica e o meio ambiente.
As oscilações nos preços do petróleo Brent, uma das principais referências globais, são influenciadas por uma complexa interação de fatores, incluindo:

- **Tensões Geopolíticas:** Conflitos, sanções e instabilidades em regiões produtoras de petróleo podem interromper o fornecimento e elevar os preços.
- **Crises Econômicas:** Recessões e desacelerações econômicas reduzem a demanda por petróleo, levando a quedas nos preços.
- **Oferta e Demanda Global:** A produção de petróleo, controlada por países e organizações como a OPEP, e a demanda, impulsionada pelo crescimento econômico e padrões de consumo, desempenham um papel crucial na determinação dos preços.
- **Avanços Tecnológicos e Energias Renováveis:** A transição para fontes de energia mais limpas e os avanços na eficiência energética afetam a demanda de longo prazo por petróleo.
- **Especulação do Mercado:** O mercado de futuros de petróleo é suscetível a movimentos especulativos que podem amplificar as variações nos preços.

Este projeto tem como objetivo fornecer uma análise abrangente e acessível das oscilações no mercado de petróleo Brent, utilizando dados históricos e modelos de Machine Learning para identificar padrões, tendências e fatores de influência.

Especificamente, buscamos:

1. **Coletar e Organizar Dados:** Reunir dados históricos do preço do petróleo Brent, bem como informações sobre eventos geopolíticos, indicadores econômicos e outros fatores relevantes.
2. **Analisar Tendências e Padrões:** Identificar as principais tendências e padrões nos preços do petróleo ao longo do tempo, utilizando técnicas de visualização e análise estatística.
3. **Desenvolver Modelos de Previsão:** Construir e avaliar modelos de Machine Learning para prever os preços futuros do petróleo, com base em dados históricos e fatores de influência identificados.
4. **Visualizar Resultados de Forma Interativa:** Criar um aplicativo Streamlit que permita aos usuários explorar os dados, analisar os modelos e visualizar as previsões de forma intuitiva e interativa.
""")

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Próximo"):
        st.switch_page("pages/2_Objetivo.py")