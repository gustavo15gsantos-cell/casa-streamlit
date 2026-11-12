import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
        /* Fundo geral e remoção de margens excessivas */
        .stApp {
            background-color: #0B111E;
            color: #F8FAFC;
        }
        .block-container {
            max-width: 520px;
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }
        /* Esconder menu padrão do Streamlit para parecer um App nativo */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Cartões escuros com borda sutil azul */
        .tech-card {
            background: linear-gradient(145deg, #131C2E 0%, #0F172A 100%);
            border: 1px solid #1E293B;
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 14px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
        }
        .tech-card-active {
            background: linear-gradient(145deg, #152238 0%, #0F172A 100%);
            border: 1.5px solid #2589F5;
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 14px;
            box-shadow: 0 0 15px rgba(37, 137, 245, 0.25);
        }

        /* Caixa de informação azul clara (igual à etapa da Fita LED) */
        .info-box-blue {
            background-color: #DBEAFE;
            color: #1E3A8A;
            border-left: 5px solid #2589F5;
            border-radius: 12px;
            padding: 14px 16px;
            font-size: 0.9rem;
            font-weight: 500;
            margin: 16px 0;
        }

        /* Botões principais azuis */
        .stButton > button {
            width: 100%;
            background-color: #2589F5;
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.65rem 1rem;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }
        .stButton > button:hover {
            background-color: #1D72D4;
            box-shadow: 0 0 12px rgba(37, 137, 245, 0.45);
            color: white;
        }

        /* Botão verde estilo WhatsApp */
        .btn-whatsapp {
            display: block;
            width: 100%;
            background-color: #25D366;
            color: #FFFFFF !important;
            text-align: center;
            text-decoration: none !important;
            font-weight: 700;
            padding: 14px 18px;
            border-radius: 12px;
            font-size: 0.95rem;
            box-shadow: 0 4px 14px rgba(37, 211, 102, 0.3);
            margin-top: 10px;
        }
        .btn-whatsapp:hover {
            background-color: #1EBE5D;
        }

        /* Badges de status (Funcionários) */
        .badge-pendente {
            background-color: rgba(245, 158, 11, 0.15);
            color: #FBBF24;
            border: 1px solid rgba(245, 158, 11, 0.4);
            padding: 3px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 600;
        }
        .badge-confirmado {
            background-color: rgba(37, 137, 245, 0.15);
            color: #60A5FA;
            border: 1px solid rgba(37, 137, 245, 0.4);
            padding: 3px 10px;
            border-radius: 8px;
            font-size: 0.78rem;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Instalação e configuração de dispositivos com Alexa"):
    st.markdown(f"""
    <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 18px;">
        <svg width="52" height="52" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M22 10C27.5 6 36.5 6 42 10" stroke="#2589F5" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M26 15C29.5 12.5 34.5 12.5 38 15" stroke="#2589F5" stroke-width="3.5" stroke-linecap="round"/>
            <path d="M12 32L32 16L52 32" stroke="#2589F5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M18 28V52H46V28" stroke="#2589F5" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
            <path d="M34 25L25 38H33L30 49L40 35H32L34 25Z" fill="#FFFFFF"/>
        </svg>
        <div>
            <div style="line-height: 1.05;">
                <span style="font-size: 1.65rem; font-weight: 800; color: #2589F5; letter-spacing: 0.5px;">TECH</span>
                <span style="font-size: 1.65rem; font-weight: 800; color: #FFFFFF; letter-spacing: 0.5px;"> HOME</span>
            </div>
            <div style="font-size: 0.82rem; color: #60A5FA; margin-top: 3px;">
                {subtitulo}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)