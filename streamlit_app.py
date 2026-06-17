"""
Klar Analytics — Diagnóstico Empresarial Interactivo
App Streamlit con chat vía Google Gemini + KnowledgeEngine.
"""
import sys, os, time
from pathlib import Path
import streamlit as st
from PIL import Image, ImageDraw
from google.api_core import exceptions

# 1. CONSTANTES


# 2. CONFIGURACIÓN
ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT))
from KnowledgeEngine import KnowledgeEngine
from APP.Objectives.ObjectiveMapper import ObjectiveMapper

BLUE_500 = "#3182CE"
CSS = f"""<style>.stApp {{ background-color: #F8F9FA; }}</style>"""

# 3. FUNCIONES AUXILIARES
@st.cache_resource
def load_engine():
    eng = KnowledgeEngine(base_path=str(ROOT))
    eng.init()
    return eng
@st.cache_resource
def load_objectives():
    return ObjectiveMapper()

def llamar_gemini(objeto_gemini, prompt, es_chat=False):
    try:
        with st.spinner("Consultando a la IA..."):
            if es_chat:
                return objeto_gemini.send_message(prompt).text
            return objeto_gemini.generate_content(prompt).text
    except exceptions.ResourceExhausted:
        st.error("⚠️ Cuota de API agotada (429). Por favor, intenta de nuevo en unos segundos.")
        return None
    except Exception as e:
        st.error(f"Error técnico: {e}")
        return None

# 4. PÁGINA DE DIAGNÓSTICO
def page_diagnosis():
    engine = load_engine()
    objective_mapper = load_objectives()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password")
    
    if not api_key:
        st.info("Configurá tu API Key en la barra lateral.")
        return

    # Inicialización de estado
    if "phase" not in st.session_state: st.session_state.phase = "setup"
    if "chat_history" not in st.session_state: st.session_state.chat_history = []

   # FASE 1: SETUP

    # FASE 1: SETUP
    if st.session_state.phase == "setup":

        company = st.text_input("Nombre de la empresa")

        available_objectives = objective_mapper.list_objectives()

        selected_objective = st.selectbox(
            "¿Qué desea lograr?",
            available_objectives
        )

        if st.button("🚀 Iniciar conversación"):

            if not company:
                st.error("Completá los campos obligatorios.")

            else:

                import google.generativeai as genai

                genai.configure(api_key=api_key)

                model = genai.GenerativeModel(
                    "gemini-3.1-flash-lite"
                )

                chat = model.start_chat(history=[])

                dimensions = objective_mapper.get_dimensions(
                    selected_objective
                )

                agents = objective_mapper.get_agents(
                    selected_objective
                )

                initial_prompt = f"""
Actuá como consultor empresarial senior.

Empresa:
{company}

Objetivo del cliente:
{selected_objective}

Dimensiones a analizar:
{', '.join(dimensions)}

Agentes especializados:
{', '.join(agents)}

Iniciá una entrevista diagnóstica.

Realizá una sola pregunta abierta.

No expliques el proceso.

No brindes recomendaciones todavía.

Buscá comprender la situación actual de la empresa.
"""

                greeting = llamar_gemini(
                    chat,
                    initial_prompt,
                    es_chat=True
                )

                if greeting:

                    st.session_state.company = company

                    st.session_state.objective = selected_objective

                    st.session_state.dimensions = dimensions

                    st.session_state.agents = agents

                    st.session_state.gemini_chat = chat

                    st.session_state.chat_history = [
                        {
                            "role": "assistant",
                            "content": greeting
                        }
                    ]

                    st.session_state.phase = "chat"

                    st.rerun()



    # FASE 2: CHAT
    elif st.session_state.phase == "chat":
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        if prompt := st.chat_input("Escribí tu respuesta..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            res = llamar_gemini(st.session_state.gemini_chat, prompt, es_chat=True)
            if res:
                st.session_state.chat_history.append({"role": "assistant", "content": res})
                st.rerun()

# 5. MAIN
def main():
    st.set_page_config(page_title="Klar Analytics", layout="wide")
    st.markdown(CSS, unsafe_allow_html=True)
    page_diagnosis()

if __name__ == "__main__":
    main()
