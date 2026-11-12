import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    exibir_logo_tech_home("Global Smart Infrastructure")

    # Banner Multinacional de Alto Impacto
    st.markdown("""
    <div style="background: linear-gradient(145deg, #0F172A 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 24px; padding: 28px; margin-bottom: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.7);">
        <div style="width: 100%; height: 220px; border-radius: 16px; overflow: hidden; margin-bottom: 20px; background-color: #020617; border: 1px solid rgba(255,255,255,0.08);">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;" alt="Smart Ecosystem">
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 5px 12px; border-radius: 8px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
            Enterprise Division
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.8rem; font-weight: 800; line-height: 1.25; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.98rem; line-height: 1.6; margin-bottom: 24px;">
            Arquitetura IoT proprietária, iluminação arquitetônica de precisão e assistentes de voz integrados para residências exclusivas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Chamada Principal
    if st.button("🚀 INICIAR CONFIGURAÇÃO DE ECOSSISTEMA", key="btn_monte_pacote"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Seção de Pilares Tecnológicos
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 14px;">Pilares Tecnológicos</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">💡</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Smart LED</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">🔌</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Power Grid</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">🎙️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Voice AI</div></div>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">⚙️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Custom Solutions</div></div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">🛡️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Enterprise Security</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Portal Corporativo (Área de Funcionários)
    col_centro = st.columns([1, 2, 1])
    with col_centro[1]:
        if st.button("🔒 PORTAL EXECUTIVO (TECH)", key="btn_ir_funcionarios"):
            st.session_state["pagina_atual"] = "funcionarios"
            st.rerun()

    st.markdown('<p style="text-align: center; color: #475569; font-size: 0.78rem; margin-top: 24px; font-weight: 500;">© 2026 TECH HOME GLOBAL INC. All rights reserved.</p>', unsafe_allow_html=True)