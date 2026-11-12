import streamlit as st
from config import site
from ui.nav import ir_para


def mostrar() -> None:
    st.markdown(f"<h1 class='titulo'>{site.TITULO_PRINCIPAL}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p class='subtitulo'>{site.SUBTITULO}</p>", unsafe_allow_html=True)

    for item in site.BENEFICIOS:
        st.markdown(f"<div class='card'>{item}</div>", unsafe_allow_html=True)

    st.write("")
    st.button(
        site.TEXTO_BOTAO_PRINCIPAL,
        type="primary",
        use_container_width=True,
        on_click=ir_para,
        args=("pacote",),
    )

    st.markdown("<div class='espaco'></div>", unsafe_allow_html=True)
    st.button(
        site.TEXTO_BOTAO_FUNCIONARIOS,
        type="tertiary",
        use_container_width=True,
        key="botao_funcionarios",
        on_click=ir_para,
        args=("funcionarios",),
    )
