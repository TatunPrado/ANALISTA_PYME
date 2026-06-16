"""
Klar Analytics — Diagnóstico Empresarial Interactivo
App Streamlit con chat vía Google Gemini + KnowledgeEngine.
"""
import sys, os, json, time
from pathlib import Path
import streamlit as st
from PIL import Image, ImageDraw

# 1. CONSTANTES
DIMENSIONES = {
    "finanzas": "Finanzas", "estrategia": "Estrategia", "operaciones": "Operaciones",
    "talento": "Talento y Organización", "riesgos": "Riesgos", "modelo_negocio": "Modelo de Negocio",
    "cliente": "Cliente y Mercado", "marketing": "Marketing", "tecnologia": "Tecnología",
}

# 2. CONFIGURACIÓN INICIAL
ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))
from KnowledgeEngine import KnowledgeEngine

BLUE_500 = "#3182CE"
GRAY_50  = "#F8F9FA"

CSS = f"""<style>.stApp {{ background-color: {GRAY_50}; }}</style>"""

# 3. FUNCIONES AUXILIARES
@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng

def llamar_gemini(objeto_gemini, prompt, error_msg="Error desconocido", es_chat=False):
    try:
        with st.spinner("Consultando a la IA..."):
            if es_chat:
                return objeto_gemini.send_message(prompt).text
            else:
                return objeto_gemini.generate_content(prompt).text
    except Exception as e:
        st.error(f"❌ {error_msg}")
        st.exception(e)
        return None

# 4. PÁGINA DE DIAGNÓSTICO
def page_diagnosis():
    engine = load_engine()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password")
    if not api_key:
        st.info("Configurá tu API Key en la barra lateral.")
        return

    for key in ("chat_history", "phase", "report", "selected_dims"):
        if key not in st.session_state:
            st.session_state[key] = [] if key == "chat_history" else (None if key == "report" else "setup")

    if st.session_state.phase == "setup":
        company = st.text_input("Nombre de la empresa")
        dims = [k for k, v in DIMENSIONES.items() if st.checkbox(v)]
        if st.button("🚀 Iniciar"):
            import google.generativeai as genai
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-1.5-flash")
            chat = model.start_chat(history=[])
            greeting = llamar_gemini(chat, f"Hola, la empresa es {company}.", "Error.", es_chat=True)
            if greeting:
                st.session_state.company = company
                st.session_state.gemini_chat = chat
                st.session_state.chat_history = [{"role": "assistant", "content": greeting}]
                st.session_state.phase = "chat"
                st.rerun()

    elif st.session_state.phase == "chat":
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        if prompt := st.chat_input("Escribí tu respuesta..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            res = llamar_gemini(st.session_state.gemini_chat, prompt, "Error.", es_chat=True)
            if res:
                st.session_state.chat_history.append({"role": "assistant", "content": res})
                st.rerun()

# 5. MAIN
def main():
    st.markdown(CSS, unsafe_allow_html=True)
    page_diagnosis()

if __name__ == "__main__":
    main()
