"""
Klar Analytics — Diagnóstico Empresarial Interactivo
App Streamlit con chat vía Google Gemini + KnowledgeEngine.
"""
# 1. IMPORTS
import sys, os, json, time
from pathlib import Path
import streamlit as st
from PIL import Image, ImageDraw

# 2. CONSTANTES (Aquí es donde estaba el problema, ponlas aquí arriba)
DIMENSIONES = {
    "finanzas": "Finanzas",
    "estrategia": "Estrategia",
    "operaciones": "Operaciones",
    # ... (el resto de tus dimensiones)
}

AGENTES_POR_DIMENSION = {
    "finanzas": "Financial_Analyst",
    # ... (el resto de tus agentes)
}

# 3. FUNCIONES DE LÓGICA (KnowledgeEngine, llamar_gemini, etc.)
def llamar_gemini(...):
    # ...

# 4. FUNCIONES DE PÁGINAS (page_diagnosis, page_home)
def page_diagnosis():
    # Ahora aquí dentro, DIMENSIONES será reconocida sin problemas
    dims = [k for k, v in DIMENSIONES.items() if st.checkbox(v, key=f"dim_{k}")]
    # ...

# 5. MAIN
def main():
    # ...
ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))
from KnowledgeEngine import KnowledgeEngine

# --- CONFIGURACIÓN Y ESTILOS ---
BLUE_800 = "#134078"
BLUE_700 = "#1A5A9E"
BLUE_500 = "#3182CE"
TEAL_500 = "#14B8A6"
GRAY_50  = "#F8F9FA"
GRAY_400 = "#9CA3AF"
GRAY_600 = "#4B5563"

CSS = f"""<style>
    .stApp {{ background-color: {GRAY_50}; }}
    .kpi-box {{ background: white; border-radius: 12px; padding: 1rem; text-align: center; border-top: 3px solid {BLUE_500}; }}
</style>"""

# --- FUNCIONES AUXILIARES ---
@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng

def llamar_gemini(objeto_gemini, prompt, error_msg="Error desconocido", es_chat=False):
    try:
        with st.spinner("Consultando a la IA..."):
            if es_chat:
                response = objeto_gemini.send_message(prompt)
            else:
                response = objeto_gemini.generate_content(prompt)
            return response.text
    except Exception as e:
        st.error(f"❌ {error_msg}")
        st.exception(e)
        return None

# --- PÁGINA DE DIAGNÓSTICO ---
def page_diagnosis():
    engine = load_engine()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password")

    if not api_key:
        st.info("Configurá tu API Key en la barra lateral.")
        return

    # Inicialización de estado
    for key in ("chat_history", "phase", "report", "selected_dims"):
        if key not in st.session_state:
            st.session_state[key] = [] if key == "chat_history" else (None if key == "report" else "setup")

    # FASE 1: SETUP
    if st.session_state.phase == "setup":
        company = st.text_input("Nombre de la empresa")
        industry = st.selectbox("Industria", ["Retail", "Servicios", "Tecnología", "Otro"])
        employees = st.number_input("Empleados", value=10)
        
        dims = [k for k, v in DIMENSIONES.items() if st.checkbox(v, key=f"dim_{k}")]

        if st.button("🚀 Iniciar conversación"):
            if not company or not dims:
                st.error("Completá los campos obligatorios.")
            else:
                import google.generativeai as genai
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel("gemini-2.0-flash", system_instruction=build_system_prompt(engine, dims))
                chat = model.start_chat(history=[])
                
                greeting = llamar_gemini(chat, f"Hola, la empresa es {company}. Empecemos.", "Error al conectar.", es_chat=True)
                if greeting:
                    st.session_state.company = company
                    st.session_state.gemini_chat = chat
                    st.session_state.chat_history = [{"role": "assistant", "content": greeting}]
                    st.session_state.selected_dims = dims
                    st.session_state.phase = "chat"
                    st.rerun()

    # FASE 2: CHAT
    elif st.session_state.phase == "chat":
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if prompt := st.chat_input("Escribí tu respuesta..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            respuesta = llamar_gemini(st.session_state.gemini_chat, prompt, "Error en chat.", es_chat=True)
            if respuesta:
                st.session_state.chat_history.append({"role": "assistant", "content": respuesta})
                st.rerun()

        if st.button("📋 Generar diagnóstico"):
            # Aquí va tu lógica de reporte usando llamar_gemini con es_chat=False
            pass

# --- MAIN ---
def main():
    st.set_page_config(page_title="Klar Analytics", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)
    # ... resto de tu lógica de menú ...
    page_diagnosis()

if __name__ == "__main__":
    main()
