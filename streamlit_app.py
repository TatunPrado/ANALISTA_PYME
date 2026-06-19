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
def _find_in_list(items, name_key):
    name_key = name_key.lower().replace("_", "-").replace(" ", "-")
    for item in items:
        fname = (item.get("filename") or "").lower().replace("_", "-").replace(" ", "-")
        title = (item.get("title") or "").lower().replace("_", "-").replace(" ", "-")
        if name_key in fname or name_key in title:
            return item
    return None


def _extract_body(item, limit=600):
    for key in ("descripción", "description", "descripcion", "summary", "objetivo"):
        body = item.get("sections", {}).get(key, {}).get("body", "")
        if body:
            return body[:limit]
    return (item.get("description") or "")[:limit]


def _artifact_dim_score(dim, artifact):
    """Score how relevant an artifact is to a dimension using its aliases."""
    from KnowledgeEngine.config import get_config
    aliases = get_config().dimension_aliases.get(dim, [dim])
    text = (
        (artifact.get("title") or "") + " " +
        (artifact.get("filename") or "") + " " +
        " ".join(artifact.get("tags", []))
    ).lower()
    score = 0
    for alias in aliases:
        if alias in text:
            score += 1
    return score


def _build_knowledge_section(context, dims):
    """Build a structured knowledge-base block for the prompt."""
    parts = ["=== BASE DE CONOCIMIENTO ==="]

    # 1. Per dimension: agent role + metodologías + frameworks + patrones
    for d in dims:
        label = DIMENSIONES.get(d, d)
        agent_name = AGENTES_POR_DIMENSION.get(d, "")
        parts.append(f"\n--- {label} ---")

        agent_def = _find_in_list(context.get("agents", []), agent_name)
        if agent_def:
            parts.append(agent_def.get("description", ""))
            for sn in agent_def.get("skills", []):
                skill = _find_in_list(context.get("skills", []), sn)
                if skill:
                    parts.append(f"\nMetodología: {skill.get('title', '')}")
                    sd = skill.get("description", "")
                    if sd:
                        parts.append(sd[:400])
                    for sn2, sdata in skill.get("sections", {}).items():
                        body = sdata.get("body", "") if isinstance(sdata, dict) else ""
                        if body and len(body) > 80:
                            parts.append(f"  {body[:400]}")

        for fw in context.get("frameworks", []):
            if _artifact_dim_score(d, fw) > 0:
                parts.append(f"\nMarco: {fw.get('title', '')}")
                body = _extract_body(fw, 500)
                if body:
                    parts.append(body)

        rel_pats = [p for p in context.get("patterns", []) if _artifact_dim_score(d, p) > 0]
        if rel_pats:
            parts.append(f"\nPatrones ({len(rel_pats)} disponibles):")
            for p in rel_pats[:5]:
                pd = p.get("description", "")[:150]
                if pd:
                    parts.append(f"  · {p.get('title', '') or p.get('filename', '')}: {pd}")

        for proc in context.get("processes", []):
            if _artifact_dim_score(d, proc) > 0:
                parts.append(f"Proceso: {proc.get('title', '')}")

    # 2. Playbooks (shared)
    for pb in context.get("playbooks", []):
        parts.append(f"\nPlaybook: {pb.get('title', '')}")
        desc = pb.get("description", "")[:300]
        if desc:
            parts.append(desc)

    return "\n".join(parts)


