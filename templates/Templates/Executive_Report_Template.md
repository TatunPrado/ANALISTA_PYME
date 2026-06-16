# INFORME EJECUTIVO DE DIAGNÓSTICO EMPRESARIAL

---

## PORTADA

| Campo | Valor |
|-------|-------|
| **Nombre de Empresa** | `{{EMPRESA}}` |
| **Industria** | `{{INDUSTRIA}}` |
| **Fecha del Diagnóstico** | `{{FECHA}}` |
| **Consultor IA** | `{{CONSULTOR_IA}}` |
| **Versión del Informe** | `{{VERSION}}` |

---

## RESUMEN EJECUTIVO

### Estado General

`{{ESTADO_GENERAL}}` → [✅ Saludable | ⚠️ Atención | 🔴 Crítico]

### Principales Hallazgos

1. `{{HALLAZGO_1}}`
2. `{{HALLAZGO_2}}`
3. `{{HALLAZGO_3}}`

### Riesgos Críticos

- `{{RIESGO_CRITICO_1}}`
- `{{RIESGO_CRITICO_2}}`

### Oportunidades Clave

- `{{OPORTUNIDAD_CLAVE_1}}`
- `{{OPORTUNIDAD_CLAVE_2}}`

> **Extensión máxima: 1 página.** Este resumen debe poder leerse en 60 segundos y habilitar la toma de decisiones inmediata.

---

## SCORE GENERAL

### Tabla de Puntuación

| Dimensión | Puntaje (0-100) | Semáforo | Interpretación |
|-----------|----------------|----------|----------------|
| Finanzas | `{{SCORE_FINANZAS}}` | `{{SEMAFORO_FINANZAS}}` | `{{INTERP_FINANZAS}}` |
| Operaciones | `{{SCORE_OPERACIONES}}` | `{{SEMAFORO_OPERACIONES}}` | `{{INTERP_OPERACIONES}}` |
| Organización | `{{SCORE_ORGANIZACION}}` | `{{SEMAFORO_ORGANIZACION}}` | `{{INTERP_ORGANIZACION}}` |
| Riesgos | `{{SCORE_RIESGOS}}` | `{{SEMAFORO_RIESGOS}}` | `{{INTERP_RIESGOS}}` |
| Modelo de Negocio | `{{SCORE_MODELO_NEGOCIO}}` | `{{SEMAFORO_MODELO_NEGOCIO}}` | `{{INTERP_MODELO_NEGOCIO}}` |
| Estrategia | `{{SCORE_ESTRATEGIA}}` | `{{SEMAFORO_ESTRATEGIA}}` | `{{INTERP_ESTRATEGIA}}` |

### Leyenda de Semáforo

| Color | Rango | Significado |
|-------|-------|-------------|
| 🟢 Verde | 70 - 100 | Saludable |
| 🟡 Amarillo | 40 - 69 | Requiere atención |
| 🔴 Rojo | 0 - 39 | Crítico |

### Gráfico Radar

```
                    Finanzas
                      ▲
                      │
                    100│
                      │
                  80  │
        Estrategia    │    Operaciones
           ────●──────┼──────●────
                      │
                  60  │
                      │
        Modelo de     │    Organización
        Negocio       │
           ────●──────┼──────●────
                      │
                  40  │
                      │
                      │    Riesgos
                      │
                      └──────────────►
```

> **Nota:** Incluir gráfico radar generado visualmente con los puntajes de cada dimensión. El área sombreada representa el estado general de la empresa.

---

## ESTADO POR ÁREA

### Área: `{{NOMBRE_AREA}}`

#### Diagnóstico

`{{DIAGNOSTICO_AREA}}`

#### Evidencia

- `{{EVIDENCIA_1}}`
- `{{EVIDENCIA_2}}`
- `{{EVIDENCIA_3}}`

#### Hallazgos

- `{{HALLAZGO_AREA_1}}`
- `{{HALLAZGO_AREA_2}}`

