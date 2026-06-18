"""
Klar Analytics — Diagnóstico Empresarial Interactivo
App Streamlit con chat vía Google Gemini + KnowledgeEngine.
"""
import sys, os, json, time
from pathlib import Path

import streamlit as st
from PIL import Image, ImageDraw

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))

from KnowledgeEngine import KnowledgeEngine

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

CSS = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    * {{ font-family: 'Inter', sans-serif; }}
    .stApp {{ background-color: {GRAY_50}; }}
    .main .block-container {{ padding-top: 2rem; }}
    h1, h2, h3 {{ color: {BLUE_800} !important; font-weight: 600 !important; }}
    .stButton button {{ background-color: {BLUE_800}; color: white; border-radius: 8px; padding: 0.5rem 2rem; font-weight: 500; border: none; }}
    .stButton button:hover {{ background-color: {BLUE_700}; }}
    .card {{ background: white; border-radius: 12px; padding: 1.5rem; box-shadow: 0 2px 8px rgba(10,37,64,0.06); margin-bottom: 1rem; }}
    .kpi-box {{ background: white; border-radius: 12px; padding: 1rem 1.5rem; text-align: center; box-shadow: 0 2px 8px rgba(10,37,64,0.06); border-top: 3px solid {BLUE_500}; }}
    .kpi-number {{ font-size: 2rem; font-weight: 700; color: {BLUE_800}; }}
    .kpi-label {{ font-size: 0.8rem; color: {GRAY_400}; text-transform: uppercase; letter-spacing: 0.05em; }}
    .stChatFocused {{ border-color: {BLUE_500} !important; }}
    footer {{ display: none; }}
