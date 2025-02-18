import streamlit as st

st.set_page_config(page_title="Referências", page_icon="📚")

st.title("📚 Referências")
st.write(
    """
    1. Dados históricos do Brent Crude Oil: [Yahoo Finance](https://finance.yahoo.com/).
    2. Impactos geopolíticos no preço do petróleo: [Artigo da Reuters](https://www.reuters.com/).
    3. Crise de 2008: [Publicação no IMF](https://www.imf.org/).
    """
)

# Botões de navegação
col1 = st.columns([1])[0]  # Acessar o primeiro elemento da lista

with col1:
    if st.button("⬅ Ir para Menu"):
        st.switch_page("main.py")