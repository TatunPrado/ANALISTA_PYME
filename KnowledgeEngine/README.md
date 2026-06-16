# Knowledge Engine — Klar Analytics

> Motor de carga dinámica de conocimiento
> Versión: 1.0 | Fecha: 2026-06-15

---

## 1. Propósito

Eliminar prompts hardcodeados. El motor escanea el filesystem, parsea los archivos Markdown de Agents/, Skills/, Knowledge/, Playbooks/ y Operations/, y construye dinámicamente el contexto necesario para que los agentes de IA ejecuten diagnósticos sin instrucciones fijas en el código.

## 2. Arquitectura

```
KnowledgeEngine/
├── __init__.py          # Inicialización, clase principal KnowledgeEngine
├── core.py              # Escáner, indexador, orquestador principal
├── parsers.py           # Parsers especializados por tipo de documento
├── prompt_builder.py    # Ensamblador dinámico de prompts
├── knowledge_loader.py  # Cargadores de filesystem
├── config.py            # Configuración, rutas, constantes
└── README.md            # Este archivo
```

## 3. Flujo de Operación

```
1. KnowledgeEngine.init()
   │
   ├── Escanea Agents/ → detecta 11 agentes
   ├── Escanea Skills/ → detecta 8 skills
   ├── Escanea Knowledge/ → detecta 20+ frameworks y patrones
   ├── Escanea Playbooks/ → detecta 3 SOPs
   └── Escanea Operations/ → detecta 11 procesos
   │
2. KnowledgeEngine.index()
   │
   ├── Parsear cada archivo según su tipo
   ├── Extraer metadatos, secciones, campos estructurados
   └── Construir índice de búsqueda (tags, palabras clave)
   │
3. KnowledgeEngine.build_context(query, dimensions)
   │
   ├── Seleccionar agentes relevantes
   ├── Seleccionar skills relevantes
   ├── Seleccionar frameworks relevantes
   ├── Seleccionar patrones relevantes
   └── Seleccionar playbooks relevantes
   │
4. KnowledgeEngine.assemble_prompt(context)
   │
   ├── Template: System (rol del agente)
   ├── Template: Context (knowledge base)
   ├── Template: Instructions (pasos a seguir)
   ├── Template: Data (inputs del cliente)
   └── Output: prompt listo para LLM
```

## 4. Uso

```python
from KnowledgeEngine import KnowledgeEngine

engine = KnowledgeEngine(base_path="C:/ruta/al/proyecto")
engine.init()        # escanea todo el repositorio
engine.index()       # parsea e indexa

# Construir contexto para un diagnóstico financiero
context = engine.build_context(
    client_brief=brief_data,
    dimensions=["finanzas", "estrategia"],
    diagnosis_type="integral"
)

# Ensamblar prompt para un agente específico
prompt = engine.assemble_prompt(
    agent="Financial_Analyst",
    client_data=client_data,
    context=context
)

# Enviar a LLM
response = llm.chat(prompt.system + prompt.user)
```

## 5. Tipos de Documentos Soportados

| Tipo | Directorio | Parser | Estructura |
|---|---|---|---|
| Agent | Agents/ | parse_agent() | H1 título, H2 secciones, bullets |
| Skill | Skills/ | parse_skill() | H1 título, Objetivo, Procedimiento, Salida |
| Framework | Knowledge/*/Framework_*.md | parse_framework() | H1 título, H2 variables, H3 sub-vars |
| Pattern | Knowledge/CORE/*_Patterns.md | parse_pattern() | H1 título, H3 pattern-ID con bold-key: value |
| Playbook | Playbooks/*.md | parse_playbook() | H1 título, blockquote meta, H2 numerados |
| Process | Operations/*.md | parse_process() | H1 título, H2 numerados, tablas |

## 6. Integración con el Sistema Actual

- Agents/ usa los nombres de skills y frameworks como referencias → el motor resuelve las dependencias automáticamente
- Skills/ linkea a frameworks vía rutas relativas → el motor sigue las referencias y carga los frameworks asociados
- Knowledge/ proporciona los fundamentos → el motor selecciona los patrones y frameworks relevantes por dimensión
- Playbooks/ guían la ejecución → el motor extrae los pasos relevantes según el tipo de diagnóstico
- Operations/ define KPIs y procesos → el motor integra las métricas en el contexto del agente
