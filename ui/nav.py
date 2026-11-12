import streamlit as st


def ir_para(pagina: str) -> None:
    """Muda a página atual do site."""
    st.session_state["pagina"] = pagina
