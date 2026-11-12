import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
        /* Fundo geral e tema escuro profissional */
        .stApp {
            background-color: #070B14;
            color: #F8FAFC;
            font-family: 'Inter', sans-serif;
        }
        .block-container {
            max-width: 540px;
            padding-top: 2.2rem;
            padding-bottom: 4rem;
        }
        
        /* Esconder elementos nativos desnecessários */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Cartões com efeito glassmorphism e borda neon sutil */
        .tech-card {
            background: linear-gradient(135deg, rgba(19, 28, 46, 0.8) 0%, rgba(11, 17, 30, 0.95) 100%);
            border: 1px solid rgba(37, 137, 245, 0.2);
            border-radius: 18px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(10px);
        }
        .tech-card-active {
            background: linear-gradient(135deg, rgba(21, 34, 56, 0.95) 0%, rgba(15, 23, 42, 100%) 100%);
            border: 1.5px solid #2589F5;
            border-radius: 18px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 0 20px rgba(37, 137, 245, 0.35);
        }

        /* Caixa de informação estilizada */
        .info-box-blue {
            background: linear-gradient(135deg, rgba(37, 137, 245, 0.15) 0%, rgba(19, 28, 46, 0.4) 100%);
            color: #93C5FD;
            border-left: 4px solid #2589F5;
            border-radius: 12px;
            padding: 14px 16px;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 16px 0;
            border-top: 1px solid rgba(37, 137, 245, 0.2);
            border-right: 1px solid rgba(37, 137, 245, 0.2);
            border-bottom: 1px solid rgba(37, 137, 245, 0.2);
        }

        /* Botões principais com gradiente e efeito neon */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #2589F5 0%, #1D72D4 100%);
            color: white;
            border: none;
            border-radius: 14px;
            padding: 0.75rem 1rem;
            font-weight: 700;
            font-size: 0.98rem;
            letter-spacing: 0.3px;
            box-shadow: 0 4px 15px rgba(37, 137, 245, 0.3);
            transition: all 0.25s ease;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #3B9EFF 0%, #2589F5 100%);
            box-shadow: 0 0 20px rgba(37, 137, 245, 0.6);
            transform: translateY(-1px);
            color: white;
        }

        /* Botão verde estilo WhatsApp altamente chamativo */
        .btn-whatsapp {
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #25D366 0%, #1EBE5D 100%);
            color: #FFFFFF !important;
            text-align: center;
            text-decoration: none !important;
            font-weight: 700;
            padding: 15px 18px;
            border-radius: 14px;
            font-size: 0.98rem;
            box-shadow: 0 6px 20px rgba(37, 211, 102, 0.4);
            margin-top: 12px;
            transition: all 0.25s ease;
        }
        .btn-whatsapp:hover {
            background: linear-gradient(135deg, #2EE872 0%, #25D366 100%);
            box-shadow: 0 0 25px rgba(37, 211, 102, 0.7);
            transform: translateY(-1px);
        }

        /* Badges de status elegantes */
        .badge-pendente {
            background-color: rgba(245, 158, 11, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(245, 158, 11, 0.4);
            padding: 4px 12px;
            border-radius: 10px;
            font-size: 0.78rem;
            font-weight: 700;
        }
        .badge-confirmado {
            background-color: rgba(37, 137, 245, 0.15);
            color: #60A5FA;
            border: 1px solid rgba(37, 137, 245, 0.4);
            padding: 4px 12px;
            border-radius: 10px;
            font-size: 0.78rem;
            font-weight: 700;
        }
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Instalação e configuração de dispositivos com Alexa"):
    # Cabeçalho limpo e clicável usando colunas para voltar à home sem botões feios
    col_logo, col_home = [st.container(), None]
    
    with st.container():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f"""
            <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 22px;">
                <svg width="50" height="50" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M22 10C27.5 6 36.5 6 42 10" stroke="#2589F5" stroke-width="3.5" stroke-linecap="round"/>
                    <path d="M26 15C29.5 12.5 34.5 12.5 38 15" stroke="#2589F5" stroke-width="3.5" stroke-linecap="round"/>
                    <path d="M12 32L32 16L52 32" stroke="#2589F5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M18 28V52H46V28" stroke="#2589F5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M34 25L25 38H33L30 49L40 35H32L34 25Z" fill="#FFFFFF"/>
                </svg>
                <div>
                    <div style="line-height: 1.05;">
                        <span style="font-size: 1.6rem; font-weight: 800; color: #2589F5; letter-spacing: 0.5px;">TECH</span>
                        <span style="font-size: 1.6rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.5px;"> HOME</span>
                    </div>
                    <div style="font-size: 0.8rem; color: #60A5FA; margin-top: 3px;">
                        {subtitulo}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            if st.button("🏠 Início", key="btn_topo_home"):
                st.session_state["pagina_atual"] = "home"
                if "etapa" in st.session_state:
                    st.session_state["etapa"] = 1
                st.rerun()
            