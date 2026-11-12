import streamlit as st
import json
import os
import urllib.parse
from datetime import datetime
from ui.estilo import exibir_logo_tech_home

ARQUIVO_PEDIDOS = "pedidos_reais.json"

def salvar_pedido_real(dados, total):
    pedidos = []
    if os.path.exists(ARQUIVO_PEDIDOS):
        try:
            with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as f:
                pedidos = json.load(f)
        except Exception:
            pedidos = []

    # Evita duplicar o mesmo pedido se o usuário atualizar a página na etapa final
    if any(p.get("nome") == dados["nome"].strip() and p.get("telefone") == dados["telefone"].strip() for p in pedidos):
        return

    partes_nome = dados["nome"].strip().split()
    if len(partes_nome) >= 2:
        inicial = (partes_nome[0][0] + partes_nome[-1][0]).upper()
    elif len(partes_nome) == 1:
        inicial = partes_nome[0][:2].upper()
    else:
        inicial = "CL"

    novo_pedido = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S"),
        "inicial": inicial,
        "nome": dados["nome"].strip(),
        "telefone": dados["telefone"].strip(),
        "pacote": dados["pacote"],
        "fita_led": dados.get("fita_led", "Não selecionado"),
        "alexa": dados.get("alexa", "Não selecionado"),
        "agendamento": "A combinar no WhatsApp",
        "total": f"R$ {total:.2f}",
        "status": "Pendente"
    }

    pedidos.insert(0, novo_pedido)
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=2)

def renderizar_pacote():
    if "etapa" not in st.session_state:
        st.session_state["etapa"] = 1
    if "dados_pedido" not in st.session_state:
        st.session_state["dados_pedido"] = {
            "pacote": "Completo",
            "valor_base": 199.0,
            "fita_led": "Fita LED - 2m",
            "valor_fita": 99.0,
            "alexa": "Echo Dot 5ª Geração",
            "valor_alexa": 349.0,
            "nome": "",
            "telefone": ""
        }

    etapa = st.session_state["etapa"]

    if st.button("← Voltar"):
        if etapa > 1:
            st.session_state["etapa"] -= 1
            st.rerun()
        else:
            st.session_state["pagina_atual"] = "home"
            st.rerun()

    exibir_logo_tech_home("Monte seu Pacote • Automação Residencial")

    st.markdown(f'<div style="font-size: 0.85rem; color: #60A5FA; font-weight: 600; margin-bottom: 6px;">Etapa {etapa} de 6</div>', unsafe_allow_html=True)
    st.progress(etapa / 6.0)
    st.markdown("<br>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # ETAPA 1: ESCOLHER PACOTE BASE
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
            st.markdown(f'<div class="{classe_card}"><div style="font-weight: 700; color: #FFFFFF; font-size: 1.05rem;">{nome}</div><div style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px;">{desc}</div><div style="color: #2589F5; font-weight: 700; font-size: 0.95rem; margin-top: 8px;">R$ {preco:.2f}</div></div>', unsafe_allow_html=True)
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

        st.markdown('<div class="info-box-blue">ℹ️ A fita LED é instalada com fita dupla-face 3M e fonte incluída. Controlável via app.</div>', unsafe_allow_html=True)

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

        st.markdown(f'<div class="tech-card"><div style="color: #60A5FA; font-weight: 700; margin-bottom: 8px;">Itens Selecionados:</div><div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 4px;">• <b>Pacote:</b> {d["pacote"]}</div><div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 4px;">• <b>Iluminação:</b> {d["fita_led"]}</div><div style="color: #F8FAFC; font-size: 0.9rem; margin-bottom: 8px;">• <b>Assistente:</b> {d["alexa"]}</div><hr style="border-color: #1E293B; margin: 10px 0;"><div style="color: #2589F5; font-weight: 800; font-size: 1.1rem;">Subtotal: R$ {total_parcial:.2f}</div></div>', unsafe_allow_html=True)

        if st.button("Avançar para Contato →", key="avancar_contato"):
            st.session_state["etapa"] = 5
            st.rerun()

    # -------------------------------------------------------------
    # ETAPA 5: DADOS DO CLIENTE
    # -------------------------------------------------------------
    elif etapa == 5:
        st.markdown("### 5. Seus Dados de Contato")
        st.markdown("<p style='color: #94A3B8; font-size: 0.9rem;'>Informe seus dados para finalizarmos o atendimento:</p>", unsafe_allow_html=True)

        nome_cliente = st.text_input("Seu Nome Completo", value=st.session_state["dados_pedido"]["nome"])
        tel_cliente = st.text_input("Seu WhatsApp (com DDD)", value=st.session_state["dados_pedido"]["telefone"])

        st.session_state["dados_pedido"]["nome"] = nome_cliente
        st.session_state["dados_pedido"]["telefone"] = tel_cliente

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Ver Resumo Final 🚀", key="ver_resumo_final"):
            if not nome_cliente.strip() or not tel_cliente.strip():
                st.warning("Por favor, preencha seu nome e WhatsApp.")
            else:
                st.session_state["etapa"] = 6
                st.rerun()

    # -------------------------------------------------------------
    # ETAPA 6: FINALIZAÇÃO E BOTÃO WHATSAPP
    # -------------------------------------------------------------
    elif etapa == 6:
        st.markdown("### 6. Pedido Pronto!")
        d = st.session_state["dados_pedido"]
        total_final = d.get("valor_base", 199.0) + d.get("valor_fita", 99.0) + d.get("valor_alexa", 349.0)

        # Salva o pedido automaticamente na Área dos Funcionários
        salvar_pedido_real(d, total_final)

        st.markdown(f'<div class="tech-card"><div style="color: #60A5FA; font-weight: 700; margin-bottom: 10px;">Resumo TECH HOME:</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">👤 <b>Cliente:</b> {d["nome"]}</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">📱 <b>WhatsApp:</b> {d["telefone"]}</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">📦 <b>Pacote:</b> {d["pacote"]}</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">💡 <b>LED:</b> {d["fita_led"]}</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 4px;">🔊 <b>Alexa:</b> {d["alexa"]}</div><div style="color: #F8FAFC; font-size: 0.88rem; margin-bottom: 8px;">📅 <b>Agendamento:</b> A combinar no WhatsApp</div><hr style="border-color: #1E293B; margin: 10px 0;"><div style="color: #2589F5; font-weight: 800; font-size: 1.15rem;">Total Estimado: R$ {total_final:.2f}</div></div>', unsafe_allow_html=True)

        texto_zap = f"Olá! Meu nome é {d['nome']}. Acabei de montar meu pacote na TECH HOME:\n- Pacote: {d['pacote']}\n- LED: {d['fita_led']}\n- Alexa: {d['alexa']}\n- Total: R$ {total_final:.2f}. Gostaria de entrar em contato para dúvidas e acertar data e horário!"
        texto_codificado = urllib.parse.quote(texto_zap)
        link_whatsapp = f"https://wa.me/5585999999999?text={texto_codificado}"

        st.markdown(f'<a href="{link_whatsapp}" target="_blank" class="btn-whatsapp" style="text-align: center; line-height: 1.4;">💬 Entre em contato conosco para dúvidas e acertar algumas coisas como data e horário</a>', unsafe_allow_html=True)