#### Riesgos Identificados

- `{{RIESGO_AREA_1}}`
- `{{RIESGO_AREA_2}}`

#### Recomendaciones

1. `{{RECOMENDACION_AREA_1}}`
2. `{{RECOMENDACION_AREA_2}}`

#### Prioridad

`{{PRIORIDAD_AREA}}` → [🔴 Alta | 🟡 Media | 🟢 Baja]

#### Gráfico Recomendado

`{{TIPO_GRAFICO}}` → [Barras | Líneas | Circular | Dispersión | Gantt]

> **Instrucción:** Repetir esta estructura para cada una de las 6 dimensiones evaluadas.

---

## PRINCIPALES HALLAZGOS

| # | Hallazgo | Impacto | Urgencia | Área |
|---|----------|---------|----------|------|
| 1 | `{{HALLAZGO_1}}` | `{{IMPACTO_1}}` | `{{URGENCIA_1}}` | `{{AREA_1}}` |
| 2 | `{{HALLAZGO_2}}` | `{{IMPACTO_2}}` | `{{URGENCIA_2}}` | `{{AREA_2}}` |
| 3 | `{{HALLAZGO_3}}` | `{{IMPACTO_3}}` | `{{URGENCIA_3}}` | `{{AREA_3}}` |
| 4 | `{{HALLAZGO_4}}` | `{{IMPACTO_4}}` | `{{URGENCIA_4}}` | `{{AREA_4}}` |
| 5 | `{{HALLAZGO_5}}` | `{{IMPACTO_5}}` | `{{URGENCIA_5}}` | `{{AREA_5}}` |

**Criterios de ordenamiento:** Urgencia (Alta → Media → Baja) y luego Impacto (Crítico → Significativo → Menor).

---

## CAUSAS RAÍZ

### Árbol de Causas

```
                    ┌─────────────────────────────┐
                    │     PROBLEMA PRINCIPAL       │
                    │   {{PROBLEMA_PRINCIPAL}}     │
                    └─────────────┬───────────────┘
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
    ┌───────┴───────┐     ┌───────┴───────┐     ┌───────┴───────┐
    │  Causa Raíz 1  │     │  Causa Raíz 2  │     │  Causa Raíz 3  │
    │ {{CAUSA_R1_1}} │     │ {{CAUSA_R1_2}} │     │ {{CAUSA_R1_3}} │
    └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
            │                     │                     │
    ┌───────┴───────┐     ┌───────┴───────┐     ┌───────┴───────┐
    │  Subcausa 1.1 │     │  Subcausa 2.1 │     │  Subcausa 3.1 │
    │ {{SUB_R1_1}}  │     │ {{SUB_R1_2}}  │     │ {{SUB_R1_3}}  │
    └───────────────┘     └───────────────┘     └───────────────┘
```

### Relación entre Problemas

| Problema | Causa Raíz Asociada | Dependencias | Áreas Afectadas |
|----------|--------------------|--------------|-----------------|
| `{{PROBLEMA_1}}` | `{{CAUSA_ASOC_1}}` | `{{DEP_1}}` | `{{AREAS_AFECT_1}}` |
| `{{PROBLEMA_2}}` | `{{CAUSA_ASOC_2}}` | `{{DEP_2}}` | `{{AREAS_AFECT_2}}` |

> **Nota:** Incluir diagrama de relaciones causales con flechas de dirección. Usar colores para identificar cadenas de causalidad críticas.

---

## MATRIZ IMPACTO VS ESFUERZO

