import streamlit as st
from ui.estilo import aplicar_estilo
from views.home import renderizar_home
from views.pacote import renderizar_pacote
from views.funcionarios import renderizar_funcionarios

# Configuração inicial da página mobile-first
st.set_page_config(
    page_title="TECH HOME - Automação Residencial",
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Aplica o design dark moderno e identidade visual
aplicar_estilo()

# Gerenciador de navegação entre as telas do site
if "pagina_atual" not in st.session_state:
    st.session_state["pagina_atual"] = "home"

pagina = st.session_state["pagina_atual"]

if pagina == "home":
    renderizar_home()
elif pagina == "pacote":
    renderizar_pacote()
elif pagina == "funcionarios":
    renderizar_funcionarios()
else:
    renderizar_home()