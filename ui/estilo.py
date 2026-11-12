import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
        /* Fundo corporativo global (Preto absoluto e azul escuro profundo) */
        .stApp {
            background-color: #030712;
            color: #F3F4F6;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        .block-container {
            max-width: 620px;
            padding-top: 2.5rem;
            padding-bottom: 5rem;
        }
        
        /* Ocultar elementos padrão do Streamlit para visual de App nativo/enterprise */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Cartões estilo Glassmorphism Corporativo */
        .tech-card {
            background: linear-gradient(135deg, rgba(17, 24, 39, 0.85) 0%, rgba(3, 7, 18, 0.95) 100%);
            border: 1px solid rgba(59, 130, 246, 0.15);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            backdrop-filter: blur(12px);
        }
        .tech-card-active {
            background: linear-gradient(135deg, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 1) 100%);
            border: 1.5px solid #3B82F6;
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 18px;
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.25);
        }

        /* Caixas de destaque executivas */
        .info-box-blue {
            background: rgba(37, 99, 235, 0.1);
            color: #93C5FD;
            border-left: 4px solid #3B82F6;
            border-radius: 10px;
            padding: 16px;
            font-size: 0.92rem;
            font-weight: 500;
            margin: 18px 0;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }

        /* Botões de Ação Corporativa */
        .stButton > button {
            width: 100%;
            background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.8rem 1.2rem;
            font-weight: 600;
            font-size: 0.98rem;
            letter-spacing: 0.4px;
            box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
            transition: all 0.2s ease;
        }
        .stButton > button:hover {
            background: linear-gradient(135deg, #3B82F6 0%, #2563EB 100%);
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.6);
            transform: translateY(-1px);
            color: white;
        }

        /* Botão de WhatsApp em alta conversão */
        .btn-whatsapp {
            display: block;
            width: 100%;
            background: linear-gradient(135deg, #059669 0%, #047857 100%);
            color: #FFFFFF !important;
            text-align: center;
            text-decoration: none !important;
            font-weight: 700;
            padding: 16px 20px;
            border-radius: 12px;
            font-size: 1rem;
            box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4);
            margin-top: 14px;
            transition: all 0.2s ease;
        }
        .btn-whatsapp:hover {
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            box-shadow: 0 0 25px rgba(16, 185, 129, 0.6);
            transform: translateY(-1px);
        }

        /* Badges executivos */
        .badge-pendente {
            background-color: rgba(217, 119, 6, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(217, 119, 6, 0.4);
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 600;
        }
        .badge-confirmado {
            background-color: rgba(37, 99, 235, 0.15);
            color: #60A5FA;
            border: 1px solid rgba(37, 99, 235, 0.4);
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Enterprise Smart Home Ecosystem"):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 24px;">
            <svg width="46" height="46" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="64" height="64" rx="14" fill="#0F172A"/>
                <path d="M22 18C27.5 14 36.5 14 42 18" stroke="#3B82F6" stroke-width="3.5" stroke-linecap="round"/>
                <path d="M14 36L32 20L50 36" stroke="#3B82F6" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M20 32V48H44V32" stroke="#3B82F6" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            <div>
                <div style="line-height: 1.1;">
                    <span style="font-size: 1.55rem; font-weight: 800; color: #3B82F6; letter-spacing: 0.5px;">TECH</span>
                    <span style="font-size: 1.55rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.5px;"> HOME</span>
                </div>
                <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; margin-top: 2px;">
                    {subtitulo}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Início", key="btn_topo_home"):
            st.session_state["pagina_atual"] = "home"
            if "etapa" in st.session_state:
                st.session_state["etapa"] = 1
            st.rerun()