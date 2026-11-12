import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    # Exibe a logo oficial TECH HOME no topo
    exibir_logo_tech_home("Instalação e configuração de dispositivos com Alexa")

    # Banner principal com imagem de ambiente inteligente (igualzinho ao design)
    st.markdown("""
    <div style="background: linear-gradient(180deg, #131C2E 0%, #0F172A 100%); border: 1px solid #1E293B; border-radius: 18px; padding: 18px; margin-bottom: 20px; box-shadow: 0 8px 24px rgba(0,0,0,0.4);">
        <div style="width: 100%; height: 180px; border-radius: 12px; overflow: hidden; margin-bottom: 14px; background-color: #0B111E;">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=800&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.85;" alt="Casa Inteligente">
        </div>
        <h2 style="color: #FFFFFF; font-size: 1.4rem; font-weight: 700; margin-bottom: 6px;">
            Casa inteligente em poucos cliques
        </h2>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.4; margin-bottom: 16px;">
            Monte seu pacote e automatize sua casa com segurança e praticidade.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão principal de Ação (Monte seu pacote)
    if st.button("🚀 Monte seu pacote", key="btn_monte_pacote"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Seção de pacotes disponíveis (mini cards decorativos)
    st.markdown('<p style="color: #94A3B8; font-size: 0.9rem; font-weight: 600; margin-bottom: 10px;">Pacotes disponíveis</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 10px; font-size: 0.82rem; font-weight: 600; color: #60A5FA;">💡 LED</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 10px; font-size: 0.82rem; font-weight: 600; color: #60A5FA;">🔌 Tomadas</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 10px; font-size: 0.82rem; font-weight: 600; color: #60A5FA;">⭐ Completo</div>', unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 10px; font-size: 0.82rem; font-weight: 600; color: #60A5FA;">⚙️ Personalizado</div>', unsafe_allow_html=True)
    with col5:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 10px; font-size: 0.82rem; font-weight: 600; color: #60A5FA;">🔧 Configuração</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; color: #64748B; font-size: 0.8rem;">Suporte &bull; Instalação rápida &bull; Configuração segura</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Link discreto para a Área dos Funcionários no rodapé da Home
    col_centro = st.columns([1, 2, 1])
    with col_centro[1]:
        if st.button("🔒 ÁREA DOS FUNCIONÁRIOS", key="btn_ir_funcionarios"):
            st.session_state["pagina_atual"] = "funcionarios"
            st.rerun()

    st.markdown('<p style="text-align: center; color: #475569; font-size: 0.75rem; margin-top: 15px;">© 2026 TECH HOME • v2.0</p>', unsafe_allow_html=True)