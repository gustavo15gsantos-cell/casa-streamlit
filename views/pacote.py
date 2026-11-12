import streamlit as st
from ui.nav import ir_para


def mostrar() -> None:
    st.markdown("<h1 class='titulo'>Monte seu pacote</h1>", unsafe_allow_html=True)
    st.info("Esta página ainda está em construção. Ela será feita na Etapa 3.")
    st.button("VOLTAR", use_container_width=True, on_click=ir_para, args=("home",))
