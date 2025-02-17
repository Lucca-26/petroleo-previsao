import streamlit as st

st.set_page_config(page_title="Objetivo", page_icon="🎯")

st.title("🎯 Objetivo")
st.write(
    """
    O objetivo deste projeto é desenvolver um modelo de Machine Learning para prever o preço diário do petróleo Brent, 
    utilizando dados históricos para identificar padrões e tendências que possam auxiliar na tomada de decisão.
    """
)
# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Ir Para Metodologia"):
        st.switch_page("pages/3_Metodologia.py")
