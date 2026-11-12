import streamlit as st
import json
import os
import re
import urllib.parse
from ui.estilo import exibir_logo_tech_home

ARQUIVO_PEDIDOS = "pedidos_reais.json"

def carregar_pedidos_reais():
    if not os.path.exists(ARQUIVO_PEDIDOS):
        return []
    try:
        with open(ARQUIVO_PEDIDOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def salvar_pedidos_reais(pedidos):
    with open(ARQUIVO_PEDIDOS, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, ensure_ascii=False, indent=2)

def renderizar_funcionarios():
    if st.button("← Voltar ao Início"):
        st.session_state["pagina_atual"] = "home"
        st.rerun()

    exibir_logo_tech_home("Área do Funcionário • Restrito")

    # Sistema de Senha para proteger a Área de Funcionários
    if "admin_autenticado" not in st.session_state:
        st.session_state["admin_autenticado"] = False

    if not st.session_state["admin_autenticado"]:
        st.markdown("""
        <div class="tech-card" style="padding: 24px; text-align: center;">
            <h3 style="color: #FFFFFF; font-size: 1.2rem; margin-bottom: 8px;">🔒 Acesso Restrito</h3>
            <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 16px;">Digite a senha de funcionário para ver os pedidos:</p>
        </div>
        """, unsafe_allow_html=True)

        senha_digitada = st.text_input("Senha de Acesso", type="password", key="input_senha_admin")
        
        if st.button("Entrar no Sistema", key="btn_login_admin"):
            # Senha padrão configurada como 'admin123' (você pode alterar depois se quiser)
            if senha_digitada == "admin123":
                st.session_state["admin_autenticado"] = True
                st.rerun()
            else:
                st.error("Senha incorreta! Acesso negado.")
        return

    # Se já estiver autenticado, exibe o painel de pedidos
    pedidos = carregar_pedidos_reais()
    qtd = len(pedidos)

    st.markdown(f"""
    <div style="margin-bottom: 20px;">
        <h3 style="color: #FFFFFF; font-size: 1.3rem; margin-bottom: 4px;">Gerenciamento de Pedidos Reais</h3>
        <p style="color: #94A3B8; font-size: 0.85rem;">Total de {qtd} {"pedido cadastrado" if qtd == 1 else "pedidos cadastrados"}</p>
    </div>
    """, unsafe_allow_html=True)

    if not pedidos:
        st.markdown("""
        <div class="tech-card" style="text-align: center; padding: 32px 18px;">
            <div style="font-size: 2rem; margin-bottom: 8px;">📭</div>
            <div style="color: #FFFFFF; font-weight: 700; font-size: 1.05rem;">Nenhum pedido realizado ainda</div>
            <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 6px;">Os pedidos feitos pelos clientes no site aparecerão aqui automaticamente.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Listagem limpa usando componentes nativos (sem código HTML quebrado aparecendo)
    for idx, p in enumerate(pedidos):
        with st.container():
            st.markdown(f"""
            <div class="tech-card">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <span style="font-weight: 700; color: #FFFFFF; font-size: 1.05rem;">👤 {p.get('nome', 'Cliente')}</span>
                    <span style="color: #60A5FA; font-size: 0.85rem; font-weight: 600;">📱 {p.get('telefone', '')}</span>
                </div>
                <div style="background-color: #0B111E; padding: 10px; border-radius: 8px; margin-bottom: 8px; font-size: 0.9rem; color: #E2E8F0;">
                    📦 <b>Pacote:</b> {p.get('pacote', '')}<br>
                    💡 <b>LED:</b> {p.get('fita_led', '')} | 🔊 <b>Alexa:</b> {p.get('alexa', '')}<br>
                    💰 <b>Total:</b> {p.get('total', 'R$ 0,00')}
                </div>
                <div style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 12px;">
                    📅 <b>Agendamento:</b> {p.get('agendamento', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Botões de Ação do Funcionário (WhatsApp e Excluir)
            col_zap, col_del = st.columns([2, 1])
            with col_zap:
                numeros_tel = re.sub(r"\D", "", p.get("telefone", ""))
                if numeros_tel and not numeros_tel.startswith("55"):
                    numeros_tel = "55" + numeros_tel
                msg_zap = urllib.parse.quote(f"Olá {p['nome']}, recebemos seu pedido ({p['pacote']}) na TECH HOME! Vamos confirmar sua instalação?")
                st.markdown(f"""
                <a href="https://wa.me/{numeros_tel}?text={msg_zap}" target="_blank" class="btn-whatsapp" style="padding: 10px; font-size: 0.85rem; text-align: center; margin-bottom: 10px;">
                    💬 Chamar no WhatsApp
                </a>
                """, unsafe_allow_html=True)
            
            with col_del:
                if st.button("🗑️ Excluir", key=f"del_pedido_{p.get('id', idx)}_{idx}"):
                    pedidos.pop(idx)
                    salvar_pedidos_reais(pedidos)
                    st.success("Pedido excluído com sucesso!")
                    st.rerun()

            st.markdown("<hr style='border-color: #1E293B; margin: 10px 0;'>", unsafe_allow_html=True)

    if st.button("🔒 Sair do Modo Funcionário"):
        st.session_state["admin_autenticado"] = False
        st.rerun()