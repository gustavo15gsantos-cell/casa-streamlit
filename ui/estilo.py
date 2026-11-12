import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
        /* Importação de fontes profissionais */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

        /* Configuração global do App */
        .stApp {
            background: #020617;
            color: #F8FAFC;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }

        /* Container principal centralizado e espaçado */
        .block-container {
            max-width: 680px;
            padding-top: 3rem;
            padding-bottom: 5rem;
        }

        /* Ocultar elementos nativos de rodapé e menu do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Cartões Corporativos de Alta Fidelidade (Glassmorphism Avançado) */
        .tech-card {
            background: linear-gradient(145deg, rgba(15, 23, 42, 0.9) 0%, rgba(2, 6, 23, 0.95) 100%);
            border: 1px solid rgba(56, 189, 248, 0.15);
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 10px 40px -10px rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(16px);
            transition: all 0.3s ease;
        }
        .tech-card:hover {
            border-color: rgba(56, 189, 248, 0.35);
            box-shadow: 0 15px 50px -10px rgba(56, 189, 248, 0.15);
        }

        .tech-card-active {
            background: linear-gradient(145deg, rgba(30, 41, 59, 0.95) 0%, rgba(15, 23, 42, 1) 100%);
            border: 2px solid #38BDF8;
            border-radius: 20px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 0 30px rgba(56, 189, 248, 0.3);
        }

        /* Caixas informativas de destaque */
        .info-box-blue {
            background: rgba(56, 189, 248, 0.08);
            color: #7DD3FC;
            border-left: 4px solid #38BDF8;
            border-radius: 12px;
            padding: 16px 20px;
            font-size: 0.92rem;
            font-weight: 500;
            margin: 20px 0;
            border-top: 1px solid rgba(56, 189, 248, 0.15);
            border-right: 1px solid rgba(56, 189, 248, 0.15);
            border-bottom: 1px solid rgba(56, 189, 248, 0.15);
        }

        /* Botões principais com gradiente executivo */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
            color: white;
            border: none;
            border-radius: 14px;
            padding: 0.85rem 1.2rem;
            font-weight: 700;
            font-size: 1rem;
            letter-spacing: 0.3px;
            box-shadow: 0 6px 20px rgba(2, 132, 199, 0.35);
            transition: all 0.25s ease;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #38BDF8 0%, #0284C7 100%);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.6);
            transform: translateY(-2px);
            color: white;
        }

        /* Botão do WhatsApp em alta conversão corporativa */
        .btn-whatsapp {
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: #FFFFFF !important;
            text-align: center;
            text-decoration: none !important;
            font-weight: 700;
            padding: 16px 20px;
            border-radius: 14px;
            font-size: 1.02rem;
            box-shadow: 0 8px 25px rgba(5, 150, 105, 0.45);
            margin-top: 16px;
            transition: all 0.25s ease;
        }
        .btn-whatsapp:hover {
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            box-shadow: 0 0 30px rgba(16, 185, 129, 0.7);
            transform: translateY(-2px);
        }

        /* Status Badges */
        .badge-pendente {
            background-color: rgba(217, 119, 6, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(217, 119, 6, 0.4);
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
        }
        .badge-confirmado {
            background-color: rgba(2, 132, 199, 0.15);
            color: #38BDF8;
            border: 1px solid rgba(2, 132, 199, 0.4);
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 700;
        }

        /* Campos de texto personalizados */
        .stTextInput > div > div > input {
            background-color: #0F172A;
            color: #F8FAFC;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 12px;
            font-size: 0.95rem;
        }
        .stTextInput > div > div > input:focus {
            border-color: #38BDF8;
            box-shadow: 0 0 15px rgba(56, 189, 248, 0.25);
        }
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Enterprise Smart Home Infrastructure"):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 28px;">
            <div style="background: linear-gradient(135deg, #0284C7 0%, #0F172A 100%); padding: 12px; border-radius: 16px; box-shadow: 0 8px 25px rgba(2,132,199,0.3);">
                <svg width="34" height="34" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M22 14C27.5 10 36.5 10 42 14" stroke="#38BDF8" stroke-width="4.5" stroke-linecap="round"/>
                    <path d="M12 32L32 16L52 32" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M18 28V50H46V28" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M34 24L24 37H33L30 48L42 33H33L34 24Z" fill="#FFFFFF"/>
                </svg>
            </div>
            <div>
                <div style="line-height: 1.1;">
                    <span style="font-size: 1.75rem; font-weight: 800; color: #38BDF8; letter-spacing: 0.5px;">TECH</span>
                    <span style="font-size: 1.75rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.5px;"> HOME</span>
                </div>
                <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 4px;">
                    {subtitulo}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Home", key="btn_topo_home"):
            st.session_state["pagina_atual"] = "home"
            if "etapa" in st.session_state:
                st.session_state["etapa"] = 1
            st.rerun()