def build_system_prompt(engine, dims):
    context = engine.build_context(dimensions=dims)
    parts = [
        "Sos un consultor senior de Klar Analytics especializado en diagnóstico empresarial para PyMEs.",
        "Tu objetivo es entrevistar al dueño o gerente para relevar información sobre su empresa.",
        "",
        "REGLAS DE CONDUCTA:",
        "- Saludá al usuario y presentate como consultor de Klar Analytics.",
        "- Hacé UNA pregunta por vez. No bombardees.",
        "- Usá tono profesional pero cercano, en español.",
        "- Después de 3-4 intercambios sobre un tema, avanzá al siguiente.",
        "- Basá tus preguntas en las metodologías, marcos y patrones listados.",
        "- Cubrí TODAS las dimensiones seleccionadas.",
        "- Cuando hayas cubierto todas, ofrecé generar el diagnóstico final.",
        "",
    ]
    parts.append(_build_knowledge_section(context, dims))
    parts.extend([
        "",
        "REGLA DE ORO (Micro-Insights):",
        "Cada 3 respuestas del usuario, interrumpí brevemente el formato de preguntas para ofrecer",
        "un 'Micro-Insight' (ej: 'Basado en tu respuesta, esto es un riesgo operativo típico en tu sector...').",
        "Mantené esto breve (máximo 2 líneas). Esto cambia la percepción de 'interrogatorio' a 'asesoría'.",
        "",
        "ESTRUCTURA:",
        "1. Preguntá por el contexto general (rubro, tamaño, mercado).",
        "2. Abordá cada dimensión con preguntas basadas en sus metodologías y marcos.",
        "3. Identificá patrones aplicables según lo que cuenta el cliente.",
        "4. Cada 3 respuestas, ofrecé un Micro-Insight de 1-2 líneas.",
        "5. Al final, preguntá si quiere agregar algo más.",
        "",
        "FORMATO: español, párrafos cortos, emojis con moderación.",
    ])
    return "\n".join(parts)


def build_report_prompt(engine, dims, transcript):
    context = engine.build_context(dimensions=dims)
    parts = [
        "Sos un consultor senior de Klar Analytics. Generá un diagnóstico empresarial estructurado.",
        "",
        "DIMENSIONES ANALIZADAS: " + ", ".join(DIMENSIONES.get(d, d) for d in dims),
        "",
    ]
    parts.append(_build_knowledge_section(context, dims))
    parts.extend([
        "",
        "TRANSCRIPCIÓN DE LA ENTREVISTA:",
        transcript,
        "",
        "INSTRUCCIONES — Generá un informe en markdown con esta estructura:",
        "",
        "# Diagnóstico Klar Analytics — [Nombre de la empresa]",
        "",
        "## Resumen Ejecutivo",
        "2-3 párrafos citando los marcos usados.",
        "",
        "## Análisis por Dimensión",
        "### [Nombre de la dimensión]",
        "- **Metodología aplicada:** [frameworks/patrones usados]",
        "- **Hallazgos clave:**",
        "- **Fortalezas:**",
        "- **Áreas de mejora:**",
        "- **Recomendaciones:** (2-3 acciones citando patrones)",
        "",
        "## Priorización",
        "| Prioridad | Acción | Dimensión | Impacto | Plazo |",
        "",
        "## Plan de Acción",
        "3-5 acciones con plazo y responsable.",
        "",
        "IMPORTANTE: citá los frameworks y patrones de Klar Analytics usados. Sé específico, no genérico. Extensión: 1000-2000 palabras.",
    ])
    return "\n".join(parts)

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

