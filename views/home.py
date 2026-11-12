import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    exibir_logo_tech_home("Global Smart Infrastructure")

    # Banner Corporativo de Impacto (Estilo Multinacional)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #0F172A 0%, #030712 100%); border: 1px solid rgba(59, 130, 246, 0.25); border-radius: 20px; padding: 24px; margin-bottom: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.6);">
        <div style="width: 100%; height: 200px; border-radius: 14px; overflow: hidden; margin-bottom: 16px; background-color: #030712; border: 1px solid rgba(255,255,255,0.05);">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.85;" alt="Smart Ecosystem">
        </div>
        <div style="display: inline-block; background: rgba(59, 130, 246, 0.15); color: #60A5FA; padding: 4px 10px; border-radius: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px;">
            Next-Gen Automation
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.65rem; font-weight: 800; line-height: 1.25; margin-bottom: 10px;">
            Infraestrutura inteligente para residências de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.5; margin-bottom: 20px;">
            Integração avançada de ecossistemas IoT, automação de iluminação arquitetônica e centrais de comando por voz de última geração.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Ação Principal
    if st.button("🚀 INICIAR CONFIGURAÇÃO DE ECOSSISTEMA", key="btn_monte_pacote"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Seção de Soluções Corporativas (Grid de Cards)
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">Portfólio de Soluções</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 14px 10px;"><div style="font-size: 1.2rem; margin-bottom: 6px;">💡</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Iluminação LED</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 14px 10px;"><div style="font-size: 1.2rem; margin-bottom: 6px;">🔌</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Smart Grid</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 14px 10px;"><div style="font-size: 1.2rem; margin-bottom: 6px;">🎙️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Voice AI</div></div>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 14px 10px;"><div style="font-size: 1.2rem; margin-bottom: 6px;">⚙️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Personalização Total</div></div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 14px 10px;"><div style="font-size: 1.2rem; margin-bottom: 6px;">🛡️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Segurança Certificada</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #64748B; font-size: 0.8rem; font-weight: 500;">Enterprise Grade • Certificação ISO • Suporte Global 24/7</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Acesso Restrito Corporativo
    col_centro = st.columns([1, 2, 1])
    with col_centro[1]:
        if st.button("🔒 PORTAL CORPORATIVO (RH / TECH)", key="btn_ir_funcionarios"):
            st.session_state["pagina_atual"] = "funcionarios"
            st.rerun()

    st.markdown('<p style="text-align: center; color: #475569; font-size: 0.75rem; margin-top: 20px;">© 2026 TECH HOME GLOBAL INC. All rights reserved.</p>', unsafe_allow_html=True)