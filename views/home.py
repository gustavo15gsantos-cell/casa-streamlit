import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    # Exibe a logo oficial clicável no topo (redireciona para o início)
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # -------------------------------------------------------------
    # ESTILOS DE UI/UX & BOTÃO DE CONVERSÃO ALTO-PADRÃO
    # -------------------------------------------------------------
    st.markdown("""
    <style>
        .img-desktop { display: block; width: 100%; }
        .img-mobile { display: none; }

        @media (max-width: 768px) {
            .img-desktop { display: none; }
            .img-mobile { display: block; width: 100%; }
        }

        /* Botão principal de conversão com destaque executivo */
        div.stButton > button:first-child {
            background: linear-gradient(135deg, #0284C7 0%, #0EA5E9 100%) !important;
            color: #FFFFFF !important;
            font-weight: 800 !important;
            font-size: 1.05rem !important;
            letter-spacing: 0.5px !important;
            padding: 18px 24px !important;
            border-radius: 14px !important;
            border: 1px solid rgba(56, 189, 248, 0.5) !important;
            box-shadow: 0 8px 25px rgba(14, 165, 233, 0.4) !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }
        div.stButton > button:first-child:hover {
            background: linear-gradient(135deg, #0ea5e9 0%, #38bdf8 100%) !important;
            box-shadow: 0 12px 30px rgba(56, 189, 248, 0.6) !important;
            border-color: #FFFFFF !important;
        }
    </style>

    <div class="img-desktop" style="margin-bottom: 24px;">
        <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border: 1px solid rgba(56, 189, 248, 0.2);">
    </div>
    <div class="img-mobile" style="margin-bottom: 24px;">
        <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" style="width: 100%; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border: 1px solid rgba(56, 189, 248, 0.2);">
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # HERO SECTION / APRESENTAÇÃO CORPORATIVA DE IMPACTO
    # -------------------------------------------------------------
    st.markdown("""
    <div style="background: linear-gradient(145deg, #090D16 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.22); border-radius: 18px; padding: 28px; margin-bottom: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.4);">
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.1); color: #38BDF8; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; padding: 5px 12px; border-radius: 20px; border: 1px solid rgba(56, 189, 248, 0.3); margin-bottom: 12px;">
            ⚡ DIVISÃO CORPORATIVA • TECNOLOGIA IOT
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.7rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6; margin: 0;">
            A <b style="color: #38BDF8;">TECH HOME</b> desenvolve e implementa ecossistemas residenciais inteligentes sem obras ou quebra-quebra. Unimos iluminação arquitetônica de precisão, controle elétrico inteligente e comandos por voz com Inteligência Artificial de última geração.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botão de Ação Principal em Destaque Absoluto
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
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
            <span>📊</span> PADRÃO CORPORATIVO TECH HOME
        </h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            ✅ <b>100% Sem Quebra-Quebra:</b> Instalação limpa via protocolo sem fio de ultra-performance.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            ✅ <b>2 Anos de Garantia:</b> Suporte técnico especializado e direto com nossa equipe de engenharia.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            ✅ <b>Segurança Criptografada:</b> Seus dados e sua rede residencial protegidos contra invasões externas.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # PILARES TECNOLÓGICOS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
            <span>🏛️</span> PILARES DE ENGENHARIA
        </h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            🔹 <b>Automação Modular:</b> Expansão gradual sem necessidade de reestruturação elétrica complexa.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            🔹 <b>Iluminação Dinâmica:</b> Cenas personalizadas para descanso, trabalho corporativo ou entretenimento.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            🔹 <b>Integração de Voz:</b> Central inteligente compatível com os principais assistentes do mercado.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # CENÁRIOS PRÁTICOS
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
            <span>🏠</span> CENÁRIOS DE USO DIÁRIO
        </h3>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            🎬 <b>Modo Cinema:</b> Atenua as luzes, fecha as cortinas motorizadas e ativa o som com um único comando.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin-bottom: 10px;">
            🌙 <b>Modo Descanso:</b> Desliga tomadas de consumo passivo e ajusta a climatização ideal.
        </p>
        <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6; margin: 0;">
            🔒 <b>Modo Ausente:</b> Simula presença residencial acendendo luzes em horários estratégicos.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # FAQ / PERGUNTAS FREQUENTES (Estrutura segura e limpa)
    # -------------------------------------------------------------
    st.markdown("""
    <div class="tech-card">
        <h3 style="color: #38BDF8; font-size: 1.1rem; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px;">
            <span>❓</span> PERGUNTAS FREQUENTES
        </h3>
        <div style="margin-bottom: 14px;">
            <div style="color: #F8FAFC; font-size: 0.9rem; font-weight: 600; margin-bottom: 4px;">Preciso quebrar paredes para realizar a instalação?</div>
            <div style="color: #CBD5E1; font-size: 0.85rem; line-height: 1.5;">Não! Todo o nosso sistema opera via rede sem fio criptografada de alta velocidade, preservando 100% da sua estrutura civil.</div>
        </div>
        <div>
            <div style="color: #F8FAFC; font-size: 0.9rem; font-weight: 600; margin-bottom: 4px;">E se a conexão com a internet cair?</div>
            <div style="color: #CBD5E1; font-size: 0.85rem; line-height: 1.5;">Os módulos locais continuam funcionando perfeitamente via automação interna local e comandos manuais nos interruptores inteligentes.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # PORTAL EXECUTIVO
    # -------------------------------------------------------------
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 Acessar Portal Executivo (Equipe)", use_container_width=True):
        st.session_state["pagina_atual"] = "funcionarios"
        st.rerun()