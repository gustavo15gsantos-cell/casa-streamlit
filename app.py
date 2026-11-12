import streamlit as st
import os
from ui.estilo import aplicar_estilo
from views.home import renderizar_home
from views.pacote import renderizar_pacote
from views.funcionarios import renderizar_funcionarios

# Verifica se o arquivo de logo existe para usar na aba do navegador
icone_aba = "logo.png" if os.path.exists("logo.png") else "⚡"

# Configuração da aba do navegador com a sua logo real
st.set_page_config(
    page_title="TECH HOME • Automação Residencial de Alto Padrão",
    page_icon=icone_aba,
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