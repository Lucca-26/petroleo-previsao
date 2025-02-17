import streamlit as st

st.set_page_config(page_title="Introdução", page_icon="📖")

st.title("📖 Introdução")
st.write("""
O mercado de petróleo é marcado por oscilações significativas causadas por crises econômicas, tensões geopolíticas, 
mudanças na demanda global e avanços nas energias renováveis.
""")

# Botões de navegação
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("⬅ Voltar"):
        st.switch_page("main.py")

with col2:
    if st.button("➡ Próximo"):
        st.switch_page("pages/2_Objetivo.py")
