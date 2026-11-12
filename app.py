import streamlit as st

from config import site
from ui.estilo import aplicar_estilo
from views import funcionarios, home, pacote

st.set_page_config(
    page_title=site.TITULO_ABA,
    page_icon="💡",
    layout="centered",
    initial_sidebar_state="collapsed",
)
aplicar_estilo()

if "pagina" not in st.session_state:
    st.session_state["pagina"] = "home"

PAGINAS = {
    "home": home.mostrar,
    "pacote": pacote.mostrar,
    "funcionarios": funcionarios.mostrar,
}

PAGINAS.get(st.session_state["pagina"], home.mostrar)()
