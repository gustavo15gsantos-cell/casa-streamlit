import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # -------------------------------------------------------------
    # IMAGENS RESPONSIVAS (Desktop vs Celular)
    # -------------------------------------------------------------
    st.markdown("""
    <style>
        .img-desktop { display: block; width: 100%; }
        .img-mobile { display: none; }

        @media (max-width: 768px) {
            .img-desktop { display: none; }
            .img-mobile { display: block; width: 100%; }
        }
    </style>

    <div class="img-desktop">
        <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; border-radius: 14px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
    </div>
    <div class="img-mobile">
        <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" style="width: 100%; border-radius: 14px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # HERO SECTION / APRESENTAÇÃO CORPORATIVA
    # -------------------------------------------------------------
    st.markdown("""
    <div style="background: linear-gradient(145deg, #090D16 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.18); border-radius: 16px; padding: 22px; margin-top: 20px; margin-bottom: 16px;">
        <span style="color: #38BDF8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px;">DIVISÃO CORPORATIVA • TECNOLOGIA IOT</span>
        <h1 style="color: #FFFFFF; font-size: 1.6rem; font-weight: 800; margin-top: 10px; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.9rem; line-height: 1.6; margin: 0;">
            A TECH HOME desenvolve e implementa ecossistemas residenciais inteligentes sem obras ou quebra-quebra. Unimos iluminação arquitetônica de precisão, controle elétrico inteligente e comandos por voz com Inteligência Artificial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Ação Principal
    if st.button("🚀 INICIAR CONFIGURAÇÃO DO ECOSSISTEMA", use_container_width=True):
        st.session_state["pagina_atual"] = "pacote"
        st.session_state["etapa"] = 1
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # MÉTRICAS DE AUTORIDADE / VALOR
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
    # PILARES TECNOLÓGICOS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 14px;">🏛️ PILARES DE ENGENHARIA</h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            🔹 <b>Automação Modular:</b> Expansão gradual sem necessidade de reestruturação elétrica.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            🔹 <b>Iluminação Dinâmica:</b> Cenas personalizadas para descanso, trabalho ou entretenimento.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            🔹 <b>Integração de Voz:</b> Central inteligente compatível com assistentes de mercado.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # CENÁRIOS PRÁTICOS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 14px;">🏠 CENÁRIOS DE USO DIÁRIO</h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            🎬 <b>Modo Cinema:</b> Atenua as luzes, fecha as cortinas e ativa o sistema de som com um único comando.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 8px;">
            🌙 <b>Modo Descanso:</b> Desliga tomadas de consumo passivo e ajusta a temperatura ideal.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            🔒 <b>Modo Ausente:</b> Simula presença residencial acendendo luzes em horários programados.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # FAQ / PERGUNTAS FREQUENTES (Sem erros de exibição)
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 14px;">❓ PERGUNTAS FREQUENTES</h3>
        <p style="color: #F8FAFC; font-size: 0.9rem; font-weight: 600; margin-bottom: 4px;">Preciso quebrar paredes para instalar?</p>
        <p style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 12px;">Não! Todo o nosso sistema opera via rede sem fio criptografada de alta velocidade.</p>
        
        <p style="color: #F8FAFC; font-size: 0.9rem; font-weight: 600; margin-bottom: 4px;">E se a internet cair?</p>
        <p style="color: #CBD5E1; font-size: 0.85rem; margin-bottom: 0;">Os módulos locais continuam funcionando via automação interna e comandos manuais.</p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # PORTAL EXECUTIVO
    # -------------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 Acessar Portal Executivo (Equipe)", use_container_width=True):
        st.session_state["pagina_atual"] = "funcionarios"
        st.rerun()