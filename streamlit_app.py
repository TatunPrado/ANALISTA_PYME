"""
Klar Analytics — Diagnóstico Empresarial
App Streamlit para uso local y deploy en Streamlit Cloud.
"""
import sys, os, time, json, io
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw

# ── Asegurar que el proyecto está en el path ──
ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))

from KnowledgeEngine import KnowledgeEngine

# ── CONSTANTES DE MARCA ──
BLUE_800 = "#134078"
BLUE_700 = "#1A5A9E"
BLUE_500 = "#3182CE"
BLUE_200 = "#BEE3F8"
BLUE_100 = "#EBF4FF"
TEAL_500 = "#14B8A6"
GRAY_50  = "#F8F9FA"
GRAY_400 = "#9CA3AF"
GRAY_600 = "#4B5563"
GRAY_800 = "#1F2937"

DIMENSIONES = {
    "finanzas":       "Finanzas",
    "estrategia":     "Estrategia",
    "operaciones":    "Operaciones",
    "talento":        "Talento y Organización",
    "riesgos":        "Riesgos",
    "modelo_negocio": "Modelo de Negocio",
    "cliente":        "Cliente y Mercado",
    "marketing":      "Marketing",
    "tecnologia":     "Tecnología",
}

AGENTES_POR_DIMENSION = {
    "finanzas":       "Financial_Analyst",
    "estrategia":     "Strategy_Designer",
    "operaciones":    "Operations_Analyst",
    "talento":        "Organization_Analyst",
    "riesgos":        "Risk_Analyst",
    "modelo_negocio": "Business_Model_Analyst",
    "cliente":        "Business_Diagnosis_Assistant",
    "marketing":      "Business_Diagnosis_Assistant",
    "tecnologia":     "AI_Transformation_Designer",
}

PLANES = {
    "Express":   "Express (3 dimensiones, 7-10 días)",
    "Integral":  "Integral (5+ dimensiones, 14-21 días)",
    "Premium":   "Premium (Integral + taller + 3 meses seguimiento)",
}

