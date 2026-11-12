import streamlit as st
from ui.estilo import carregar_estilo_global
from views.home import renderizar_home
from views.pacote import renderizar_pacote
from views.funcionarios import renderizar_funcionarios

st.set_page_config(
    page_title="TECH HOME • Automação Residencial e IoT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

carregar_estilo_global()

# Inicializar estado da página se não existir
if "pagina_atual" not in st.session_state:
    st.session_state["pagina_atual"] = "home"

# Menu lateral de navegação
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h2 style="color: #38BDF8; margin: 0; font-size: 1.4rem;">⚡ TECH HOME</h2>
            <p style="color: #94A3B8; font-size: 0.8rem; margin: 5px 0 0 0;">Infraestrutura Inteligente</p>
        </div>
        <hr style="border-color: rgba(56, 189, 248, 0.2);">
    """, unsafe_allow_html=True)
    
    escolha = st.radio(
        "Navegação",
        ["🏠 Início", "⚙️ Configurar Ecossistema", "🔐 Portal Executivo"],
        label_visibility="collapsed"
    )
    
    if "Início" in escolha:
        st.session_state["pagina_atual"] = "home"
    elif "Configurar" in escolha:
        st.session_state["pagina_atual"] = "pacote"
    elif "Portal" in escolha:
        st.session_state["pagina_atual"] = "funcionarios"

# Renderização baseada no estado atual
pagina = st.session_state.get("pagina_atual", "home")

if pagina == "home":
    renderizar_home()
elif pagina == "pacote":
    renderizar_pacote()
elif pagina == "funcionarios":
    renderizar_funcionarios()