import streamlit as st
from ui.estilo import exibir_logo_tech_home

def renderizar_funcionarios():
    # Topo com botão de voltar para a Home
    if st.button("← Voltar ao Início"):
        st.session_state["pagina_atual"] = "home"
        st.rerun()

    exibir_logo_tech_home("Área do Funcionário • Gestão de Pedidos")

    st.markdown("""
    <div style="margin-bottom: 20px;">
        <h3 style="color: #FFFFFF; font-size: 1.3rem; margin-bottom: 4px;">Lista de Pedidos</h3>
        <p style="color: #94A3B8; font-size: 0.85rem;">Pedidos para o funcionário entrar em contato • 3 pedidos pendentes</p>
    </div>
    """, unsafe_allow_html=True)

    # Lista de pedidos simulados (idêntica às imagens de referência)
    pedidos = [
        {
            "inicial": "JS",
            "nome": "João Silva",
            "telefone": "(11) 98765-4321",
            "pacote": "Pacote Smart Casa",
            "agendamento": "11/11/2026 • 14:30",
            "status": "Pendente",
            "classe_status": "badge-pendente",
            "num_zap": "5511987654321"
        },
        {
            "inicial": "MO",
            "nome": "Maria Oliveira",
            "telefone": "(21) 99423-1108",
            "pacote": "Pacote Segurança Pro",
            "agendamento": "12/10/2026 • 09:00",
            "status": "Confirmado",
            "classe_status": "badge-confirmado",
            "num_zap": "5521994231108"
        },
        {
            "inicial": "CM",
            "nome": "Carlos Mendes",
            "telefone": "(85) 99112-5567",
            "pacote": "Pacote Energia Solar",
            "agendamento": "12/10/2026 • 16:45",
            "status": "Aguardando cliente",
            "classe_status": "badge-pendente",
            "num_zap": "5585991125567"
        }
    ]

    for p in pedidos:
        st.markdown(f"""
        <div class="tech-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <div style="width: 38px; height: 38px; background-color: #2589F5; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; color: white; font-size: 0.85rem;">
                        {p['inicial']}
                    </div>
                    <div>
                        <div style="font-weight: 700; color: #FFFFFF; font-size: 1rem;">{p['nome']}</div>
                        <div style="color: #94A3B8; font-size: 0.82rem;">📞 {p['telefone']}</div>
                    </div>
                </div>
                <div>
                    <span class="{p['classe_status']}">{p['status']}</span>
                </div>
            </div>
            
            <div style="background-color: #0B111E; padding: 8px 12px; border-radius: 8px; margin-bottom: 10px; font-size: 0.85rem; color: #60A5FA; font-weight: 600;">
                📦 {p['pacote']}
            </div>
            
            <div style="color: #94A3B8; font-size: 0.82rem; margin-bottom: 12px;">
                📅 Agendamento: {p['agendamento']}
            </div>

            <a href="https://wa.me/{p['num_zap']}?text=Olá%20{p['nome']},%20recebemos%20seu%20pedido%20na%20TECH%20HOME!%20Vamos%20confirmar%20sua%20instalação?" target="_blank" class="btn-whatsapp" style="padding: 10px; font-size: 0.85rem;">
                💬 Chamar no WhatsApp
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<p style="text-align: center; color: #64748B; font-size: 0.78rem; margin-top: 25px;">Streamlit • Atualizado agora • 3 pedidos</p>', unsafe_allow_html=True)