import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Tech Challenge", layout="wide")

# Centralizar título e subtítulo
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

# Centralizar imagem
st.image("images/petroleo.png", width=300)

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

# Criar menu de navegação com ícones
selected = option_menu(
    menu_title=None,
    options=["Introdução", "Objetivo", "Metodologia", "Análise", "Conclusão", "Referências"],
    icons=["house", "bullseye", "tools", "bar-chart", "check-circle", "book"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Redirecionamento para páginas
if selected == "Introdução":
    st.switch_page("pages/1_Introdução.py")
elif selected == "Objetivo":
    st.switch_page("pages/2_Objetivo.py")
elif selected == "Metodologia":
    st.switch_page("pages/3_Metodologia.py")
elif selected == "Análise":
    st.switch_page("pages/4_Analise.py")
elif selected == "Conclusão":
    st.switch_page("pages/5_Conclusão.py")
elif selected == "Referências":
    st.switch_page("pages/6_Referências.py")

# Rodapé com nomes da equipe alinhado à direita
st.markdown(
    """
    <div style="position: fixed; bottom: 10px; right: 20px; text-align: right; font-size: 14px;">
        <b>Equipe:</b><br>
        Francisco das Chagas Alcântara Júnior – RM 357554<br>
        Geovana Façanha da Silva – RM357215<br>
        Luciana Conceição Ferreira – RM357220
    </div>
    """,
    unsafe_allow_html=True
)
