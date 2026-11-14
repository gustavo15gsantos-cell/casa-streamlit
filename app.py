from datetime import datetime
import streamlit as st

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="TECH HOME • Automação Residencial e IoT",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================================
# ESTILO GLOBAL (TECHFLUX DARK + LOGO EM HTML/CSS PURO)
# ==========================================
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    .stApp {
        background-color: #020617;
        color: #F8FAFC;
        font-family: 'Inter', sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    section[data-testid="stSidebar"] {
        background-color: #050811;
        border-right: 1px solid rgba(56, 189, 248, 0.15);
    }

    /* Logo profissional em HTML puro (sem erros de ficheiro) */
    .brand-logo-container {
        text-align: center;
        padding: 10px 0;
    }
    .brand-logo {
        font-size: 1.5rem;
        font-weight: 800;
        letter-spacing: 2px;
        color: #FFFFFF;
        display: inline-block;
    }
    .brand-logo span {
        color: #38BDF8;
    }
    .brand-sub {
        font-size: 0.65rem;
        color: #94A3B8;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        margin-top: 4px;
        font-weight: 600;
    }

    .tech-card {
        background: linear-gradient(145deg, #090D16 0%, #020617 100%);
        border: 1px solid rgba(56, 189, 248, 0.22);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }

    .hero-card {
        background: linear-gradient(145deg, #090D16 0%, #020617 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 18px;
        padding: 28px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
    }

    .tech-badge {
        display: inline-block;
        background: rgba(56, 189, 248, 0.1);
        color: #38BDF8;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        padding: 5px 12px;
        border-radius: 20px;
        border: 1px solid rgba(56, 189, 248, 0.3);
        margin-bottom: 12px;
    }

    .img-desktop { display: block; width: 100%; max-width: 820px; margin: 0 auto 24px auto; }
    .img-mobile { display: none; }

    @media (max-width: 768px) {
        .img-desktop { display: none; }
        .img-mobile { display: block; width: 100%; margin-bottom: 24px; }
    }

    .stButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%);
        color: #FFFFFF;
        font-weight: 700;
        border-radius: 10px;
        border: 1px solid rgba(56, 189, 248, 0.45);
        padding: 0.65rem 1.2rem;
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0369A1 0%, #075985 100%);
        border-color: #38BDF8;
        box-shadow: 0 6px 20px rgba(56, 189, 248, 0.35);
    }

    .metric-box {
        background: #090D16;
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 18px;
        text-align: center;
    }
</style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# CONTROLE DE ESTADO
# ==========================================
if "pagina_atual" not in st.session_state:
    st.session_state["pagina_atual"] = "inicio"

if "ordens_servico" not in st.session_state:
    st.session_state["ordens_servico"] = []

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if "orcamento_texto" not in st.session_state:
    st.session_state["orcamento_texto"] = ""

# ==========================================
# BARRA LATERAL (SIDEBAR) COM LOGO
# ==========================================
with st.sidebar:
    st.markdown(
        """
    <div class="brand-logo-container">
        <div class="brand-logo">⚡ TECH<span> HOME</span></div>
        <div class="brand-sub">Infraestrutura Inteligente</div>
    </div>
    <hr style="border-color: rgba(56, 189, 248, 0.18); margin: 14px 0 18px 0;">
    """,
        unsafe_allow_html=True,
    )

    opcoes_menu = {
        "inicio": "🏠 Início",
        "pacote": "⚙️ Configurar Ecossistema",
        "contato": "💬 Dúvidas e Contato",
        "funcionarios": "🔐 Portal Executivo",
    }

    chaves = list(opcoes_menu.keys())
    indice_atual = chaves.index(st.session_state["pagina_atual"])

    escolha = st.radio(
        "Navegação",
        options=chaves,
        format_func=lambda x: opcoes_menu[x],
        index=indice_atual,
        label_visibility="collapsed",
    )

    if escolha != st.session_state["pagina_atual"]:
        st.session_state["pagina_atual"] = escolha
        st.rerun()

# ==========================================
# CABEÇALHO SUPERIOR COM LOGO
# ==========================================


def exibir_logo_topo(subtitulo="Infraestrutura Residencial Inteligente"):
    st.markdown(
        f"""
    <div class="brand-logo-container" style="padding: 10px 0 5px 0;">
        <div class="brand-logo" style="font-size: 2rem;">⚡ TECH<span> HOME</span></div>
        <div class="brand-sub" style="font-size: 0.78rem; letter-spacing: 2px;">{subtitulo}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )


pagina = st.session_state["pagina_atual"]

# ==========================================
# PÁGINA 1: INÍCIO
# ==========================================
if pagina == "inicio":
    exibir_logo_topo("Infraestrutura Residencial Inteligente")

    st.markdown(
        """
    <div class="img-desktop">
        <img src="https://images.unsplash.com/photo-1558002038-1055907df827?auto=format&fit=crop&w=1200&q=80" style="width: 100%; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border: 1px solid rgba(56, 189, 248, 0.25);">
    </div>
    <div class="img-mobile">
        <img src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=600&q=80" style="width: 100%; border-radius: 16px; box-shadow: 0 15px 35px rgba(0,0,0,0.6); border: 1px solid rgba(56, 189, 248, 0.25);">
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="hero-card">
        <div class="tech-badge">⚡ DIVISÃO CORPORATIVA • TECNOLOGIA IOT</div>
        <h1 style="color: #FFFFFF; font-size: 1.75rem; font-weight: 800; line-height: 1.3; margin-bottom: 12px;">
            O futuro da automação residencial de alto padrão.
        </h1>
        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.65; margin: 0;">
            A <b style="color: #38BDF8;">TECH HOME</b> desenvolve e implementa ecossistemas residenciais inteligentes sem obras ou quebra-quebra. Unimos iluminação arquitetônica de precisão, controle elétrico inteligente e comandos por voz com Inteligência Artificial de última geração.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    if st.button("🚀 INICIAR CONFIGURAÇÃO DO ECOSSISTEMA", use_container_width=True):
        st.session_state["pagina_atual"] = "pacote"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    col_esq, col_dir = st.columns(2)
    with col_esq:
        st.markdown(
            """
        <div class="tech-card" style="height: 100%;">
            <h3 style="color: #38BDF8; font-size: 1.08rem; font-weight: 700; margin-bottom: 16px;">
                📊 PADRÃO CORPORATIVO TECH HOME
            </h3>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px;">
                ✅ <b>100% Sem Quebra-Quebra:</b> Instalação limpa via protocolo sem fio de ultra-performance.
            </p>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px;">
                ✅ <b>2 Anos de Garantia:</b> Suporte técnico especializado e direto com nossa equipe de engenharia.
            </p>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin: 0;">
                ✅ <b>Segurança Criptografada:</b> Seus dados e sua rede residencial protegidos contra invasões externas.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with col_dir:
        st.markdown(
            """
        <div class="tech-card" style="height: 100%;">
            <h3 style="color: #38BDF8; font-size: 1.08rem; font-weight: 700; margin-bottom: 16px;">
                🏛️ PILARES DE ENGENHARIA
            </h3>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px;">
                🔹 <b>Automação Modular:</b> Expansão gradual sem necessidade de reestruturação elétrica complexa.
            </p>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin-bottom: 12px;">
                🔹 <b>Iluminação Dinâmica:</b> Cenas personalizadas para descanso, trabalho corporativo ou entretenimento.
            </p>
            <p style="color: #CBD5E1; font-size: 0.9rem; line-height: 1.6; margin: 0;">
                🔹 <b>Integração de Voz:</b> Central inteligente compatível com os principais assistentes do mercado.
            </p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 Acessar Portal Executivo (Equipe)", use_container_width=True):
        st.session_state["pagina_atual"] = "funcionarios"
        st.rerun()

# ==========================================
# PÁGINA 2: CONFIGURAR ECOSSISTEMA
# ==========================================
elif pagina == "pacote":
    exibir_logo_topo("Configurador de Ecossistema IoT")

    st.markdown(
        """
    <div class="tech-card">
        <h3 style="color: #38BDF8; margin-top: 0;">⚙️ Simulador de Módulos Inteligentes</h3>
        <p style="color: #94A3B8; margin-bottom: 0;">Selecione os sistemas desejados para estimar o investimento e enviar para orçamento.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    modulos = {
        "Iluminação Arquitetônica Inteligente (Interruptores touch e dimerização)": 1490.00,
        "Central de Voz & Automação IA (Comandos por voz e rotinas)": 1890.00,
        "Segurança Criptografada & Acesso (Fechadura biométrica e sensores)": 2290.00,
        "Climatização & Cortinas Motorizadas (Controle de ar e persianas)": 1290.00,
    }

    c_mod, c_res = st.columns([1.3, 0.7])
    escolhidos = []
    total = 0.0

    with c_mod:
        for nome, valor in modulos.items():
            valor_str = (
                f"R$ {valor:,.2f}"
                .replace(",", "X")
                .replace(".", ",")
                .replace("X", ".")
            )
            if st.checkbox(f"{nome} — {valor_str}", key=f"chk_{nome}"):
                escolhidos.append(nome.split(" (")[0])
                total += valor

    with c_res:
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
        <div class="tech-card" style="border-color: rgba(56, 189, 248, 0.4);">
            <h4 style="color: #FFFFFF; margin-top: 0;">Resumo do Projeto</h4>
            <p style="color: #CBD5E1; font-size: 0.88rem; line-height: 1.6;">{lista_html}</p>
            <hr style="border-color: rgba(56, 189, 248, 0.2);">
            <div style="font-size: 0.75rem; color: #94A3B8; text-transform: uppercase;">Investimento Estimado</div>
            <div style="font-size: 1.8rem; font-weight: 800; color: #38BDF8; margin-top: 4px;">{total_str}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button(
            "📩 Solicitar Proposta com Esta Configuração", use_container_width=True
        ):
            if escolhidos:
                itens_txt = "\n".join([f"- {item}" for item in escolhidos])
                st.session_state["orcamento_texto"] = (
                    f"Olá! Gostaria de solicitar um orçamento para:\n{itens_txt}\n\nEstimativa: {total_str}"
                )
                st.session_state["pagina_atual"] = "contato"
                st.rerun()
            else:
                st.warning("Selecione pelo menos um módulo.")

# ==========================================
# PÁGINA 3: DÚVIDAS E CONTATO
# ==========================================
elif pagina == "contato":
    exibir_logo_topo("Atendimento e Engenharia")

    col_faq, col_form = st.columns([1.1, 0.9])

    with col_faq:
        st.markdown(
            "<h3 style='color: #38BDF8;'>❓ Perguntas Frequentes</h3>",
            unsafe_allow_html=True,
        )
        with st.expander(
            "1. Preciso quebrar paredes ou passar novos fios?", expanded=True
        ):
            st.write(
                "Não. Utilizamos módulos compactos de comunicação sem fio de alta frequência que se adaptam à sua caixa elétrica atual sem sujeira ou obras."
            )
        with st.expander(
            "2. Se a internet cair, a casa para de funcionar?", expanded=True
        ):
            st.write(
                "De forma alguma. Toda a automação opera em rede local inteligente, mantendo os interruptores físicos e as rotinas locais funcionando normalmente mesmo sem internet."
            )
        with st.expander("3. Como funciona a garantia e o suporte?", expanded=True):
            st.write(
                "Todos os projetos contam com 2 anos de garantia integral nos equipamentos e instalação, com atendimento técnico especializado."
            )

    with col_form:
        st.markdown(
            "<h3 style='color: #38BDF8;'>📩 Solicitar Orçamento</h3>",
            unsafe_allow_html=True,
        )
        with st.form("form_contato", clear_on_submit=True):
            nome = st.text_input(
                "Seu Nome Completo", placeholder="Digite seu nome"
            )
            telefone = st.text_input(
                "WhatsApp ou Telefone", placeholder="(11) 99999-9999"
            )
            mensagem = st.text_area(
                "Detalhes do Projeto / Pacote",
                value=st.session_state["orcamento_texto"],
                height=140,
                placeholder=(
                    "Descreva os ambientes ou módulos que deseja automatizar..."
                ),
            )
            if st.form_submit_button(
                "Enviar Solicitação", use_container_width=True
            ):
                if nome.strip() and telefone.strip():
                    st.success(
                        f"Solicitação enviada com sucesso, {nome}! Entraremos em contato em breve."
                    )
                    st.session_state["orcamento_texto"] = ""
                else:
                    st.error("Por favor, preencha seu nome e telefone.")

# ==========================================
# PÁGINA 4: PORTAL EXECUTIVO (FUNCIONÁRIOS)
# ==========================================
elif pagina == "funcionarios":
    exibir_logo_topo("Portal Executivo • Equipe Técnica")

    if not st.session_state["autenticado"]:
        _, col_login, _ = st.columns([1, 1.2, 1])
        with col_login:
            st.markdown(
                """
            <div class="tech-card" style="text-align: center;">
                <div style="font-size: 2rem; margin-bottom: 8px;">🔐</div>
                <h3 style="color: #FFFFFF; margin-top: 0;">Acesso Restrito</h3>
                <p style="color: #94A3B8; font-size: 0.9rem; margin-bottom: 0;">Área exclusiva para gestão de ordens de serviço da TECH HOME.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

            pin = st.text_input(
                "PIN de Acesso (Padrão: 1234)", type="password", placeholder="••••"
            )
            b1, b2 = st.columns(2)
            with b1:
                if st.button("Entrar com PIN", use_container_width=True):
                    if pin == "1234":
                        st.session_state["autenticado"] = True
                        st.rerun()
                    else:
                        st.error("PIN incorreto.")
            with b2:
                if st.button("Acesso Direto", use_container_width=True):
                    st.session_state["autenticado"] = True
                    st.rerun()
    else:
        t1, t2 = st.columns([4, 1])
        with t1:
            st.markdown(
                "<h3 style='color: #38BDF8; margin: 0;'>📊 Painel Operacional</h3>",
                unsafe_allow_html=True,
            )
            st.caption("Controle real de projetos e ordens de serviço.")
        with t2:
            if st.button("Sair", use_container_width=True):
                st.session_state["autenticado"] = False
                st.rerun()

        lista_os = st.session_state["ordens_servico"]
        total_os = len(lista_os)
        agendados = sum(1 for o in lista_os if o["status"] == "Agendado")
        em_inst = sum(1 for o in lista_os if o["status"] == "Em Instalação")
        concluidos = sum(1 for o in lista_os if o["status"] == "Concluído")

        m1, m2, m3, m4 = st.columns(4)
        m1.markdown(
            f"<div class='metric-box'><div style='color:#94A3B8;font-size:0.75rem;'>TOTAL DE PROJETOS</div><div style='font-size:1.7rem;font-weight:800;color:#FFF;'>{total_os}</div></div>",
            unsafe_allow_html=True,
        )
        m2.markdown(
            f"<div class='metric-box'><div style='color:#94A3B8;font-size:0.75rem;'>AGENDADOS</div><div style='font-size:1.7rem;font-weight:800;color:#F59E0B;'>{agendados}</div></div>",
            unsafe_allow_html=True,
        )
        m3.markdown(
            f"<div class='metric-box'><div style='color:#94A3B8;font-size:0.75rem;'>EM INSTALAÇÃO</div><div style='font-size:1.7rem;font-weight:800;color:#38BDF8;'>{em_inst}</div></div>",
            unsafe_allow_html=True,
        )
        m4.markdown(
            f"<div class='metric-box'><div style='color:#94A3B8;font-size:0.75rem;'>CONCLUÍDOS</div><div style='font-size:1.7rem;font-weight:800;color:#10B981;'>{concluidos}</div></div>",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### ➕ Cadastrar Nova Ordem de Serviço")
        with st.form("nova_os_form", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            with c1:
                cli = st.text_input(
                    "Nome do Cliente", placeholder="Nome do cliente real"
                )
            with c2:
                mod = st.text_input(
                    "Escopo / Módulos", placeholder="Ex: Iluminação + Voz"
                )
            with c3:
                tec = st.text_input(
                    "Técnico Responsável", placeholder="Nome do técnico"
                )

            if st.form_submit_button("Registrar Ordem de Serviço"):
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

        st.markdown("#### 📋 Ordens de Serviço Ativas")
        if not lista_os:
            st.info(
                "Nenhuma ordem de serviço cadastrada ainda. Utilize o formulário acima para registrar o primeiro projeto real."
            )
        else:
            estados = ["Agendado", "Em Instalação", "Concluído"]
            for idx, item in enumerate(lista_os):
                r1, r2, r3, r4, r5 = st.columns([2, 2.5, 1.5, 1.5, 0.8])
                r1.write(f"**{item['cliente']}**")
                r2.write(item["modulo"])
                r3.write(item["tecnico"])
                novo_st = r4.selectbox(
                    "Status",
                    estados,
                    index=estados.index(item["status"]),
                    key=f"st_{item['id']}",
                    label_visibility="collapsed",
                )
                if novo_st != item["status"]:
                    st.session_state["ordens_servico"][idx]["status"] = (
                        novo_st
                    )
                    st.rerun()
                if r5.button("🗑️", key=f"rm_{item['id']}"):
                    st.session_state["ordens_servico"].pop(idx)
                    st.rerun()