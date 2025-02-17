import streamlit as st

# Configuração da página
st.set_page_config(page_title="Previsão do Petróleo", page_icon="⛽", layout="wide")

# Ocultando o menu lateral e rodapé do Streamlit
hide_menu = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Título da página inicial
st.title("⛽ Previsão do Petróleo")
st.write("Bem-vindo ao painel interativo de análise da previsão do petróleo Brent.")

# Botões para direcionar às páginas dentro da pasta `pages/`
st.markdown("### 📌 Navegue pelas seções:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Introdução"):
        st.switch_page("pages/1_Introdução.py")

with col2:
    if st.button("Metodologia"):
        st.switch_page("pages/3_Metodologia.py")

with col3:
    if st.button("Análise"):
        st.switch_page("pages/4_Análise.py")
