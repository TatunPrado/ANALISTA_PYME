def page_home():
        st.session_state["page"] = "diagnosis"
        st.rerun()

def reset_diagnosis():
    keys = ["chat_history", "diagnosis_done", "report"]
    for k in keys:
        st.session_state.pop(k, None)

def page_diagnosis():
    engine = load_engine()
    api_key = st.sidebar.text_input("🔑 Gemini API Key", type="password",
@@ -216,73 +211,70 @@ def page_diagnosis():
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

                    system_prompt = build_system_prompt(engine, dims)
                    st.session_state.system_prompt = system_prompt
    phase = st.session_state.phase

                    st.session_state.setup_done = True
                    st.session_state.chat_history = []
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
@@ -298,52 +290,56 @@ def page_diagnosis():
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
