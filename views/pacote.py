import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_pacote():
    # Inicializa o estado das etapas se não existir
    if "etapa" not in st.session_state:
        st.session_state["etapa"] = 1
    if "dados_pedido" not in st.session_state:
        st.session_state["dados_pedido"] = {
            "pacote": "Completo",
            "fita_led": "Fita LED - 2m",
            "valor_fita": 99.0,
            "tomadas": "4 Tomadas Inteligentes",
            "valor_tomadas": 150.0,
            "alexa": "Echo Dot 5ª Geração",
            "valor_alexa": 349.0,
            "nome": "",
            "telefone": "",
            "data_agendamento": "11/11/2026",
            "hora_agendamento": "14:30"
        }

    etapa = st.session_state["etapa"]

    # Topo com botão de voltar e Logo
    col_voltar, col_logo = st.columns([1, 5])
    with col_voltar:
        if st.button("← Voltar"):
            if etapa > 1:
                st.session_state["etapa"] -= 1
                st.rerun()
            else:
                st.session_state["pagina_atual"] = "home"
                st.rerun()
    with col_logo:
        pass

    exibir_logo_tech_home("Monte seu Pacote • Automação Residencial")

    # Barra de Progresso e Indicador de Etapas
    st.markdown(f"""
    <div style="font-size: 0.85rem; color: #60A5FA; font-weight: 600; margin-bottom: 6px;">
        Etapa {etapa} de 7
    </div>
    """, unsafe_allow_html=True)
    
    progresso = etapa / 7.0
    st.progress(progresso)

    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ETAPA 1: ESCOLHER PACOTE PRINCIPAL
    # -------------------------------------------------------------
    if etapa == 1:
        st.markdown("### 1. Escolher Pacote Base")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Selecione a modalidade ideal para a sua residência:</p>", unsafe_allow_html=True)
        
        pacotes = [
            ("💡 Pacote Fita LED", "Iluminação indireta e cenários customizados", 199.0),
            ("🔌 Pacote Tomadas", "Controle de eletrodomésticos via aplicativo", 250.0),
            ("⭐ Pacote Completo (Recomendado)", "LED + Tomadas + Assistente de Voz", 598.0),
            ("⚙️ Pacote Personalizado", "Monte sob medida com nosso suporte", 150.0),
            ("🔧 Apenas Configuração", "Configuração de dispositivos que você já possui", 120.0)
        ]

        for nome, desc, preco in pacotes:
            selecionado = st.session_state["dados_pedido"]["pacote"] == nome
            classe_card = "tech-card-active" if selecionado else "tech-card"
            
            st.markdown(f"""
            <div class="{classe_card}">
                <div style="font-weight: 700; color: #FFFFFF; font-size: 1.05rem;">{nome}</div>
                <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px;">{desc}</div>
                <div style="color: #2589F5; font-weight: 700; font-size: 0.95rem; margin-top: 8px;">R$ {preco:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Selecionar {nome.split()[1]}", key=f"sel_pac_{nome}"):
                st.session_state["dados_pedido"]["pacote"] = nome
                st.session_state["dados_pedido"]["valor_base"] = preco
                st.session_state["etapa"] = 2
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 2: ESCOLHER FITA LED
    # -------------------------------------------------------------
    elif etapa == 2:
        st.markdown("### 2. Escolher Fita LED")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Selecione o comprimento da fita LED para o seu pacote</p>", unsafe_allow_html=True)

        fitas = [
            ("Fita LED - 2m", 99.0),
            ("Fita LED - 5m", 199.0),
            ("Fita LED - 10m", 349.0),
            ("Fita LED - 15m", 399.0),
            ("Fita LED - 20m", 649.0)
        ]

        for nome, preco in fitas:
            if st.button(f"{nome} — + R$ {preco:.2f}", key=f"fita_{nome}"):
                st.session_state["dados_pedido"]["fita_led"] = nome
                st.session_state["dados_pedido"]["valor_fita"] = preco
                st.session_state["etapa"] = 3
                st.rerun()

        st.markdown("""
        <div class="info-box-blue">
            ℹ️ A fita LED é instalada com fita dupla-face 3M e fonte incluída. Controlável via app.
        </div>
        """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ETAPA 3: ESCOLHER ALEXA / DISPOSITIVO DE VOZ
    # -------------------------------------------------------------
    elif etapa == 3:
        st.markdown("### 3. Escolher Central de Voz (Alexa)")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Escolha o dispositivo inteligente para comando por voz:</p>", unsafe_allow_html=True)

        alexas = [
            ("Echo Pop (Compacto)", 249.0),
            ("Echo Dot 5ª Geração", 349.0),
            ("Echo Show 5 (Com Tela)", 599.0),
            ("Sem Assistente (Já possuo)", 0.0)
        ]

        for nome, preco in alexas:
            if st.button(f"{nome} — + R$ {preco:.2f}" if preco > 0 else f"{nome}", key=f"alexa_{nome}"):
                st.session_state["dados_pedido"]["alexa"] = nome
                st.session_state["dados_pedido"]["valor_alexa"] = preco
                st.session_state["etapa"] = 4
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 4: RESUMO PARCIAL
    # -------------------------------------------------------------
    elif etapa == 4:
        st.markdown("### 4. Resumo do Pedido")
        d = st.session_state["dados_pedido"]
        total_parcial = d.get("valor_base", 199.0) + d.get("valor_fita", 99.0) + d.get("valor_alexa", 349.0)

        st.markdown(f"""
        <div class="tech-card">
            <div style="color: #60A5FA; font-weight: 700; margin-bottom: 8px;">Itens Selecionados:</div>
            <div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 4px;">• <b>Pacote:</b> {d['pacote']}</div>
            <div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 4px;">• <b>Iluminação:</b> {d['fita_led']}</div>
            <div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 8px;">• <b>Assistente:</b> {d['alexa']}</div>
            <hr style="border-color: #1E293B; margin: 10px 0;">
            <div style="color: #2589F5; font-weight: 800; font-size: 1.1rem;">Subtotal: R$ {total_parcial:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Avançar para Agendamento →", key="avancar_agend"):
            st.session_state["etapa"] = 5
            st.rerun()

    # -------------------------------------------------------------
    # ETAPA 5: AGENDAMENTO
    # -------------------------------------------------------------
    elif etapa == 5:
        st.markdown("### 5. Agendar Instalação")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Escolha a melhor data e horário para nossa equipe ir até sua residência:</p>", unsafe_allow_html=True)

        data_agenda = st.text_input("Data da Instalação (DD/MM/AAAA)", value=st.session_state["dados_pedido"]["data_agendamento"])
        hora_agenda = st.text_input("Horário preferencial", value=st.session_state["dados_pedido"]["hora_agendamento"])

        st.session_state["dados_pedido"]["data_agendamento"] = data_agenda
        st.session_state["dados_pedido"]["hora_agendamento"] = hora_agenda

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Confirmar Agendamento →", key="avancar_dados"):
            st.session_state["etapa"] = 6
            st.rerun()

    # -------------------------------------------------------------
    # ETAPA 6: DADOS DO CLIENTE
    # -------------------------------------------------------------
    elif etapa == 6:
        st.markdown("### 6. Seus Dados de Contato")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Informe seus dados para finalizarmos o atendimento:</p>", unsafe_allow_html=True)

        nome_cliente = st.text_input("Seu Nome Completo", value=st.session_state["dados_pedido"]["nome"])
        tel_cliente = st.text_input("Seu WhatsApp (com DDD)", value=st.session_state["dados_pedido"]["telefone"])

        st.session_state["dados_pedido"]["nome"] = nome_cliente
        st.session_state["dados_pedido"]["telefone"] = tel_cliente

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Ver Resumo Final 🚀", key="ver_resumo_final"):
            if not nome_cliente or not tel_cliente:
                st.warning("Por favor, preencha seu nome e WhatsApp.")
            else:
                st.session_state["etapa"] = 7
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 7: FINALIZAÇÃO E BOTÃO WHATSAPP
    # -------------------------------------------------------------
    elif etapa == 7:
        st.markdown("### 7. Pedido Pronto!")
        d = st.session_state["dados_pedido"]
        total_final = d.get("valor_base", 199.0) + d.get("valor_fita", 99.0) + d.get("valor_alexa", 349.0)

        st.markdown(f"""
        <div class="tech-card">
            <div style="color: #60A5FA; font-weight: 700; margin-bottom: 10px;">Resumo TECH HOME:</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">👤 <b>Cliente:</b> {d['nome']}</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">📱 <b>WhatsApp:</b> {d['telefone']}</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">📦 <b>Pacote:</b> {d['pacote']}</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">💡 <b>LED:</b> {d['fita_led']}</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">🔊 <b>Alexa:</b> {d['alexa']}</div>
            <div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 8px;">📅 <b>Agendamento:</b> {d['data_agendamento']} às {d['hora_agendamento']}</div>
            <hr style="border-color: #1E293B; margin: 10px 0;">
            <div style="color: #2589F5; font-weight: 800; font-size: 1.15rem;">Total Estimado: R$ {total_final:.2f}</div>
        </div>
        """, unsafe_allow_html=True)

        # Monta o link do WhatsApp com a mensagem formatada
        texto_zap = f"Olá! Meu nome é {d['nome']}. Acabei de montar meu pacote na TECH HOME:\n- Pacote: {d['pacote']}\n- LED: {d['fita_led']}\n- Alexa: {d['alexa']}\n- Agendamento: {d['data_agendamento']} às {d['hora_agendamento']}\n- Total: R$ {total_final:.2f}. Gostaria de confirmar a instalação!"
        import urllib.parse
        texto_codificado = urllib.parse.quote(texto_zap)
        link_whatsapp = f"https://wa.me/5585999999999?text={texto_codificado}"

        st.markdown(f"""
        <a href="{link_whatsapp}" target="_blank" class="btn-whatsapp">
            💬 FINALIZAR PEDIDO PELO WHATSAPP
        </a>
        """, unsafe_allow_html=True)