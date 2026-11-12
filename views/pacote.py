import streamlit as st
import json
import os
from datetime import datetime
from ui.estilo import exibir_logo_tech_home

def carregar_pedidos():
    if os.path.exists("pedidos_reais.json"):
        try:
            with open("pedidos_reais.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_pedido(novo_pedido):
    pedidos = carregar_pedidos()
    pedidos.append(novo_pedido)
    with open("pedidos_reais.json", "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=4)

def renderizar_pacote():
    exibir_logo_tech_home("Configuração de Ecossistema & Suporte")

    if "etapa" not in st.session_state:
        st.session_state["etapa"] = 1
    if "tipo_servico" not in st.session_state:
        st.session_state["tipo_servico"] = "Novo Ecossistema"

    etapa = st.session_state["etapa"]

    # Barra de Progresso Superior
    st.markdown(f"""
    <div style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.2); border-radius: 12px; padding: 12px; text-align: center; margin-bottom: 24px;">
        <span style="color: #38BDF8; font-weight: 700; font-size: 0.9rem;">ETAPA {etapa} DE 6</span>
        <div style="color: #94A3B8; font-size: 0.8rem; margin-top: 2px;">
            {
                'Escolha do Tipo de Atendimento' if etapa == 1 else 
                ('Seleção de Dispositivos' if etapa == 2 else 
                ('Iluminação LED' if etapa == 3 else 
                ('Assistente de Voz' if etapa == 4 else 
                ('Resumo do Projeto' if etapa == 5 else 'Dados e Finalização'))))
            }
        </div>
    </div>
    """, unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ETAPA 1: ESCOLHA DO TIPO DE SERVIÇO
    # -------------------------------------------------------------
    if etapa == 1:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;">O que você precisa hoje?</h3>', unsafe_allow_html=True)
        
        tipo = st.radio(
            "Selecione o serviço:",
            ["Instalar Novo Ecossistema TECH HOME", "Reparo / Manutenção Técnica"],
            label_visibility="collapsed"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if "Reparo" in tipo:
            st.markdown("""
            <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-left: 4px solid #EF4444; border-radius: 12px; padding: 16px; margin-bottom: 20px;">
                <div style="color: #FCA5A5; font-weight: 700; font-size: 0.92rem; margin-bottom: 6px;">⚠️ ATENÇÃO AOS TERMOS DE REPARO:</div>
                <p style="color: #CBD5E1; font-size: 0.85rem; line-height: 1.5; margin: 0;">
                    Realizamos serviços de reparo, manutenção e reconfiguração <b>exclusivamente em instalações realizadas pela TECH HOME</b>. Não prestamos suporte em dispositivos instalados por terceiros.
                </p>
            </div>
            """, unsafe_allow_html=True)
            st.session_state["tipo_servico"] = "Reparo Técnico (Exclusivo Instalação TECH HOME)"
        else:
            st.session_state["tipo_servico"] = "Novo Ecossistema"

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar ao Início"):
                st.session_state["pagina_atual"] = "home"
                st.rerun()
        with col2:
            if st.button("Avançar ➡️"):
                st.session_state["etapa"] = 2
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 2: SELEÇÃO DE PACOTE
    # -------------------------------------------------------------
    elif etapa == 2:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;">Selecione o Pacote Base</h3>', unsafe_allow_html=True)
        
        pacote_escolhido = st.radio(
            "Escolha o pacote:",
            ["Pacote Essencial (2 Módulos Smart + Central)", "Pacote Avançado (4 Módulos Smart + Central)", "Pacote Premium Enterprise (8 Módulos Smart + Central)"],
            label_visibility="collapsed"
        )
        st.session_state["pacote_base"] = pacote_escolhido

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar"):
                st.session_state["etapa"] = 1
                st.rerun()
        with col2:
            if st.button("Avançar ➡️"):
                st.session_state["etapa"] = 3
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 3: FITA LED
    # -------------------------------------------------------------
    elif etapa == 3:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;">Iluminação Arquitetônica LED</h3>', unsafe_allow_html=True)
        
        fita_escolhida = st.radio(
            "Deseja adicionar Fita LED RGB?",
            ["Sem Fita LED", "Fita LED 5 Metros (Ambiente S/N)", "Fita LED 10 Metros (Duplo Ambiente)"],
            label_visibility="collapsed"
        )
        st.session_state["fita_led"] = fita_escolhida

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar"):
                st.session_state["etapa"] = 2
                st.rerun()
        with col2:
            if st.button("Avançar ➡️"):
                st.session_state["etapa"] = 4
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 4: ASSISTENTE DE VOZ
    # -------------------------------------------------------------
    elif etapa == 4:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;">Central de Comando por Voz</h3>', unsafe_allow_html=True)
        
        voz_escolhida = st.radio(
            "Escolha o assistente:",
            ["Echo Dot com Alexa (Incluso)", "Echo Show com Tela Inteligente", "Apenas Configuração (Já possuo dispositivo)"],
            label_visibility="collapsed"
        )
        st.session_state["assistente_voz"] = voz_escolhida

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar"):
                st.session_state["etapa"] = 3
                st.rerun()
        with col2:
            if st.button("Avançar ➡️"):
                st.session_state["etapa"] = 5
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 5: RESUMO EXECUTIVO
    # -------------------------------------------------------------
    elif etapa == 5:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 16px;">Resumo do Projeto</h3>', unsafe_allow_html=True)
        
        tipo_srv = st.session_state.get('tipo_servico', 'Novo Ecossistema')
        pacote = st.session_state.get('pacote_base', 'Essencial')
        fita = st.session_state.get('fita_led', 'Sem Fita')
        voz = st.session_state.get('assistente_voz', 'Alexa')

        st.markdown(f"""
        <div class="tech-card">
            <p style="color: #38BDF8; font-weight: 700; margin-bottom: 10px;">📋 ESPECIFICAÇÕES DO PEDIDO:</p>
            <p style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 6px;"><b>Tipo:</b> {tipo_srv}</p>
            <p style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 6px;"><b>Pacote:</b> {pacote}</p>
            <p style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 6px;"><b>Iluminação:</b> {fita}</p>
            <p style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 0;"><b>Assistente:</b> {voz}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar"):
                st.session_state["etapa"] = 4
                st.rerun()
        with col2:
            if st.button("Avançar para Dados ➡️"):
                st.session_state["etapa"] = 6
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 6: DADOS DE CONTATO E MENSAGEM PARA AGENDAMENTO NO WHATSAPP
    # -------------------------------------------------------------
    elif etapa == 6:
        st.markdown('<h3 style="color: #FFFFFF; font-size: 1.25rem; font-weight: 700; margin-bottom: 12px;">Dados para Contato</h3>', unsafe_allow_html=True)

        # Mensagem corporativa orientando o agendamento no WhatsApp
        st.markdown("""
        <div style="background: rgba(56, 189, 248, 0.08); border: 1px solid rgba(56, 189, 248, 0.25); border-left: 4px solid #38BDF8; border-radius: 12px; padding: 14px 16px; margin-bottom: 18px;">
            <p style="color: #E2E8F0; font-size: 0.88rem; line-height: 1.5; margin: 0;">
                💬 <b>Agendamento Direto:</b> Após finalizar abaixo, entre em contato conosco pelo WhatsApp para combinarmos o melhor <b>horário, local e data</b> para o seu atendimento.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        nome = st.text_input("Seu Nome Completo")
        telefone = st.text_input("Seu WhatsApp (com DDD)")

        st.markdown("<br>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("⬅️ Voltar"):
                st.session_state["etapa"] = 5
                st.rerun()
        with col2:
            if st.button("✅ FINALIZAR E ENVIAR AO WHATSAPP"):
                if not nome or not telefone:
                    st.error("Por favor, preencha seu nome e WhatsApp.")
                else:
                    tipo_srv = st.session_state.get('tipo_servico', 'Novo Ecossistema')
                    pacote = st.session_state.get('pacote_base', 'Essencial')
                    fita = st.session_state.get('fita_led', 'Sem Fita')
                    voz = st.session_state.get('assistente_voz', 'Alexa')

                    novo_pedido = {
                        "id": str(datetime.now().timestamp()),
                        "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                        "nome": nome,
                        "telefone": telefone,
                        "tipo": tipo_srv,
                        "pacote": pacote,
                        "fita_led": fita,
                        "assistente": voz,
                        "status": "Pendente"
                    }

                    salvar_pedido(novo_pedido)

                    msg = f"*NOVO PEDIDO - TECH HOME*%0A%0A*Cliente:* {nome}%0A*WhatsApp:* {telefone}%0A*Serviço:* {tipo_srv}%0A*Pacote:* {pacote}%0A*Fita LED:* {fita}%0A*Assistente:* {voz}%0A%0A_Gostaria de combinar o horário, local e data para o atendimento._"
                    link_wpp = f"https://wa.me/5511999999999?text={msg}"

                    st.success("Pedido registrado com sucesso em nosso sistema!")
                    st.markdown(f"""
                    <a href="{link_wpp}" target="_blank" class="btn-whatsapp">
                        💬 ENTRAR EM CONTATO NO WHATSAPP PARA AGENDAR HORÁRIO, LOCAL E DATA
                    </a>
                    """, unsafe_allow_html=True)