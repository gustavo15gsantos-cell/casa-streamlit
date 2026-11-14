from datetime import datetime
import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA (OTIMIZADA PARA MOBILE)
# ==========================================
st.set_page_config(
    page_title="TECH HOME • Mobile",
    page_icon="Tech-HOME.jpeg",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ==========================================
# ESTILO MOBILE-FIRST (TECHFLUX DARK)
# ==========================================
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background-color: #020617;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stSidebar"] {display: none;}
    [data-testid="collapsedControl"] {display: none;}

    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 3rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 520px !important;
    }

    .mobile-header {
        background: linear-gradient(145deg, #090D16 0%, #050811 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 8px !important;
    }

    .m-card {
        background: linear-gradient(145deg, #090D16 0%, #020617 100%);
        border: 1px solid rgba(56, 189, 248, 0.22);
        border-radius: 16px;
        padding: 18px;
        margin-bottom: 14px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.45);
    }

    .m-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.12);
        color: #38BDF8;
        font-size: 0.68rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        padding: 4px 10px;
        border-radius: 20px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        margin-bottom: 10px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.9rem;
        border-radius: 12px;
        border: 1px solid rgba(56, 189, 248, 0.45);
        padding: 0.7rem 0.8rem;
        min-height: 46px;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0369A1 0%, #075985 100%);
        border-color: #38BDF8;
    }

    .m-metric {
        background: #090D16;
        border: 1px solid rgba(56, 189, 248, 0.22);
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        margin-bottom: 8px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# CONTROLE DE ESTADO
# ==========================================
if "pagina_mobile" not in st.session_state:
    st.session_state["pagina_mobile"] = "inicio"

if "ordens_servico" not in st.session_state:
    st.session_state["ordens_servico"] = []

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if "orcamento_texto" not in st.session_state:
    st.session_state["orcamento_texto"] = ""

# ==========================================
# CABEÇALHO COM LOGO E MENU SUPERIOR TOUCH (2x2)
# ==========================================
st.markdown(
    """
<div class="mobile-header">
""",
    unsafe_allow_html=True,
)

# Exibição da logo centralizada no cabeçalho mobile
col_l1, col_l2, col_l3 = st.columns([1, 1.6, 1])
with col_l2:
    st.image("Tech-HOME.jpeg", use_container_width=True)

st.markdown(
    """
    <p style="color: #94A3B8; font-size: 0.68rem; text-transform: uppercase; letter-spacing: 1.5px; margin: 4px 0 0 0; font-weight: 600;">
        Automação Residencial • Mobile
    </p>
</div>
""",
    unsafe_allow_html=True,
)

nav1, nav2 = st.columns(2)
with nav1:
    if st.button("🏠 Início", use_container_width=True):
        st.session_state["pagina_mobile"] = "inicio"
        st.rerun()
with nav2:
    if st.button("⚙️ Simulador", use_container_width=True):
        st.session_state["pagina_mobile"] = "pacote"
        st.rerun()

nav3, nav4 = st.columns(2)
with nav3:
    if st.button("💬 Contato", use_container_width=True):
        st.session_state["pagina_mobile"] = "contato"
        st.rerun()
with nav4:
    if st.button("🔐 Equipe", use_container_width=True):
        st.session_state["pagina_mobile"] = "funcionarios"
        st.rerun()

st.markdown(
    "<hr style='border-color: rgba(56, 189, 248, 0.18); margin: 12px 0 16px 0;'>",
    unsafe_allow_html=True,
)

pagina = st.session_state["pagina_mobile"]

# ==========================================
# PÁGINA 1: INÍCIO (MOBILE)
# ==========================================
if pagina == "inicio":
    st.markdown(
        """
    <div class="m-card">
        <div class="m-badge">⚡ TECNOLOGIA IOT RESIDENCIAL</div>
        <h2 style="color: #FFFFFF; font-size: 1.35rem; font-weight: 800; line-height: 1.3; margin-bottom: 10px;">
            O futuro da automação residencial de alto padrão.
        </h2>
        <p style="color: #94A3B8; font-size: 0.88rem; line-height: 1.55; margin: 0;">
            A <b style="color: #38BDF8;">TECH HOME</b> instala ecossistemas inteligentes sem obras ou quebra-quebra. Iluminação arquitetônica, controle elétrico e comandos por voz com IA.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("🚀 CONFIGURAR MEU ECOSSISTEMA", use_container_width=True):
        st.session_state["pagina_mobile"] = "pacote"
        st.rerun()

    st.markdown(
        "<div style='height: 10px;'></div>", unsafe_allow_html=True
    )

    st.markdown(
        """
    <div class="m-card">
        <h3 style="color: #38BDF8; font-size: 1rem; font-weight: 700; margin-bottom: 12px;">
            📊 PADRÃO TECH HOME
        </h3>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin-bottom: 10px;">
            ✅ <b>100% Sem Quebra-Quebra:</b> Instalação limpa sem fio.
        </p>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin-bottom: 10px;">
            ✅ <b>2 Anos de Garantia:</b> Suporte técnico especializado.
        </p>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin: 0;">
            ✅ <b>Segurança Criptografada:</b> Rede local blindada.
        </p>
    </div>

    <div class="m-card">
        <h3 style="color: #38BDF8; font-size: 1rem; font-weight: 700; margin-bottom: 12px;">
            🏛️ PILARES DE ENGENHARIA
        </h3>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin-bottom: 10px;">
            🔹 <b>Automação Modular:</b> Expansão gradual sem reformas.
        </p>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin-bottom: 10px;">
            🔹 <b>Iluminação Dinâmica:</b> Cenas personalizadas por ambiente.
        </p>
        <p style="color: #CBD5E1; font-size: 0.86rem; line-height: 1.55; margin: 0;">
            🔹 <b>Integração de Voz:</b> Controle completo pelo celular ou voz.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ==========================================
# PÁGINA 2: SIMULADOR (MOBILE)
# ==========================================
elif pagina == "pacote":
    st.markdown(
        """
    <div class="m-card">
        <h3 style="color: #38BDF8; font-size: 1.05rem; margin-top: 0;">⚙️ Simulador de Módulos</h3>
        <p style="color: #94A3B8; font-size: 0.85rem; margin-bottom: 0;">Toque nos módulos desejados para calcular o investimento:</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    modulos = {
        "Iluminação Arquitetônica Inteligente": 1490.00,
        "Central de Voz & Automação IA": 1890.00,
        "Segurança Criptografada & Acesso": 2290.00,
        "Climatização & Cortinas Motorizadas": 1290.00,
    }

    escolhidos = []
    total = 0.0

    for nome, valor in modulos.items():
        valor_str = (
            f"R$ {valor:,.2f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
        if st.checkbox(f"{nome} ({valor_str})", key=f"m_chk_{nome}"):
            escolhidos.append(nome)
            total += valor

    total_str = (
        f"R$ {total:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    lista_html = (
        "<br>".join([f"• {e}" for e in escolhidos])
        if escolhidos
        else "Nenhum módulo selecionado."
    )

    st.markdown(
        f"""
    <div class="m-card" style="border-color: rgba(56, 189, 248, 0.45); margin-top: 12px;">
        <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Investimento Estimado</div>
        <div style="font-size: 1.75rem; font-weight: 800; color: #38BDF8; margin: 4px 0 10px 0;">{total_str}</div>
        <p style="color: #CBD5E1; font-size: 0.84rem; line-height: 1.5; margin: 0;">{lista_html}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("📩 Solicitar Proposta", use_container_width=True):
        if escolhidos:
            itens_txt = "\n".join([f"- {item}" for item in escolhidos])
            st.session_state["orcamento_texto"] = (
                f"Olá! Gostaria de solicitar orçamento para:\n{itens_txt}\n\nEstimativa: {total_str}"
            )
            st.session_state["pagina_mobile"] = "contato"
            st.rerun()
        else:
            st.warning("Selecione pelo menos um módulo acima.")

# ==========================================
# PÁGINA 3: DÚVIDAS E CONTATO (MOBILE)
# ==========================================
elif pagina == "contato":
    st.markdown(
        "<h3 style='color: #38BDF8; font-size: 1.1rem;'>📩 Solicitar Orçamento</h3>",
        unsafe_allow_html=True,
    )
    with st.form("m_form_contato", clear_on_submit=True):
        nome = st.text_input("Seu Nome", placeholder="Digite seu nome")
        telefone = st.text_input("WhatsApp", placeholder="(11) 99999-9999")
        mensagem = st.text_area(
            "Detalhes do Projeto",
            value=st.session_state["orcamento_texto"],
            height=120,
            placeholder="Descreva os ambientes que deseja automatizar...",
        )
        if st.form_submit_button("Enviar Solicitação", use_container_width=True):
            if nome.strip() and telefone.strip():
                st.success(
                    f"Solicitação enviada, {nome}! Entraremos em contato."
                )
                st.session_state["orcamento_texto"] = ""
            else:
                st.error("Preencha seu nome e WhatsApp.")

    st.markdown(
        "<h3 style='color: #38BDF8; font-size: 1.1rem; margin-top: 16px;'>❓ Dúvidas Frequentes</h3>",
        unsafe_allow_html=True,
    )
    with st.expander("Preciso quebrar paredes?"):
        st.write(
            "Não. Nossa tecnologia sem fio se adapta à sua caixa elétrica atual sem sujeira ou obras."
        )
    with st.expander("Funciona sem internet?"):
        st.write(
            "Sim. Os interruptores físicos e rotinas locais continuam operando normalmente mesmo sem internet."
        )
    with st.expander("Qual o prazo de garantia?"):
        st.write("2 anos de garantia integral nos equipamentos e instalação.")

# ==========================================
# PÁGINA 4: PORTAL EXECUTIVO (MOBILE)
# ==========================================
elif pagina == "funcionarios":
    if not st.session_state["autenticado"]:
        st.markdown(
            """
        <div class="m-card" style="text-align: center;">
            <div style="font-size: 1.8rem; margin-bottom: 6px;">🔐</div>
            <h3 style="color: #FFFFFF; font-size: 1.1rem; margin: 0;">Portal Executivo</h3>
            <p style="color: #94A3B8; font-size: 0.84rem; margin: 6px 0 0 0;">Acesso exclusivo para equipe TECH HOME.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        pin = st.text_input(
            "PIN de Acesso (Padrão: 1234)", type="password", placeholder="••••"
        )
        if st.button("Entrar com PIN", use_container_width=True):
            if pin == "1234":
                st.session_state["autenticado"] = True
                st.rerun()
            else:
                st.error("PIN incorreto.")
        if st.button("Acesso Direto", use_container_width=True):
            st.session_state["autenticado"] = True
            st.rerun()
    else:
        st.markdown(
            "<h3 style='color: #38BDF8; font-size: 1.1rem; margin-bottom: 10px;'>📊 Painel Operacional</h3>",
            unsafe_allow_html=True,
        )

        lista_os = st.session_state["ordens_servico"]
        total_os = len(lista_os)
        agendados = sum(1 for o in lista_os if o["status"] == "Agendado")
        em_inst = sum(1 for o in lista_os if o["status"] == "Em Instalação")
        concluidos = sum(1 for o in lista_os if o["status"] == "Concluído")

        mc1, mc2 = st.columns(2)
        mc1.markdown(
            f"<div class='m-metric'><div style='color:#94A3B8;font-size:0.7rem;'>TOTAL</div><div style='font-size:1.4rem;font-weight:800;color:#FFF;'>{total_os}</div></div>",
            unsafe_allow_html=True,
        )
        mc2.markdown(
            f"<div class='m-metric'><div style='color:#94A3B8;font-size:0.7rem;'>AGENDADOS</div><div style='font-size:1.4rem;font-weight:800;color:#F59E0B;'>{agendados}</div></div>",
            unsafe_allow_html=True,
        )

        mc3, mc4 = st.columns(2)
        mc3.markdown(
            f"<div class='m-metric'><div style='color:#94A3B8;font-size:0.7rem;'>INSTALANDO</div><div style='font-size:1.4rem;font-weight:800;color:#38BDF8;'>{em_inst}</div></div>",
            unsafe_allow_html=True,
        )
        mc4.markdown(
            f"<div class='m-metric'><div style='color:#94A3B8;font-size:0.7rem;'>CONCLUÍDOS</div><div style='font-size:1.4rem;font-weight:800;color:#10B981;'>{concluidos}</div></div>",
            unsafe_allow_html=True,
        )

        with st.expander("➕ Nova Ordem de Serviço", expanded=True):
            with st.form("m_nova_os", clear_on_submit=True):
                cli = st.text_input(
                    "Cliente", placeholder="Nome do cliente real"
                )
                mod = st.text_input(
                    "Módulos", placeholder="Ex: Iluminação + Voz"
                )
                tec = st.text_input("Técnico", placeholder="Nome do técnico")
                if st.form_submit_button(
                    "Registrar OS", use_container_width=True
                ):
                    if cli.strip() and mod.strip() and tec.strip():
                        st.session_state["ordens_servico"].append({
                            "id": datetime.now().strftime("%H%M%S%f"),
                            "cliente": cli.strip(),
                            "modulo": mod.strip(),
                            "tecnico": tec.strip(),
                            "status": "Agendado",
                        })
                        st.rerun()
                    else:
                        st.warning("Preencha todos os campos.")

        st.markdown("#### 📋 Projetos Registrados")
        if not lista_os:
            st.info("Nenhuma ordem de serviço cadastrada ainda.")
        else:
            estados = ["Agendado", "Em Instalação", "Concluído"]
            for idx, item in enumerate(lista_os):
                st.markdown(
                    f"""
                <div class="m-card" style="padding: 14px; margin-bottom: 8px;">
                    <div style="font-weight: 700; color: #FFFFFF; font-size: 0.95rem;">{item['cliente']}</div>
                    <div style="color: #38BDF8; font-size: 0.82rem; margin: 2px 0;">{item['modulo']}</div>
                    <div style="color: #94A3B8; font-size: 0.78rem;">Técnico: {item['tecnico']}</div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

                b_st, b_del = st.columns([3, 1])
                with b_st:
                    novo_st = st.selectbox(
                        "Status",
                        estados,
                        index=estados.index(item["status"]),
                        key=f"m_st_{item['id']}",
                        label_visibility="collapsed",
                    )
                    if novo_st != item["status"]:
                        st.session_state["ordens_servico"][idx]["status"] = (
                            novo_st
                        )
                        st.rerun()
                with b_del:
                    if st.button(
                        "🗑️", key=f"m_rm_{item['id']}", use_container_width=True
                    ):
                        st.session_state["ordens_servico"].pop(idx)
                        st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sair do Portal", use_container_width=True):
            st.session_state["autenticado"] = False
            st.rerun()