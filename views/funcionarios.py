import streamlit as st
from ui.nav import ir_para


def mostrar() -> None:
    st.markdown("<h1 class='titulo'>Área dos funcionários</h1>", unsafe_allow_html=True)
    st.info("O login ainda não existe. Ele será feito na Etapa 4.")
    st.button("VOLTAR", use_container_width=True, on_click=ir_para, args=("home",))