</style>
"""

def _make_logo_img():
    img = Image.new("RGBA", (300, 70), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    pts = [(20, 55), (55, 50), (90, 45), (130, 15), (150, 10), (175, 20), (210, 25)]
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=BLUE_800, width=2)
    draw.ellipse([144, 4, 156, 16], fill=BLUE_800)
    draw.ellipse([147, 7, 153, 13], fill=TEAL_500)
    return img

@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng

def build_system_prompt(engine, dims):
    context = engine.build_context(dimensions=dims)
    lines = [
        "Sos un consultor senior de Klar Analytics especializado en diagnóstico empresarial para PyMEs.",
        "Tu objetivo es entrevistar al dueño o gerente de una PyME para relevar información sobre su empresa.",
        "",
        "REGLAS DE CONDUCTA:",
        "- Saludá al usuario y presentate como consultor de Klar Analytics.",
        "- Hacé UNA pregunta por vez. No bombardees con preguntas múltiples.",
        "- Usá un tono profesional pero cercano, en español.",
        "- Después de 3-4 intercambios sobre un tema, avanzá naturalmente al siguiente.",
        "- Cubrí TODAS las dimensiones seleccionadas por el usuario.",
        "- Cuando hayas cubierto todas, ofrecé generar el diagnóstico final.",
        "",
        "DIMENSIONES A DIAGNOSTICAR:",
    ]
    for d in dims:
        label = DIMENSIONES.get(d, d)
        agent_name = AGENTES_POR_DIMENSION.get(d, "")
        agent_def = None
        for a in context.get("agents", []):
            if agent_name.lower() in (a.get("filename") or "").lower():
                agent_def = a
                break
        lines.append(f"\n--- {label} (agente: {agent_name}) ---")
        if agent_def:
            lines.append(agent_def.get("description", ""))
            skills = agent_def.get("skills", [])
            if skills:
                lines.append("Áreas de indagación: " + ", ".join(skills))
        for fw in context.get("frameworks", []):
            title = (fw.get("title") or "").lower()
            if d in title or d[:-1] in title:
                body = fw.get("sections", {}).get("descripción", {}).get("body", "") or fw.get("sections", {}).get("description", {}).get("body", "")
                if body:
                    lines.append(f"Marco de referencia: {body[:500]}")

    lines.extend([
        "",
        "ESTRUCTURA DE LA ENTREVISTA:",
        "1. Preguntá primero por el contexto general de la empresa (rubro, tamaño, mercado).",
        "2. Luego abordá cada dimensión una por una, con preguntas específicas.",
        "3. Finalmente, preguntá si quiere agregar algo más.",
        "",
        "FORMATO DE RESPUESTA:",
        "- Respondé en español, con párrafos cortos.",
        "- Usá emojis con moderación.",
        "- Si el usuario se desvía, retomá el hilo amablemente.",
        "- Cuando termines todas las dimensiones, decí: 'He cubierto todas las áreas. ¿Querés que genere el diagnóstico final?'",
    ])
    return "\n".join(lines)

def build_report_prompt(engine, dims, transcript):
    context = engine.build_context(dimensions=dims)
    lines = [
        "Sos un consultor senior de Klar Analytics. Generá un diagnóstico empresarial estructurado en base a la siguiente conversación con el cliente.",
        "",
        "DIMENSIONES ANALIZADAS: " + ", ".join(DIMENSIONES.get(d, d) for d in dims),
        "",
        "TRANSCRIPCIÓN DE LA ENTREVISTA:",
        transcript,
        "",
        "INSTRUCCIONES:",
        "Generá un informe con esta estructura exacta (en markdown):",
        "",
        "# Diagnóstico Klar Analytics — [Nombre de la empresa]",
        "",
        "## Resumen Ejecutivo",
        "2-3 párrafos con los hallazgos más importantes.",
        "",
        "## Análisis por Dimensión",
        "Para cada dimensión analizada:",
        "### [Nombre de la dimensión]",
        "- **Hallazgos clave:** (2-3 puntos)",
        "- **Fortalezas detectadas:**",
        "- **Áreas de mejora:**",
        "- **Recomendaciones:** (2-3 acciones concretas)",
        "",
        "## Priorización",
        "Ordenar las recomendaciones por impacto y urgencia (tabla simple):",
        "| Prioridad | Acción | Dimensión | Impacto |",
        "",
        "## Plan de Acción",
        "3-5 acciones concretas con plazo estimado y responsable sugerido.",
        "",
        "IMPORTANTE:",
        "- Usá los frameworks y metodologías de Klar Analytics como referencia.",
        "- Sé específico, no genérico. Basate en lo que dijo el usuario.",
        "- Si faltó información en alguna dimensión, mencionarlo como limitación.",
        "- Extensión: entre 800 y 1500 palabras.",
    ]
    return "\n".join(lines)

def page_home():
    st.markdown("## Bienvenido a Klar Analytics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""<div class="kpi-box"><div class="kpi-number">{len(DIMENSIONES)}</div><div class="kpi-label">Dimensiones de diagnóstico</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""<div class="kpi-box"><div class="kpi-number">{len(AGENTES_POR_DIMENSION)}</div><div class="kpi-label">Agentes especializados</div></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown(f"""<div class="kpi-box"><div class="kpi-number">11</div><div class="kpi-label">Procesos operativos</div></div>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
    <strong>Diagnóstico Empresarial Interactivo con IA</strong><br><br>
    Klar Analytics combina inteligencia artificial con metodologías probadas para analizar tu PyME.<br>
    Conversá con nuestro consultor IA sobre tu empresa y recibí un diagnóstico completo con
    hallazgos, priorización y plan de acción personalizado.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Cómo funciona")
    cols = st.columns(4)
    pasos = ["1. Configurá tu API Key de Gemini", "2. Cargá los datos básicos de tu empresa", "3. Conversá con el consultor IA", "4. Descargá el diagnóstico"]
    for i, (col, paso) in enumerate(zip(cols, pasos)):
        with col:
            st.markdown(f"""<div class="card" style="text-align:center; min-height: 100px;"><div style="font-size:1.8rem; color:{BLUE_500}; font-weight:700;">{i+1}</div><div style="font-size:0.85rem; color:{GRAY_600};">{paso}</div></div>""", unsafe_allow_html=True)
    if st.button("Comenzar diagnóstico →", type="primary"):
        st.session_state["page"] = "diagnosis"
        st.rerun()

def reset_diagnosis():
    keys = ["chat_history", "diagnosis_done", "report"]
    for k in keys:
        st.session_state.pop(k, None)