# ── LOGO (generado inline) ──
def _make_logo_img():
    img = Image.new("RGBA", (300, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pts = [(20, 55), (55, 50), (90, 45), (130, 15), (150, 10), (175, 20), (210, 25)]
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=BLUE_800, width=2)
    cx, cy = 150, 10
    draw.ellipse([cx-6, cy-6, cx+6, cy+6], fill=BLUE_800)
    draw.ellipse([cx-3, cy-3, cx+3, cy+3], fill=TEAL_500)
    return img


# ── ESTILOS CSS ──
CSS = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}
    .stApp {{ background-color: {GRAY_50}; }}
    .main .block-container {{ padding-top: 2rem; }}
    h1, h2, h3 {{ color: {BLUE_800} !important; font-weight: 600 !important; }}
    .stButton button {{
        background-color: {BLUE_800}; color: white; border-radius: 8px;
        padding: 0.5rem 2rem; font-weight: 500; border: none;
    }}
    .stButton button:hover {{ background-color: {BLUE_700}; }}
    .card {{
        background: white; border-radius: 12px; padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(10,37,64,0.06); margin-bottom: 1rem;
    }}
    .kpi-box {{
        background: white; border-radius: 12px; padding: 1rem 1.5rem;
        text-align: center; box-shadow: 0 2px 8px rgba(10,37,64,0.06);
        border-top: 3px solid {BLUE_500};
    }}
    .kpi-number {{ font-size: 2rem; font-weight: 700; color: {BLUE_800}; }}
    .kpi-label {{ font-size: 0.8rem; color: {GRAY_400}; text-transform: uppercase; letter-spacing: 0.05em; }}
    .prompt-box {{
        background: {BLUE_100}; border-radius: 8px; padding: 1rem;
        font-family: 'Courier New', monospace; font-size: 0.85rem;
        white-space: pre-wrap; border-left: 3px solid {BLUE_500};
    }}
    .badge {{
        display: inline-block; padding: 0.15rem 0.6rem; border-radius: 999px;
        font-size: 0.75rem; font-weight: 500; margin: 0.15rem;
    }}
    .badge-blue {{ background: {BLUE_100}; color: {BLUE_800}; }}
    .badge-teal {{ background: #E6FCF5; color: #0F766E; }}
    footer {{ display: none; }}
</style>
"""


# ── INICIALIZAR ENGINE (cacheada) ──
@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng


# ── HELPERS ──
def make_client_data(form: dict) -> dict:
    return {
        "company":        form.get("company", ""),
        "industry":       form.get("industry", ""),
        "employees":      form.get("employees", 0),
        "annual_revenue": form.get("revenue", ""),
        "legal_name":     form.get("legal_name", ""),
        "tax_id":         form.get("tax_id", ""),
        "website":        form.get("website", ""),
        "contact_name":   form.get("contact_name", ""),
        "contact_email":  form.get("contact_email", ""),
        "contact_phone":  form.get("contact_phone", ""),
        "current_situation": form.get("situation", ""),
        "main_problems":  form.get("problems", ""),
        "expectations":   form.get("expectations", ""),
    }


# ════════════════════════════════════════════════════
#  PÁGINAS
# ════════════════════════════════════════════════════

def page_home():
    st.markdown("## Bienvenido a Klar Analytics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""<div class="kpi-box">
            <div class="kpi-number">{len(DIMENSIONES)}</div>
            <div class="kpi-label">Dimensiones de diagnóstico</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="kpi-box">
            <div class="kpi-number">{len(AGENTES_POR_DIMENSION)}</div>
            <div class="kpi-label">Agentes especializados</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi-box">
            <div class="kpi-number">11</div>
            <div class="kpi-label">Procesos operativos</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <strong>Sistema de Diagnóstico Empresarial Multi-Agente</strong><br><br>
    Klar Analytics combina inteligencia artificial con metodologías de clase mundial
    para analizar tu PyME en profundidad. Seleccioná las dimensiones que querés evaluar,
    cargá los datos de tu empresa y recibí un análisis completo con hallazgos,
    priorización y plan de acción.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Cómo funciona")
    cols = st.columns(4)
    pasos = ["1. Cargá los datos de tu empresa",
             "2. Seleccioná las dimensiones a diagnosticar",
             "3. Ejecutá el análisis multi-agente",
             "4. Descargá el informe completo"]
    for i, (col, paso) in enumerate(zip(cols, pasos)):
        with col:
            st.markdown(f"""<div class="card" style="text-align:center; min-height: 100px;">
                <div style="font-size:1.8rem; color:{BLUE_500}; font-weight:700;">{i+1}</div>
                <div style="font-size:0.85rem; color:{GRAY_600};">{paso}</div>
            </div>""", unsafe_allow_html=True)

    if st.button("Comenzar diagnóstico →", type="primary"):
        st.session_state["page"] = "diagnosis"
        st.rerun()


def page_diagnosis():
    engine = load_engine()

    # ── Layout: dos columnas ──
    col_form, col_result = st.columns([1, 1])

    with col_form:
        st.markdown("### Datos de la empresa")
        with st.container():
            company    = st.text_input("Nombre de la empresa", placeholder="Ej: MiPyME S.A.")
            industry   = st.selectbox("Industria", ["", "Retail", "Manufactura", "Servicios", "Tecnología", "Agro", "Salud", "Educación", "Construcción", "Logística", "Otro"])
            employees  = st.number_input("Empleados", min_value=1, max_value=5000, value=10)
            revenue    = st.text_input("Facturación anual (USD)", placeholder="Ej: 500,000")

        with st.expander("Datos fiscales (opcional)"):
            legal_name  = st.text_input("Razón social", placeholder="Razón social completa")
            tax_id      = st.text_input("RUT / CUIT / NIT", placeholder="Número fiscal")

        with st.expander("Contacto (opcional)"):
            contact_name  = st.text_input("Nombre del contacto", placeholder="Nombre y apellido")
            contact_email = st.text_input("Email", placeholder="correo@ejemplo.com")
            contact_phone = st.text_input("Teléfono", placeholder="+54 11 1234 5678")

        with st.expander("Contexto (opcional)"):
            situation    = st.text_area("Situación actual", placeholder="Describí brevemente la situación actual de la empresa...", height=80)
            problems     = st.text_area("Principales problemas", placeholder="¿Qué problemas están enfrentando?", height=80)
            expectations = st.text_area("Expectativas", placeholder="¿Qué esperan del diagnóstico?", height=80)

        st.markdown("### Dimensiones a diagnosticar")
        dims = []
        for key, label in DIMENSIONES.items():
            if st.checkbox(label, value=(key in ("finanzas", "operaciones", "estrategia"))):
                dims.append(key)

        plan = st.radio("Plan", list(PLANES.keys()), index=1, format_func=lambda x: PLANES[x])

        cols_btn = st.columns([1, 1])
        with cols_btn[0]:
            ejecutar = st.button("▶ Ejecutar diagnóstico", type="primary", use_container_width=True)
        with cols_btn[1]:
            st.button("↺ Limpiar", use_container_width=True)

    # ── Resultados ──
    with col_result:
        if not ejecutar:
            st.markdown("""
            <div class="card" style="text-align:center; padding:3rem; color:{};">
                <div style="font-size:3rem; margin-bottom:1rem;">📋</div>
                <div style="font-size:1.1rem; font-weight:500;">Completá los datos y ejecutá el diagnóstico</div>
                <div style="font-size:0.85rem; margin-top:0.5rem;">Los resultados aparecerán aquí</div>
            </div>
            """.format(GRAY_400), unsafe_allow_html=True)
            return

        if not dims:
            st.error("Seleccioná al menos una dimensión para diagnosticar.")
            return

        if not company:
            st.error("Ingresá el nombre de la empresa.")
            return

        # ── PROCESAR ──
        with st.status("Ejecutando diagnóstico multi-agente...", expanded=True) as status:
            st.write("📂 Cargando base de conocimiento...")
            time.sleep(0.3)

            st.write("🔍 Seleccionando agentes relevantes...")
            client_data = make_client_data(locals())
            context = engine.build_context(dimensions=dims, diagnosis_type=plan.lower())

            agentes_usados = {}
            for dim in dims:
                agent_name = AGENTES_POR_DIMENSION.get(dim, "Business_Diagnosis_Assistant")
                agentes_usados[agent_name] = agentes_usados.get(agent_name, []) + [dim]

            st.write(f"🤖 Activando {len(agentes_usados)} agente(s): {', '.join(agentes_usados.keys())}")
            time.sleep(0.3)

            st.write("📊 Ensamblando prompts de diagnóstico...")
            prompts = {}
            for agent_name in agentes_usados:
                prompt = engine.assemble_prompt(
                    agent_name=agent_name,
                    client_data=client_data,
                    context=context,
                    dimensions=dims,
                )
                prompts[agent_name] = prompt

            st.write("✅ Diagnóstico completado")
            status.update(label="Diagnóstico finalizado", state="complete")

        # ── MOSTRAR RESULTADOS ──
        st.markdown(f"### Resultados — {company}")

        # KPIs rápidos
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f"""<div class="kpi-box">
                <div class="kpi-number">{len(dims)}</div>
                <div class="kpi-label">Dimensiones</div>
            </div>""", unsafe_allow_html=True)
        with k2:
            total_p = sum(len(p.get("patterns", [])) for p in context.get("patterns", []))
            st.markdown(f"""<div class="kpi-box">
                <div class="kpi-number">{total_p}</div>
                <div class="kpi-label">Patrones consultados</div>
            </div>""", unsafe_allow_html=True)
        with k3:
            st.markdown(f"""<div class="kpi-box">
                <div class="kpi-number">{len(agentes_usados)}</div>
                <div class="kpi-label">Agentes activados</div>
            </div>""", unsafe_allow_html=True)
        with k4:
            tk = context.get("metadata", {}).get("total_tokens", 0)
            st.markdown(f"""<div class="kpi-box">
                <div class="kpi-number">{tk:,}</div>
                <div class="kpi-label">Tokens de contexto</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("#### Agentes involucrados")
        for agent_name, dims_list in agentes_usados.items():
            dim_badges = "".join(f'<span class="badge badge-blue">{DIMENSIONES.get(d, d)}</span> ' for d in dims_list)
            st.markdown(f"""<div class="card" style="padding:0.8rem 1.2rem;">
                <strong>{agent_name}</strong><br>
                {dim_badges}
            </div>""", unsafe_allow_html=True)

        # Tabs para ver prompts
        tab_names = list(prompts.keys())
        tabs = st.tabs(tab_names)

        report_data = {"company": company, "dimensions": dims, "agents": {}}

        for i, agent_name in enumerate(tab_names):
            with tabs[i]:
                prompt = prompts[agent_name]

                st.markdown("**System Prompt** (rol del agente + conocimiento)")
                st.markdown(f'<div class="prompt-box">{prompt["system"][:1500]}</div>', unsafe_allow_html=True)

                st.markdown("**User Prompt** (datos del cliente + instrucciones)")
                st.markdown(f'<div class="prompt-box">{prompt["user"][:2000]}</div>', unsafe_allow_html=True)

                report_data["agents"][agent_name] = {
                    "system": prompt["system"],
                    "user": prompt["user"],
                }

        # ── EXPORTAR ──
        st.markdown("### Exportar")
        export_cols = st.columns(3)

        with export_cols[0]:
            json_bytes = json.dumps(report_data, indent=2, ensure_ascii=False).encode("utf-8")
            st.download_button("📥 Descargar JSON", data=json_bytes,
                               file_name=f"diagnostico_{company}_{int(time.time())}.json",
                               mime="application/json", use_container_width=True)

        with export_cols[1]:
            md_content = f"# Diagnóstico Klar Analytics — {company}\n\n"
            md_content += f"**Dimensiones:** {', '.join(DIMENSIONES.get(d, d) for d in dims)}\n\n"
            for agent_name, p in prompts.items():
                md_content += f"## {agent_name}\n\n"
                md_content += f"### System\n```\n{p['system'][:2000]}\n```\n\n"
                md_content += f"### User\n```\n{p['user'][:2000]}\n```\n\n"
            st.download_button("📥 Descargar Markdown", data=md_content.encode("utf-8"),
                               file_name=f"diagnostico_{company}_{int(time.time())}.md",
                               mime="text/markdown", use_container_width=True)

        with export_cols[2]:
            st.markdown(f"""<div style="text-align:center; padding:0.4rem;">
                <div style="font-size:0.8rem; color:{GRAY_400};">Docx pronto</div>
            </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════
#  MAIN
# ════════════════════════════════════════════════════

def main():
    st.set_page_config(
        page_title="Klar Analytics — Diagnóstico Empresarial",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(CSS, unsafe_allow_html=True)

    # ── Sidebar ──
    with st.sidebar:
        logo = _make_logo_img()
        st.image(logo, width=220)
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.8rem; margin-top:-0.3rem;">'
                    'Claridad que transforma decisiones</div>', unsafe_allow_html=True)
        st.markdown("---")

        menu = st.radio("", ["Inicio", "Diagnóstico"],
                        index=0 if st.session_state.get("page") != "diagnosis" else 1,
                        label_visibility="collapsed")

        st.markdown("---")
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.75rem;">'
                    'Knowledge Engine v1.0<br>'
                    f'{len(DIMENSIONES)} dimensiones · {len(AGENTES_POR_DIMENSION)} agentes<br>'
                    'Klar Analytics © 2026</div>', unsafe_allow_html=True)

    # ── Routing de páginas ──
    if menu == "Diagnóstico" or st.session_state.get("page") == "diagnosis":
        st.session_state["page"] = "diagnosis"
        page_diagnosis()
    else:
        if "page" in st.session_state:
            del st.session_state["page"]
        page_home()


if __name__ == "__main__":
    main()
