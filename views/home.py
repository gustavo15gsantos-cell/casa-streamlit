import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # Banner Multinacional de Alto Impacto
    st.markdown("""
    <div style="background: linear-gradient(145deg, #0F172A 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 24px; padding: 28px; margin-bottom: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.7);">
        <div style="width: 100%; height: 220px; border-radius: 16px; overflow: hidden; margin-bottom: 20px; background-color: #020617; border: 1px solid rgba(255,255,255,0.08);">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;" alt="Smart Ecosystem">
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 5px 12px; border-radius: 8px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
            Divisão Corporativa
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.8rem; font-weight: 800; line-height: 1.25; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.98rem; line-height: 1.6; margin-bottom: 16px;">
            A <b>TECH HOME</b> é especializada no desenvolvimento e na implementação de infraestruturas de automação residencial de alto padrão. Combinando engenharia de ponta, design arquitetônico e ecossistemas IoT proprietários, transformamos residências tradicionais em ambientes totalmente integrados, inteligentes e seguros.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Chamada Principal
    if st.button("🚀 INICIAR CONFIGURAÇÃO DE ECOSSISTEMA", key="btn_monte_pacote"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # SEÇÃO DE CONFIANÇA E SEGURANÇA (Para tranquilizar o cliente)
    st.markdown("""
    <div class="tech-card" style="border-left: 4px solid #10B981;">
        <h3 style="color: #FFFFFF; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px;">🛡️ Garantia e Segurança TECH HOME</h3>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin-bottom: 10px;">
            • <b>Privacidade de Dados:</b> Suas informações de contato são utilizadas exclusivamente para o nosso atendimento técnico e não são compartilhadas.
        </p>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin-bottom: 10px;">
            • <b>Suporte Direto:</b> Todo o fechamento e alinhamento de datas são feitos diretamente pelo nosso WhatsApp oficial, garantindo total transparência.
        </p>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin-bottom: 0px;">
            • <b>Instalação Certificada:</b> Profissionais qualificados e equipamentos com garantia de fábrica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Portal Corporativo
    col_centro = st.columns([1, 2, 1])
    with col_centro[1]:
        if st.button("🔒 PORTAL EXECUTIVO (TECH)", key="btn_ir_funcionarios"):
            st.session_state["pagina_atual"] = "funcionarios"
            st.rerun()

    st.markdown('<p style="text-align: center; color: #475569; font-size: 0.78rem; margin-top: 24px; font-weight: 500;">© 2026 TECH HOME GLOBAL INC. Todos os direitos reservados.</p>', unsafe_allow_html=True)