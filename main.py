import streamlit as st

# Configuração da página
st.set_page_config(page_title="Previsão do Petróleo", page_icon="⛽", layout="wide")

# Esconder menu lateral e rodapé
hide_menu_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        button {
            font-size: 20px !important;
            padding: 15px !important;
            width: 100% !important;
            border-radius: 10px !important;
        }
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Título centralizado
st.markdown("<h1 style='text-align: center;'>⛽ Previsão do Petróleo</h1>", unsafe_allow_html=True)
st.write("<h4 style='text-align: center;'>Bem-vindo ao painel interativo de análise da previsão do petróleo Brent.</h4>", unsafe_allow_html=True)

# Exibir a imagem centralizada com tamanho fixo
col_img, col_space, col_img2 = st.columns([4, 3, 2])

with col_space:
    st.image("images/petroleo.png", width=200)  # Ajuste o tamanho conforme necessário

st.write("### 🚀 Navegue pelas seções:")

# Criando layout com colunas para alinhar os botões
col1, col2, col3 = st.columns(3)

# Primeira linha de botões
with col1:
    if st.button("📖 Introdução"):
        st.switch_page("pages/1_Introdução.py")

    if st.button("📊 Análise"):
        st.switch_page("pages/4_Analise.py")

with col2:
    if st.button("🎯 Objetivo"):
        st.switch_page("pages/2_Objetivo.py")

    if st.button("📡 Modelo"):
        st.switch_page("pages/5_Modelo.py")

with col3:
    if st.button("🛠 Metodologia"):
        st.switch_page("pages/3_Metodologia.py")

    if st.button("📚 Conclusão"):
        st.switch_page("pages/6_Conclusão.py")

    if st.button("🔍 Referências"):
        st.switch_page("pages/7_Referências.py")
