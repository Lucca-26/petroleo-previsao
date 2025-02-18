import streamlit as st
from PIL import Image
import os

# Esconder o menu lateral e configurar a página
st.set_page_config(page_title="Tech Challenge", layout="wide")

# CSS para remover a barra de rolagem
st.markdown(
    """
    <style>
        html, body {
            overflow: hidden !important;
            height: 100%;
            margin: 0;
        }
        .centered-container {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: auto;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Centralizar o título principal
st.markdown(
    """
    <h1 style="text-align: center; color: #1E3A8A;">
        FIAP PÓS TECH – DATA ANALYTICS, 2025
    </h1>
    <h3 style="text-align: center; color: #1E3A8A;">
        Tech Challenge Fase 4 | FIAP | Data Analytics
    </h3>
    """,
    unsafe_allow_html=True
)

# Criar título da seção de botões
st.markdown("<h3 style='text-align: center;'>🚀 Navegue pelas seções:</h3>", unsafe_allow_html=True)

# Criar layout para centralizar os botões e aumentar o tamanho
col1, col2, col3 = st.columns([1, 2, 1])  # Coluna do meio maior para centralizar melhor

with col2:
    st.markdown(
        """
        <style>
        div.stButton > button {
            width: 100%; /* Faz os botões ocuparem toda a largura da coluna */
            height: 50px; /* Aumenta a altura dos botões */
            font-size: 18px; /* Aumenta o tamanho do texto */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Criar botões em uma grade 3x3, alinhados no centro
    col_btn1, col_btn2, col_btn3 = st.columns(3)

    with col_btn1:
        if st.button("📖 Introdução"):
            st.switch_page("pages/1_Introdução.py")

        if st.button("📊 Análise e Insights"):
            st.switch_page("pages/4_Analise.py")

    with col_btn2:
        if st.button("🎯 Objetivo"):
            st.switch_page("pages/2_Objetivo.py")

        if st.button("📡 Modelo"):
            st.switch_page("pages/5_Modelo.py")

    with col_btn3:
        if st.button("🛠 Metodologia"):
            st.switch_page("pages/3_Metodologia.py")

        if st.button("📚 Conclusão"):
            st.switch_page("pages/6_Conclusão.py")

    # Botão de referências centralizado abaixo dos outros
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔍 Referências"):
        st.switch_page("pages/7_Referências.py")

# Rodapé com nomes da equipe alinhado à direita
st.markdown(
    """
    <div style="position: fixed; bottom: 10px; right: 20px; text-align: right; font-size: 14px;">
        <b>Grupo 9 | 6DTAT:</b><br>
        Francisco das Chagas Alcântara Júnior – RM 357554<br>
        Geovana Façanha da Silva – RM357215<br>
        Luciana Conceição Ferreira – RM357220
    </div>
    """,
    unsafe_allow_html=True
)
