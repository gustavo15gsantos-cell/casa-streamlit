import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    # Exibe a logo oficial clicable no topo
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # -------------------------------------------------------------
    # BANNER PRINCIPAL (SUBSTITUI IMAGEM ANTIGA POR DESIGN PURAMENTE NÍTIDO)
    # -------------------------------------------------------------
    st.markdown("""
    <div style="background: linear-gradient(135deg, #090D16 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 20px; padding: 28px 20px; text-align: center; margin-bottom: 24px; box-shadow: 0 15px 35px rgba(0,0,0,0.6);">
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.1); color: #38BDF8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 6px 14px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 14px;">
            ⚡ AUTOMAÇÃO RESIDENCIAL CORPORATIVA
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.6rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px;">
            O Futuro da Sua Casa na Palma da Mão
        </h1>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">
            Transforme residências comuns em ecossistemas inteligentes de alto padrão com segurança avançada, iluminação arquitetônica e comando por voz.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Ação Principal para Iniciar o Orçamento
    if st.button("🚀 INICIAR CONFIGURAÇÃO DO ECOSSISTEMA", use_container_width=True):
        st.session_state["pagina_atual"] = "pacote"
        st.session_state["etapa"] = 1
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # MÉTRICAS DE AUTORIDADE
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 14px;">📊 PADRÃO CORPORATIVO TECH HOME</h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            ✅ <b>100% Sem Quebra-Quebra:</b> Instalação limpa via protocolo sem fio de alta performance.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            ✅ <b>2 Anos de Garantia:</b> Suporte técnico especializado e direto com nossa equipe.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            ✅ <b>Segurança Criptografada:</b> Seus dados e sua rede residencial protegidos contra invasões.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ACESSO AO PORTAL EXECUTIVO (FUNCIONÁRIOS)
    # -------------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 Acessar Portal Executivo (Equipe)", use_container_width=True):
        st.session_state["pagina_atual"] = "funcionarios"
        st.rerun()