def page_diagnosis():
    engine = load_engine()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password",
                                     help="Obtené tu key gratis en https://aistudio.google.com/apikey")

    if not api_key:
        st.info("### Paso 1: Configurá tu API Key\n\n1. Andá a https://aistudio.google.com/apikey\n2. Creá una API Key (gratis, sin tarjeta)\n3. Pegala en el campo de la barra lateral 🔑\n\nDespués podés empezar el diagnóstico.")
        return

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
                ok = True
                with st.spinner("Conectando con Gemini..."):
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=api_key)
                        system_prompt = build_system_prompt(engine, dims)
                        model = genai.GenerativeModel("gemini-3.1-flash-lite", system_instruction=system_prompt)
                        chat = model.start_chat(history=[])
                        greeting = chat.send_message(
                            f"El cliente se llama {company}. "
                            f"Rubro: {industry or 'no especificado'}. "
                            f"Empleados: {employees}. "
                            + (f"Contexto: {extra}. " if extra else "")
                            + "Iniciá la entrevista. Presentate como consultor de Klar Analytics."
                        )
                        st.session_state.company = company
                        st.session_state.industry = industry
                        st.session_state.employees = employees
                        st.session_state.selected_dims = dims
                        st.session_state.gemini_chat = chat
                        st.session_state.chat_history = [{"role": "assistant", "content": greeting.text}]
                        st.session_state.phase = "chat"
                    except Exception as e:
                        ok = False
                        st.error(f"Error conectando con Gemini. Revisá tu API Key e intentá de nuevo.\nDetalle: {e}")
                if ok:
                    st.rerun()
        return

    # ═══════════════════════════════════════════════════
    #  FASE 2: CHAT — conversación interactiva
    # ═══════════════════════════════════════════════════
    if phase == "chat":
        st.markdown(f"### Conversación con {st.session_state.company}")
        dims = st.session_state.selected_dims
        badges = "".join(f'<span class="badge badge-blue" style="background:{BLUE_100};color:{BLUE_800};padding:2px 10px;border-radius:12px;margin:2px;font-size:0.8rem;">{DIMENSIONES.get(d,d)}</span>' for d in dims)
        st.markdown(f"Dimensiones activas: {badges}", unsafe_allow_html=True)

        dims_totales = len(st.session_state.selected_dims)
        user_msgs = sum(1 for m in st.session_state.chat_history if m["role"] == "user")
        progreso = min(user_msgs / (dims_totales * 3), 1.0)
        st.progress(progreso, text=f"Progreso del diagnóstico — {user_msgs} respuestas dadas")

        st.markdown("---")

        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Escribí tu respuesta..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            ok = True
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                response = st.session_state.gemini_chat.send_message(prompt)
                st.session_state.chat_history.append({"role": "assistant", "content": response.text})
            except Exception as e:
                ok = False
                st.error(f"Error de conexión: {e}")
            if ok:
                st.rerun()

        c1, c2, c3 = st.columns([2, 2, 1])
        with c1:
            if st.button("📋 Generar diagnóstico final", type="primary", use_container_width=True):
                transcript = "\n".join(
                    f"{'Cliente' if m['role']=='user' else 'Consultor'}: {m['content']}"
                    for m in st.session_state.chat_history
                )
                ok = True
                with st.spinner("Generando diagnóstico..."):
                    try:
                        import google.generativeai as genai
                        genai.configure(api_key=api_key)
                        report_prompt = build_report_prompt(engine, dims, transcript)
                        model = genai.GenerativeModel("gemini-3.1-flash-lite")
                        resp = model.generate_content(report_prompt)
                        st.session_state.report = resp.text
                        st.session_state.phase = "done"
                    except Exception as e:
                        ok = False
                        st.error(f"Error al generar diagnóstico: {e}")
                if ok:
                    st.rerun()
        with c2:
            pass
        with c3:
            if st.button("↺ Reiniciar"):
                st.session_state.phase = "setup"
                st.rerun()
        return

    # ═══════════════════════════════════════════════════
    #  FASE 3: DIAGNÓSTICO COMPLETO
    # ═══════════════════════════════════════════════════
    st.markdown("## Diagnóstico completo")
    st.markdown(st.session_state.report)
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button("📥 Descargar Markdown", data=st.session_state.report.encode("utf-8"),
                           file_name=f"diagnostico_{st.session_state.company}.md", mime="text/markdown", use_container_width=True)
    with c2:
        st.download_button("📥 Descargar JSON",
                           data=json.dumps({"company": st.session_state.company, "report": st.session_state.report}, indent=2, ensure_ascii=False).encode("utf-8"),
                           file_name=f"diagnostico_{st.session_state.company}.json", mime="application/json", use_container_width=True)
    with c3:
        if st.button("🔄 Nuevo diagnóstico", use_container_width=True):
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