def page_diagnosis():
    engine = load_engine()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password",
                                     help="Obtené tu key gratis en https://aistudio.google.com/apikey")

    if not api_key:
        st.info("### Paso 1: Configurá tu API Key\n\n1. Andá a https://aistudio.google.com/apikey\n2. Creá una API Key (gratis, sin tarjeta)\n3. Pegala en el campo de la barra lateral 🔑\n\nDespués podés empezar el diagnóstico.")
        return

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "diagnosis_done" not in st.session_state:
        st.session_state.diagnosis_done = False
    if "report" not in st.session_state:
        st.session_state.report = None
    if "setup_done" not in st.session_state:
        st.session_state.setup_done = False

    # ── SETUP ──
    if not st.session_state.setup_done:
        with st.form("setup"):
            st.markdown("### Datos de la empresa")
            col1, col2 = st.columns(2)
            with col1:
                company = st.text_input("Nombre de la empresa", placeholder="Ej: MiPyME S.A.")
                industry = st.selectbox("Industria", ["", "Retail", "Manufactura", "Servicios", "Tecnología", "Agro", "Salud", "Educación", "Construcción", "Logística", "Otro"])
            with col2:
                employees = st.number_input("Empleados", min_value=1, max_value=5000, value=10)
                st.markdown("<br>", unsafe_allow_html=True)
                extra = st.text_area("Contanos brevemente sobre tu empresa (opcional)", placeholder="Rubro, mercado, desafíos principales...", height=80)
            st.markdown("### Dimensiones a diagnosticar")
            dims = []
            cols_dim = st.columns(3)
            for i, (key, label) in enumerate(DIMENSIONES.items()):
                with cols_dim[i % 3]:
                    if st.checkbox(label, value=(key in ("finanzas", "operaciones", "estrategia"))):
                        dims.append(key)
            if st.form_submit_button("Iniciar conversación con el consultor", type="primary", use_container_width=True):
                if not company:
                    st.error("Ingresá el nombre de la empresa.")
                elif not dims:
                    st.error("Seleccioná al menos una dimensión.")
                else:
                    st.session_state.company = company
                    st.session_state.industry = industry
                    st.session_state.employees = employees
                    st.session_state.selected_dims = dims
                    st.session_state.extra_context = extra
   # ── INICIALIZAR SESIÓN ──
for key in ("chat_history", "phase", "report"):
    if key not in st.session_state:
        st.session_state[key] = [] if key == "chat_history" else (None if key == "report" else "setup")