```
                      IMPACTO
                        ▲
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      │   PROYECTOS     │   QUICK WINS    │
      │   ESTRATÉGICOS  │                 │
      │                 │                 │
      │  ┌───────────┐  │  ┌───────────┐  │
      │  │ {{PE_1}}  │  │  │ {{QW_1}}  │  │
      │  │ {{PE_2}}  │  │  │ {{QW_2}}  │  │
      │  └───────────┘  │  └───────────┘  │
      │                 │                 │
Alto──┼─────────────────┼─────────────────┼──►
      │                 │                 │
      │  NO PRIORIZAR   │  MEJORAS        │
      │                 │  INCREMENTALES  │
      │  ┌───────────┐  │  ┌───────────┐  │
      │  │ {{NP_1}}  │  │  │ {{MI_1}}  │  │
      │  │ {{NP_2}}  │  │  │ {{MI_2}}  │  │
      │  └───────────┘  │  └───────────┘  │
      │                 │                 │
Bajo──┼─────────────────┼─────────────────┼──►
      │                 │                 │
      └─────────────────┼─────────────────┘
                        │
                   Bajo           Alto
                              ESFUERZO
```

### Clasificación de Iniciativas

| Cuadrante | Iniciativas | Acción Recomendada |
|-----------|-------------|-------------------|
| 🟢 **Quick Wins** | `{{LISTA_QUICK_WINS}}` | Ejecutar inmediatamente |
| 🔵 **Proyectos Estratégicos** | `{{LISTA_PROY_ESTRATEGICOS}}` | Planificar y ejecutar |
| 🟡 **Mejoras Incrementales** | `{{LISTA_MEJORAS_INCREMENTALES}}` | Incorporar en operación continua |
| ⚪ **No Priorizar** | `{{LISTA_NO_PRIORIZAR}}` | Descartar o aplazar |

---

## RIESGOS

### Tabla de Riesgos

| ID | Riesgo | Probabilidad | Impacto | Nivel | Mitigación |
|----|--------|-------------|---------|-------|------------|
| R1 | `{{RIESGO_1}}` | `{{PROB_1}}` | `{{IMPACTO_RIESGO_1}}` | `{{NIVEL_1}}` | `{{MITIGACION_1}}` |
| R2 | `{{RIESGO_2}}` | `{{PROB_2}}` | `{{IMPACTO_RIESGO_2}}` | `{{NIVEL_2}}` | `{{MITIGACION_2}}` |
| R3 | `{{RIESGO_3}}` | `{{PROB_3}}` | `{{IMPACTO_RIESGO_3}}` | `{{NIVEL_3}}` | `{{MITIGACION_3}}` |
| R4 | `{{RIESGO_4}}` | `{{PROB_4}}` | `{{IMPACTO_RIESGO_4}}` | `{{NIVEL_4}}` | `{{MITIGACION_4}}` |
| R5 | `{{RIESGO_5}}` | `{{PROB_5}}` | `{{IMPACTO_RIESGO_5}}` | `{{NIVEL_5}}` | `{{MITIGACION_5}}` |

### Leyenda de Nivel de Riesgo

| Nivel | Rango Probabilidad x Impacto | Color |
|-------|------------------------------|-------|
| Crítico | 16 - 25 | 🔴 |
| Alto | 10 - 15 | 🟠 |
| Medio | 5 - 9 | 🟡 |
| Bajo | 1 - 4 | 🟢 |

### Mapa de Calor (Heatmap) Recomendado

```
Probabilidad
    ▲
Alta │    ┌─────┬─────┬─────┬─────┐
     │    │ 🟡  │ 🟠  │ 🔴  │ 🔴  │
     │    └─────┴─────┴─────┴─────┘
     │    ┌─────┬─────┬─────┬─────┐
Media │    │ 🟢  │ 🟡  │ 🟠  │ 🔴  │
     │    └─────┴─────┴─────┴─────┘
     │    ┌─────┬─────┬─────┬─────┐
Baja  │    │ 🟢  │ 🟢  │ 🟡  │ 🟠  │
     │    └─────┴─────┴─────┴─────┘
     │
     └──────────────────────────────►
        Bajo   Medio   Alto  Crítico
                       Impacto
```

---

## OPORTUNIDADES

