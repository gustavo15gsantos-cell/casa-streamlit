import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_home():
    exibir_logo_tech_home("Infraestrutura Residencial Inteligente")

    # 1. BANNER CORPORATIVO DE ALTO IMPACTO
    st.markdown("""
    <div style="background: linear-gradient(145deg, #0F172A 0%, #020617 100%); border: 1px solid rgba(56, 189, 248, 0.25); border-radius: 24px; padding: 28px; margin-bottom: 24px; box-shadow: 0 20px 50px rgba(0,0,0,0.7);">
        <div style="width: 100%; height: 220px; border-radius: 16px; overflow: hidden; margin-bottom: 20px; background-color: #020617; border: 1px solid rgba(255,255,255,0.08);">
            <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.9;" alt="Ecossistema Inteligente">
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); color: #38BDF8; padding: 5px 12px; border-radius: 8px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 12px;">
            Divisão Corporativa • Tecnologia IoT
        </div>
        <h1 style="color: #FFFFFF; font-size: 1.8rem; font-weight: 800; line-height: 1.25; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.98rem; line-height: 1.6; margin-bottom: 12px;">
            A <b>TECH HOME</b> desenvolve e implementa ecossistemas residenciais inteligentes sem obras ou quebra-quebra. Unimos iluminação arquitetônica de precisão, controle elétrico inteligente e comandos por voz com Inteligência Artificial.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # BOTÃO DE CHAMADA PRINCIPAL
    if st.button("🚀 MONTAR MEU ECOSSISTEMA AGORA", key="btn_monte_pacote"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. MÉTRICAS DE AUTORIDADE (NÚMEROS DE MULTINACIONAL)
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.markdown("""
        <div class="tech-card" style="text-align: center; padding: 16px 8px;">
            <div style="font-size: 1.4rem; font-weight: 800; color: #38BDF8;">100%</div>
            <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600; margin-top: 4px;">Sem Quebra-Quebra</div>
        </div>
        """, unsafe_allow_html=True)
    with col_m2:
        st.markdown("""
        <div class="tech-card" style="text-align: center; padding: 16px 8px;">
            <div style="font-size: 1.4rem; font-weight: 800; color: #38BDF8;">2 Anos</div>
            <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600; margin-top: 4px;">Garantia Técnica</div>
        </div>
        """, unsafe_allow_html=True)
    with col_m3:
        st.markdown("""
        <div class="tech-card" style="text-align: center; padding: 16px 8px;">
            <div style="font-size: 1.4rem; font-weight: 800; color: #38BDF8;">24/7</div>
            <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600; margin-top: 4px;">Controle Remoto</div>
        </div>
        """, unsafe_allow_html=True)

    # 3. PILARES TECNOLÓGICOS
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 10px; margin-bottom: 14px;">Pilares Tecnológicos</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">💡</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Iluminação LED</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">🔌</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Tomadas IoT</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="tech-card" style="text-align: center; padding: 18px 12px;"><div style="font-size: 1.4rem; margin-bottom: 8px;">🎙️</div><div style="font-size: 0.82rem; font-weight: 700; color: #FFFFFF;">Comando Alexa</div></div>', unsafe_allow_html=True)

    # 4. CENÁRIOS INTELIGENTES NA PRÁTICA
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 16px; margin-bottom: 14px;">Experiência na Prática</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="tech-card" style="padding: 20px;">
        <div style="margin-bottom: 14px;">
            <span style="color: #38BDF8; font-weight: 700; font-size: 0.95rem;">🎬 "Alexa, ativar Modo Cinema"</span>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px; margin-bottom: 0;">As luzes principais se apagam, a fita LED acende em azul suave e a TV liga automaticamente.</p>
        </div>
        <hr style="border-color: rgba(255,255,255,0.08); margin: 12px 0;">
        <div style="margin-bottom: 14px;">
            <span style="color: #38BDF8; font-weight: 700; font-size: 0.95rem;">☀️ "Alexa, bom dia"</span>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px; margin-bottom: 0;">A cafeteira na tomada inteligente começa a preparar o café enquanto você ouve a previsão do tempo.</p>
        </div>
        <hr style="border-color: rgba(255,255,255,0.08); margin: 12px 0;">
        <div>
            <span style="color: #38BDF8; font-weight: 700; font-size: 0.95rem;">✈️ "Modo Viagem Ativado"</span>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px; margin-bottom: 0;">Simule presença em casa acendendo e apagando luzes pelo celular de qualquer lugar do mundo.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 5. COMO FUNCIONA (PASSO A PASSO)
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 16px; margin-bottom: 14px;">Como Funciona</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tech-card" style="padding: 20px;">
        <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 14px;">
            <div style="background: #0284C7; color: white; font-weight: 800; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 0.85rem;">1</div>
            <div>
                <div style="color: #FFFFFF; font-weight: 700; font-size: 0.92rem;">Configure seu Pacote Online</div>
                <div style="color: #94A3B8; font-size: 0.83rem;">Escolha os dispositivos e veja o valor estimado na hora, sem compromisso.</div>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 14px;">
            <div style="background: #0284C7; color: white; font-weight: 800; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 0.85rem;">2</div>
            <div>
                <div style="color: #FFFFFF; font-weight: 700; font-size: 0.92rem;">Alinhamento via WhatsApp</div>
                <div style="color: #94A3B8; font-size: 0.83rem;">Nossa equipe tira suas dúvidas e combina o melhor dia e horário para você.</div>
            </div>
        </div>
        <div style="display: flex; align-items: flex-start; gap: 12px;">
            <div style="background: #0284C7; color: white; font-weight: 800; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 0.85rem;">3</div>
            <div>
                <div style="color: #FFFFFF; font-weight: 700; font-size: 0.92rem;">Instalação Limpa e Configuração</div>
                <div style="color: #94A3B8; font-size: 0.83rem;">Instalamos tudo e deixamos os comandos de voz prontos no seu celular.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 6. GARANTIA E SEGURANÇA
    st.markdown("""
    <div class="tech-card" style="border-left: 4px solid #10B981; margin-top: 16px;">
        <h3 style="color: #FFFFFF; font-size: 1.1rem; font-weight: 700; margin-bottom: 10px;">🛡️ Garantia e Segurança TECH HOME</h3>
        <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 8px;">
            • <b>Privacidade Total:</b> Seus dados são protegidos e usados apenas para o seu atendimento técnico.
        </p>
        <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.5; margin-bottom: 0px;">
            • <b>Equipamentos Homologados:</b> Produtos originais com certificação Anatel e garantia de fábrica.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 7. PERGUNTAS FREQUENTES (FAQ INTERATIVO)
    st.markdown('<p style="color: #94A3B8; font-size: 0.82rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.2px; margin-top: 20px; margin-bottom: 12px;">Dúvidas Frequentes</p>', unsafe_allow_html=True)

    with st.expander("🔨 Precisa quebrar parede ou passar fios novos?"):
        st.write("Não! Trabalhamos com tecnologia sem fio (Wi-Fi / Zigbee) e fitas LED com adesivo industrial 3M de alta fixação. A instalação é 100% limpa e rápida.")

    with st.expander("📶 E se a internet da minha casa cair?"):
        st.write("Seus interruptores e tomadas continuam funcionando manualmente normalmente. Assim que o Wi-Fi voltar, o controle por voz e aplicativo se reconecta sozinho.")

    with st.expander("🗣️ Já tenho uma Alexa, posso contratar só a instalação?"):
        st.write("Com certeza! Na etapa de configuração do pacote, basta selecionar a opção 'Sem Assistente (Já possuo)' ou 'Apenas Configuração'.")

    st.markdown("<br>", unsafe_allow_html=True)

    # BOTÃO SECUNDÁRIO DE CONVERSÃO NO FINAL DA PÁGINA
    if st.button("✨ CONFIGURAR MEU PACOTE AGORA", key="btn_monte_pacote_rodape"):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # PORTAL CORPORATIVO (ÁREA RESTRITA)
    col_centro = st.columns([1, 2, 1])
    with col_centro[1]:
        if st.button("🔒 PORTAL EXECUTIVO (TECH)", key="btn_ir_funcionarios"):
            st.session_state["pagina_atual"] = "funcionarios"
            st.rerun()

    st.markdown('<p style="text-align: center; color: #475569; font-size: 0.78rem; margin-top: 24px; font-weight: 500;">© 2026 TECH HOME GLOBAL INC. Todos os direitos reservados.</p>', unsafe_allow_html=True)