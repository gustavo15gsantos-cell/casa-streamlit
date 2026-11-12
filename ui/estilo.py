import streamlit as st

def aplicar_estilo():
    st.markdown("""
    <style>
        .stApp {
            background-color: #020617;
            color: #F8FAFC;
        }
        .tech-card {
            background: linear-gradient(145deg, #090D16 0%, #020617 100%);
            border: 1px solid rgba(56, 189, 248, 0.18);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }
        .btn-whatsapp {
            display: block;
            background: linear-gradient(135deg, #059669 0%, #10B981 100%);
            color: white;
            text-align: center;
            padding: 14px 20px;
            border-radius: 12px;
            font-weight: 700;
            text-decoration: none;
            margin-top: 16px;
            box-shadow: 0 4px 15px rgba(16, 185, 129, 0.4);
        }
        .btn-whatsapp:hover {
            opacity: 0.95;
            color: white;
        }
        /* Esconde elementos padrão desnecessários do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

def exibir_logo_tech_home(subtitulo="Infraestrutura Residencial Inteligente"):
    # Cria a logo clicable no topo que redireciona para a home
    if st.button("", key="btn_logo_topo", help="Ir para a Página Inicial"):
        st.session_state["pagina_atual"] = "home"
        if "etapa" in st.session_state:
            st.session_state["etapa"] = 1
        st.rerun()

    st.markdown(f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 16px; margin-bottom: 24px; cursor: pointer;">
        <div style="background: linear-gradient(145deg, #090D16 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 14px; padding: 12px; display: flex; align-items: center; justify-content: center; box-shadow: 0 8px 20px rgba(0,0,0,0.5);">
            <svg width="40" height="40" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect width="64" height="64" rx="16" fill="#020617"/>
                <path d="M22 14C27.5 10 36.5 10 42 14" stroke="#38BDF8" stroke-width="4.5" stroke-linecap="round"/>
                <path d="M12 32L32 16L52 32" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M18 28V50H46V28" stroke="#38BDF8" stroke-width="5.5" stroke-linecap="round" stroke-linejoin="round"/>
                <path d="M34 24L24 37H33L30 48L42 33H33L34 24Z" fill="#FFFFFF"/>
            </svg>
        </div>
        <div>
            <h2 style="color: #FFFFFF; font-size: 1.5rem; font-weight: 800; margin: 0; letter-spacing: 0.5px;">TECH <span style="color: #38BDF8;">HOME</span></h2>
            <p style="color: #94A3B8; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin: 2px 0 0 0;">{subtitulo}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)