| ID | Oportunidad | Beneficio Esperado | Complejidad | Prioridad |
|----|------------|-------------------|-------------|-----------|
| O1 | `{{OPORTUNIDAD_1}}` | `{{BENEFICIO_1}}` | `{{COMPLEJIDAD_1}}` | `{{PRIORIDAD_OP_1}}` |
| O2 | `{{OPORTUNIDAD_2}}` | `{{BENEFICIO_2}}` | `{{COMPLEJIDAD_2}}` | `{{PRIORIDAD_OP_2}}` |
| O3 | `{{OPORTUNIDAD_3}}` | `{{BENEFICIO_3}}` | `{{COMPLEJIDAD_3}}` | `{{PRIORIDAD_OP_3}}` |
| O4 | `{{OPORTUNIDAD_4}}` | `{{BENEFICIO_4}}` | `{{COMPLEJIDAD_4}}` | `{{PRIORIDAD_OP_4}}` |
| O5 | `{{OPORTUNIDAD_5}}` | `{{BENEFICIO_5}}` | `{{COMPLEJIDAD_5}}` | `{{PRIORIDAD_OP_5}}` |

---

## PLAN DE ACCIÓN 90 DÍAS

| # | Acción | Responsable | Impacto Esperado | Prioridad | Semana |
|---|--------|-------------|-----------------|-----------|--------|
| 1 | `{{ACCION_1}}` | `{{RESPONSABLE_1}}` | `{{IMPACTO_ESPERADO_1}}` | `{{PRIORIDAD_ACCION_1}}` | `{{SEMANA_1}}` |
| 2 | `{{ACCION_2}}` | `{{RESPONSABLE_2}}` | `{{IMPACTO_ESPERADO_2}}` | `{{PRIORIDAD_ACCION_2}}` | `{{SEMANA_2}}` |
| 3 | `{{ACCION_3}}` | `{{RESPONSABLE_3}}` | `{{IMPACTO_ESPERADO_3}}` | `{{PRIORIDAD_ACCION_3}}` | `{{SEMANA_3}}` |
| 4 | `{{ACCION_4}}` | `{{RESPONSABLE_4}}` | `{{IMPACTO_ESPERADO_4}}` | `{{PRIORIDAD_ACCION_4}}` | `{{SEMANA_4}}` |
| 5 | `{{ACCION_5}}` | `{{RESPONSABLE_5}}` | `{{IMPACTO_ESPERADO_5}}` | `{{PRIORIDAD_ACCION_5}}` | `{{SEMANA_5}}` |
| 6 | `{{ACCION_6}}` | `{{RESPONSABLE_6}}` | `{{IMPACTO_ESPERADO_6}}` | `{{PRIORIDAD_ACCION_6}}` | `{{SEMANA_6}}` |
| 7 | `{{ACCION_7}}` | `{{RESPONSABLE_7}}` | `{{IMPACTO_ESPERADO_7}}` | `{{PRIORIDAD_ACCION_7}}` | `{{SEMANA_7}}` |

---

## ROADMAP ESTRATÉGICO

```
FASE 1                    FASE 2                   FASE 3                   FASE 4
0 - 30 DÍAS               30 - 90 DÍAS             3 - 12 MESES             1 - 3 AÑOS
────────────────────      ────────────────────     ────────────────────     ────────────────────
                                                                            
┌────────────────────┐    ┌────────────────────┐   ┌────────────────────┐   ┌────────────────────┐
│   QUICK WINS       │    │ PROYECTOS          │   │ TRANSFORMACIÓN     │   │ MADUREZ            │
│                    │    │ TÁCTICOS           │   │ ESTRUCTURAL        │   │ SOSTENIBLE         │
│ ┌────────────────┐ │    │ ┌────────────────┐ │   │ ┌────────────────┐ │   │ ┌────────────────┐ │
│ │{{QW_S1}}       │ │    │ │{{PT_S2}}       │ │   │ │{{TE_S3}}       │ │   │ │{{MS_S4}}       │ │
│ │{{QW_S2}}       │ │    │ │{{PT_S2}}       │ │   │ │{{TE_S3}}       │ │   │ │{{MS_S4}}       │ │
│ └────────────────┘ │    │ └────────────────┘ │   │ └────────────────┘ │   │ └────────────────┘ │
└────────────────────┘    └────────────────────┘   └────────────────────┘   └────────────────────┘
                                                                            
◄──────────────►          ◄──────────────►         ◄──────────────►         ◄──────────────►
  Ejecución rápida          Implementación           Transformación           Consolidación
  Resultados inmediatos     Resultados tácticos      Resultados               Resultados
                            visibles                 estratégicos             de largo plazo
```

