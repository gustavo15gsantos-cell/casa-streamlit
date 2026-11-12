import streamlit as st

CSS = """
<style>
header, footer, #MainMenu {visibility: hidden;}

.block-container {
    max-width: 640px;
    padding: 2rem 1rem 3rem 1rem;
}

.titulo {
    text-align: center;
    font-size: 1.9rem;
    line-height: 1.2;
    font-weight: 800;
    margin: 1rem 0 0.5rem 0;
}
.subtitulo {
    text-align: center;
    color: #b8c4d6;
    margin-bottom: 1.5rem;
}
.card {
    background: #0d1117;
    border: 1px solid #1c2a3d;
    border-left: 4px solid #2f8cff;
    border-radius: 12px;
    padding: 14px 16px;
    margin: 10px 0;
    text-align: center;
}
.espaco { height: 3rem; }

[data-testid="stBaseButton-primary"] {
    background: #2f8cff;
    border: none;
    color: #ffffff;
    font-weight: 700;
    padding: 0.9rem 1rem;
    border-radius: 12px;
}
[data-testid="stBaseButton-tertiary"] {
    color: #6b7686;
    font-size: 0.7rem;
    letter-spacing: 0.08em;
}
</style>
"""


def aplicar_estilo() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
