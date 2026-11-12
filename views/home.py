import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    # Exibe a logo oficial clicável no topo
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # -------------------------------------------------------------
    # IMAGEM DE ALTA QUALIDADE E PROFISSIONAL (Substituída)
    # -------------------------------------------------------------
    st.image(
        "https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80",
        use_container_width=True,
        caption="Divisão Corporativa • Tecnologia IoT de Alta Performance"
    )

    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <h1 style="color: #FFFFFF; font-size: 1.6rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.5; margin-bottom: 20px; max-width: 600px; margin-left: auto; margin-right: auto;">
            Controle total de iluminação, segurança e acessos através de ecossistemas inteligentes integrados e seguros.
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