### Hitos Clave por Fase

| Fase | Hito | Fecha Estimada | Dependencia |
|------|------|---------------|-------------|
| 0-30 días | `{{HITO_F1_1}}` | `{{FECHA_F1_1}}` | `{{DEP_F1_1}}` |
| 0-30 días | `{{HITO_F1_2}}` | `{{FECHA_F1_2}}` | `{{DEP_F1_2}}` |
| 30-90 días | `{{HITO_F2_1}}` | `{{FECHA_F2_1}}` | `{{DEP_F2_1}}` |
| 30-90 días | `{{HITO_F2_2}}` | `{{FECHA_F2_2}}` | `{{DEP_F2_2}}` |
| 3-12 meses | `{{HITO_F3_1}}` | `{{FECHA_F3_1}}` | `{{DEP_F3_1}}` |
| 1-3 años | `{{HITO_F4_1}}` | `{{FECHA_F4_1}}` | `{{DEP_F4_1}}` |

---

## KPIs RECOMENDADOS

| Dimensión | Indicador | Objetivo | Línea Base | Frecuencia | Meta 90 Días |
|-----------|-----------|----------|------------|------------|--------------|
| Finanzas | `{{KPI_FIN_1}}` | `{{OBJ_FIN_1}}` | `{{BASE_FIN_1}}` | `{{FREC_FIN_1}}` | `{{META_FIN_1}}` |
| Finanzas | `{{KPI_FIN_2}}` | `{{OBJ_FIN_2}}` | `{{BASE_FIN_2}}` | `{{FREC_FIN_2}}` | `{{META_FIN_2}}` |
| Operaciones | `{{KPI_OP_1}}` | `{{OBJ_OP_1}}` | `{{BASE_OP_1}}` | `{{FREC_OP_1}}` | `{{META_OP_1}}` |
| Organización | `{{KPI_ORG_1}}` | `{{OBJ_ORG_1}}` | `{{BASE_ORG_1}}` | `{{FREC_ORG_1}}` | `{{META_ORG_1}}` |
| Riesgos | `{{KPI_RIES_1}}` | `{{OBJ_RIES_1}}` | `{{BASE_RIES_1}}` | `{{FREC_RIES_1}}` | `{{META_RIES_1}}` |
| Modelo de Negocio | `{{KPI_MN_1}}` | `{{OBJ_MN_1}}` | `{{BASE_MN_1}}` | `{{FREC_MN_1}}` | `{{META_MN_1}}` |
| Estrategia | `{{KPI_EST_1}}` | `{{OBJ_EST_1}}` | `{{BASE_EST_1}}` | `{{FREC_EST_1}}` | `{{META_EST_1}}` |

---

## PRÓXIMOS PASOS

### Recomendaciones para la Dirección

1. **`{{RECOMENDACION_DIR_1}}`**
   - `{{DETALLE_REC_1}}`

2. **`{{RECOMENDACION_DIR_2}}`**
   - `{{DETALLE_REC_2}}`

3. **`{{RECOMENDACION_DIR_3}}`**
   - `{{DETALLE_REC_3}}`

4. **`{{RECOMENDACION_DIR_4}}`**
   - `{{DETALLE_REC_4}}`