phase = st.session_state.phase
    # ═══════════════════════════════════════════════════
    #  FASE 1: SETUP — formulario inicial
    # ═══════════════════════════════════════════════════
    if phase == "setup":
        st.markdown("### Datos de la empresa")
        c1, c2 = st.columns(2)
        with c1:
            company = st.text_input("Nombre de la empresa", key="f_company", placeholder="Ej: MiPyME S.A.")
            industry = st.selectbox("Industria", ["", "Retail", "Manufactura", "Servicios", "Tecnología", "Agro", "Salud", "Educación", "Construcción", "Logística", "Otro"], key="f_industry")
        with c2:
            employees = st.number_input("Empleados", min_value=1, max_value=5000, value=10, key="f_employees")
            extra = st.text_area("Contanos brevemente sobre tu empresa", placeholder="Rubro, mercado, desafíos principales...", height=80, key="f_extra")
        st.markdown("### Dimensiones a diagnosticar")
        cols_dim = st.columns(3)
        dims = []
        for i, (key, label) in enumerate(DIMENSIONES.items()):
            with cols_dim[i % 3]:
                if st.checkbox(label, value=(key in ("finanzas", "operaciones", "estrategia")), key=f"dim_{key}"):
                    dims.append(key)

        if st.button("🚀 Iniciar conversación con el consultor", type="primary", use_container_width=True):
            errores = []
            if not company: errores.append("Ingresá el nombre de la empresa.")
            if not dims: errores.append("Seleccioná al menos una dimensión.")
            if errores:
                for e in errores: st.error(e)
            else:
                with st.spinner("Conectando con Gemini..."):
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=api_key)
                        system_prompt = build_system_prompt(engine, dims)
                        model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=system_prompt)
                        chat = model.start_chat(history=[])
                        greeting = chat.send_message(
                            f"El cliente se llama {company}. "
                            f"Rubro: {industry}. "
                            f"Rubro: {industry or 'no especificado'}. "
                            f"Empleados: {employees}. "
                            f"{'Contexto adicional: ' + extra if extra else ''}"
                            f"Iniciá la entrevista. Presentate como consultor de Klar Analytics."
                            + (f"Contexto: {extra}. " if extra else "")
                            + "Iniciá la entrevista. Presentate como consultor de Klar Analytics."
                        )
                        st.session_state.company = company
                        st.session_state.industry = industry
                        st.session_state.employees = employees
                        st.session_state.selected_dims = dims
                        st.session_state.gemini_chat = chat
                        st.session_state.chat_history.append({"role": "assistant", "content": greeting.text})
                        st.session_state.chat_history = [{"role": "assistant", "content": greeting.text}]
                        st.session_state.phase = "chat"
                    except Exception as e:
                        st.error(f"Error al conectar con Gemini: {e}")
                        st.error(f"Error conectando con Gemini. Revisá tu API Key e intentá de nuevo.\nDetalle: {e}")
                    st.rerun()
        return

    # ── CHAT ──
    if not st.session_state.diagnosis_done:
    # ═══════════════════════════════════════════════════
    #  FASE 2: CHAT — conversación interactiva
    # ═══════════════════════════════════════════════════
    if phase == "chat":
        st.markdown(f"### Conversación con {st.session_state.company}")
        dims = st.session_state.selected_dims
        badges = "".join(f'<span class="badge badge-blue" style="background:{BLUE_100};color:{BLUE_800};padding:2px 10px;border-radius:12px;margin:2px;font-size:0.8rem;">{DIMENSIONES.get(d,d)}</span>' for d in dims)
        st.markdown(f"Dimensiones activas: {badges}", unsafe_allow_html=True)
        st.markdown("---")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Escribí tu respuesta..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                chat = st.session_state.gemini_chat
                response = chat.send_message(prompt)
                response = st.session_state.gemini_chat.send_message(prompt)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Error: {e}")
                st.error(f"Error de conexión: {e}")
            st.rerun()

        col1, col2 = st.columns([1, 4])
        with col1:
        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            if st.button("📋 Generar diagnóstico final", type="primary", use_container_width=True):
                transcript = "\n".join(
                    f"{'Cliente' if m['role']=='user' else 'Consultor'}: {m['content']}"
                    for m in st.session_state.chat_history
                )
                report_prompt = build_report_prompt(engine, dims, transcript)
                try:
                    import google.generativeai as genai
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel("gemini-2.0-flash")
                    report_resp = model.generate_content(report_prompt)
                    st.session_state.report = report_resp.text
                    st.session_state.diagnosis_done = True
                except Exception as e:
                    st.error(f"Error al generar diagnóstico: {e}")
                with st.spinner("Generando diagnóstico..."):
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=api_key)
                        report_prompt = build_report_prompt(engine, dims, transcript)
                        model = genai.GenerativeModel("gemini-2.0-flash")
                        resp = model.generate_content(report_prompt)
                        st.session_state.report = resp.text
                        st.session_state.phase = "done"
                    except Exception as e:
                        st.error(f"Error al generar diagnóstico: {e}")
                st.rerun()
        with col2:
            if st.button("↺ Empezar de nuevo"):
                reset_diagnosis()
        with c2:
            pass
        with c3:
            if st.button("↺ Reiniciar"):
                st.session_state.phase = "setup"
                st.rerun()
        return

    # ── REPORTE FINAL ──
    # ═══════════════════════════════════════════════════
    #  FASE 3: DIAGNÓSTICO COMPLETO
    # ═══════════════════════════════════════════════════
    st.markdown("## Diagnóstico completo")
    st.markdown(st.session_state.report)
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button("📥 Descargar Markdown", data=st.session_state.report.encode("utf-8"),
                           file_name=f"diagnostico_{st.session_state.company}.md", mime="text/markdown", use_container_width=True)
    with col2:
    with c2:
        st.download_button("📥 Descargar JSON",
                           data=json.dumps({"company": st.session_state.company, "report": st.session_state.report}, indent=2, ensure_ascii=False).encode("utf-8"),
                           file_name=f"diagnostico_{st.session_state.company}.json", mime="application/json", use_container_width=True)
    with col3:
    with c3:
        if st.button("🔄 Nuevo diagnóstico", use_container_width=True):
            reset_diagnosis()
            st.session_state.phase = "setup"
            st.rerun()

def main():
    st.set_page_config(
        page_title="Klar Analytics — Diagnóstico Empresarial",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(CSS, unsafe_allow_html=True)

    with st.sidebar:
        logo = _make_logo_img()
        st.image(logo, width=220)
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.8rem; margin-top:-0.3rem;">Claridad que transforma decisiones</div>', unsafe_allow_html=True)
        st.markdown("---")
        menu = st.radio("", ["Inicio", "Diagnóstico"],
                        index=0 if st.session_state.get("page") != "diagnosis" else 1,
                        label_visibility="collapsed")
        st.markdown("---")
        st.markdown(f'<div style="color:{GRAY_400}; font-size:0.75rem;">Powered by Gemini + KnowledgeEngine<br>{len(DIMENSIONES)} dimensiones · {len(AGENTES_POR_DIMENSION)} agentes<br>Klar Analytics © 2026</div>', unsafe_allow_html=True)

    if menu == "Diagnóstico" or st.session_state.get("page") == "diagnosis":
        st.session_state["page"] = "diagnosis"
        page_diagnosis()
    else:
        if "page" in st.session_state:
            st.session_state.pop("page", None)
        page_home()

if __name__ == "__main__":
    main()
