import streamlit as st
from ui.estilo import aplicar_estilo
from views.home import renderizar_home
from views.pacote import renderizar_pacote
from views.funcionarios import renderizar_funcionarios

# Configuração da aba do navegador (Título e Ícone / Favicon)
st.set_page_config(
    page_title="TECH HOME • Automação Residencial de Alto Padrão",
    page_icon="⚡",  # Aqui você pode colocar "⚡", "🏠" ou o caminho de uma imagem PNG sua
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Aplica o design system corporativo
aplicar_estilo()

# Gerenciamento de páginas do app
if "pagina_atual" not in st.session_state:
    st.session_state["pagina_atual"] = "home"

pagina = st.session_state["pagina_atual"]

if pagina == "home":
    renderizar_home()
elif pagina == "pacote":
    renderizar_pacote()
elif pagina == "funcionarios":
    renderizar_funcionarios()