5. **`{{RECOMENDACION_DIR_5}}`**
   - `{{DETALLE_REC_5}}`

### Decisiones Requeridas

| Decisión | Requerido por | Impacto si se retrasa |
|----------|--------------|----------------------|
| `{{DECISION_1}}` | `{{FECHA_DECISION_1}}` | `{{IMPACTO_RETRASO_1}}` |
| `{{DECISION_2}}` | `{{FECHA_DECISION_2}}` | `{{IMPACTO_RETRASO_2}}` |

---

## REGLAS DE FORMATO

### Cuándo usar cada elemento visual

| Elemento | Cuándo usarlo |
|----------|---------------|
| **Tablas** | Para comparar múltiples elementos con atributos comunes (hallazgos, riesgos, KPIs, planes de acción). Toda tabla debe tener un encabezado claro y ordenamiento definido. |
| **Gráficos** | Para mostrar tendencias, distribuciones, proporciones o comparaciones visuales. Preferir radar para scores generales, barras para comparaciones, heatmap para riesgos. |
| **Texto narrativo** | Solo para diagnósticos contextuales, descripción de hallazgos cualitativos y recomendaciones detalladas. Máximo 3 párrafos por sección. |
| **Diagramas** | Para relaciones causales (árbol de causas), flujos de proceso, dependencias entre iniciativas y roadmaps. Preferir diagramas de árbol y matrices 2x2. |
| **Semáforos** | Para estado general de cada dimensión. Usar exclusivamente 🟢 🟡 🔴. No usar escalas de colores no estandarizadas. |
| **Matrices** | Para clasificar iniciativas por dos variables (impacto vs esfuerzo, probabilidad vs impacto). Formato 2x2 o 4x4. |

### Reglas generales de formato

- Toda sección debe incluir al menos un elemento visual (tabla, gráfico o diagrama).
- No usar texto continuo de más de 10 líneas sin un elemento visual intermedio.
- Los scores numéricos deben estar siempre acompañados de semáforo.
- Las recomendaciones deben tener prioridad asociada explícita.
- Fechas en formato ISO 8601: `YYYY-MM-DD`.
- Moneda expresada en unidad local con símbolo estándar.
- Usar nomenclatura de variables `{{LLAVES_DOBLES}}` para campos dinámicos.

---

## REGLAS DE CALIDAD

### Principios fundamentales

1. **Basarse en evidencia:** Toda afirmación debe tener al menos una evidencia asociada y trazable citada en el informe. No incluir opiniones no respaldadas.

2. **Visualizaciones obligatorias:** Cada sección debe contener al menos una tabla o gráfico. No entregar secciones con únicamente texto narrativo.

3. **Priorización explícita:** Toda recomendación, hallazgo y riesgo debe tener un nivel de prioridad asignado (Alta / Media / Baja).

4. **Impacto esperado cuantificado:** Cada acción recomendada debe incluir el impacto esperado medible (%, $, tiempo, reducción de riesgo).

5. **Facilitar decisiones:** El informe debe terminar con decisiones concretas que la dirección debe tomar, con fechas límite y consecuencias del retraso.

6. **Extensión controlada:** Máximo 15 páginas (excluyendo portada y anexos). Cada área diagnóstica máxima 1 página.

7. **Lenguaje ejecutivo:** Evitar jerga técnica no explicada. Usar verbos de acción: implementar, optimizar, reducir, aumentar, transformar.

8. **Consistencia visual:** Usar la misma paleta de colores, tipografía y estilo de tablas en todo el documento.

> ⚠️ **Advertencia:** Nunca entregar un informe compuesto únicamente de texto narrativo. Todo informe debe tener al menos un 40% de su contenido en formato visual (tablas, gráficos, diagramas, matrices).

---

*Plantilla corporativa propiedad de la consultora. Versión {{VERSION}}.*
*Generado por: {{CONSULTOR_IA}}*
*Cliente: {{EMPRESA}}*
