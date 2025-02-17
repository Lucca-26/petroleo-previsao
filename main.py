import streamlit as st

# Esconder o menu lateral
st.set_page_config(page_title="Tech Challenge", layout="wide")

# Centralizar o título principal
st.markdown(
    """
    <h1 style="text-align: center; color: #1E3A8A;">
        FIAP PÓS TECH – DATA ANALYTICS, 2024
    </h1>
    <h3 style="text-align: center; color: #1E3A8A;">
        Tech Challenge Fase 4 | FIAP | Data Analytics
    </h3>
    """,
    unsafe_allow_html=True
)

# Adicionar imagem centralizada
st.image("images/petroleo.png", width=400)

# Exibir informações da equipe com layout estruturado
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; margin-top: 20px;">
        <b>Equipe:</b><br>
        Francisco das Chagas Alcântara Júnior – RM 357554<br>
        Geovana Façanha da Silva – RM357215<br>
        Luciana Conceição Ferreira – RM357220
    </div>
    """,
    unsafe_allow_html=True
)

# Criar botões alinhados no centro
st.markdown("<br>", unsafe_allow_html=True)  # Espaço entre os elementos

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Introdução", use_container_width=True):
        st.switch_page("pages/1_Introdução.py")
with col2:
    if st.button("Objetivo", use_container_width=True):
        st.switch_page("pages/2_Objetivo.py")
with col3:
    if st.button("Metodologia", use_container_width=True):
        st.switch_page("pages/3_Metodologia.py")

col4, col5, col6 = st.columns(3)
with col4:
    if st.button("Análise", use_container_width=True):
        st.switch_page("pages/4_Analise.py")
with col5:
    if st.button("Conclusão", use_container_width=True):
        st.switch_page("pages/5_Conclusão.py")
with col6:
    if st.button("Referências", use_container_width=True):
        st.switch_page("pages/6_Referências.py")
