import streamlit as st
from ui.estilo import aplicar_estilo
from views.home import renderizar_home
from views.pacote import renderizar_pacote
from views.funcionarios import renderizar_funcionarios

# Logo oficial da TECH HOME em SVG embutido diretamente (não depende de arquivo externo e nunca falha!)
icone_tech_home = """data:image/svg+xml;utf8,<svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="64" height="64" rx="16" fill="%23020617"/><path d="M22 14C27.5 10 36.5 10 42 14" stroke="%2338BDF8" stroke-width="4.5" stroke-linecap="round"/><path d="M12 32L32 16L52 32" stroke="%2338BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M18 28V50H46V28" stroke="%2338BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 24L24 37H33L30 48L42 33H33L34 24Z" fill="%23FFFFFF"/></svg>"""

# Configuração da aba do navegador com a logo oficial
st.set_page_config(
    page_title="TECH HOME • Automação Residencial de Alto Padrão",
    page_icon=icone_tech_home,
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