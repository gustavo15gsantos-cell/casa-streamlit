import streamlit as st

def carregar_estilo_global():
    st.markdown("""
    <style>
        /* Fundo geral da aplicação padrão Techflux Dark */
        .stApp {
            background-color: #020617;
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
        }
        
        /* Ocultar cabeçalho, menu e rodapé padrão do Streamlit (remove o 'M' e elementos flutuantes) */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Estilização padrão de Cards Tecnológicos */
        .tech-card {
            background: linear-gradient(145deg, #090D16 0%, #020617 100%);
            border: 1px solid rgba(56, 189, 248, 0.2);
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .tech-card:hover {
            border-color: rgba(56, 189, 248, 0.5);
            box-shadow: 0 15px 35px rgba(56, 189, 248, 0.1);
        }

        /* Estilização da Barra Lateral */
        section[data-testid="stSidebar"] {
            background-color: #050811;
            border-right: 1px solid rgba(56, 189, 248, 0.15);
        }
        
        /* Botões personalizados */
        .stButton button {
            background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
            color: #FFFFFF;
            font-weight: 700;
            border-radius: 10px;
            border: 1px solid rgba(56, 189, 248, 0.4);
            padding: 0.6rem 1.2rem;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.3);
            transition: all 0.3s;
        }
        .stButton button:hover {
            background: linear-gradient(135deg, #0369A1 0%, #075985 100%);
            border-color: #38BDF8;
            box-shadow: 0 6px 20px rgba(56, 189, 248, 0.5);
        }
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Infraestrutura Residencial Inteligente"):
    st.markdown(f"""
    <div style="text-align: center; padding: 10px 0 20px 0;">
        <div style="display: inline-flex; align-items: center; justify-content: center; width: 55px; height: 55px; background: rgba(56, 189, 248, 0.1); border-radius: 16px; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 10px; font-size: 26px;">
            ⚡
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.8rem; font-weight: 800; margin: 0; letter-spacing: 0.5px;">
            TECH <span style="color: #38BDF8;">HOME</span>
        </h1>
        <p style="color: #94A3B8; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 2px; margin-top: 4px; font-weight: 600;">
            {subtitulo}
        </p>
    </div>
    """, unsafe_allow_html=True)