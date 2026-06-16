# GUÍA DE SITIO WEB — Estructura y Contenido

## Arquitectura del Sitio

```
Home
├── Servicios
│   ├── Diagnóstico Integral
│   ├── Diagnóstico Financiero
│   ├── Diagnóstico Estratégico
│   └── Diagnóstico Operativo
├── Metodología
│   ├── Nuestro Proceso
│   └── Tecnología + IA
├── Casos de Uso
│   └── (por perfil de empresa)
├── FAQ
└── Contacto
    └── Solicitar Diagnóstico
```

### Barra de navegación (global)

| Elemento | Comportamiento |
|---|---|
| Logo | Izquierda, enlace a Home |
| Menú | Servicios, Metodología, Casos de Uso, FAQ |
| CTA principal | Derecha: "Solicitar diagnóstico" — botón primario (Azul 800) |
| CTA secundario | "Hablar con un asesor" — icono de WhatsApp, visible en mobile |
| Sticky | Sí, fondo blanco con sombra al hacer scroll |

---

## HOME

### Objetivo

Generar confianza y credibilidad en segundos. El visitante debe entender qué hace la consultora, para quién es y por qué es diferente. Captar leads calificados.

### Mensaje principal

> **Entendé tu negocio con claridad. Decidí con confianza.**

### Mensajes secundarios

- Diagnósticos empresariales con inteligencia artificial
- Resultados en 7 días, no en meses
- Sin conflicto de interés (no vendemos implementación)
- Metodologías de clase mundial

### Llamados a la acción

| CTA | Tipo | Color | Destino |
|---|---|---|---|
| "Solicitar mi diagnóstico" | Primario | Azul 800 | Formulario de contacto |
| "Ver casos de uso" | Secundario | Borde Azul 500 | /casos-de-uso |
| "Conocé la metodología" | Link | Texto | /metodologia |

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  HERO                                            │
│  ┌─────────────────────────────────────────┐    │
│  │                                         │    │
│  │  "Entendé tu negocio con claridad.      │    │
│  │   Decidí con confianza."                │    │
│  │                                         │    │
│  │  [Subtítulo: Diagnósticos empresa-      │    │
│  │   riales con IA · 7 días · Sin          │    │
│  │   conflicto de interés]                 │    │
│  │                                         │    │
│  │  [Solicitar mi diagnóstico] [Ver cómo]  │    │
│  │                                         │    │
│  │  ┌─ Logo ┐ ┌─ Logo ┐ ┌─ Logo ┐         │    │
│  │  │ confía│ │ confía│ │ confía│          │    │
│  │  └───────┘ └───────┘ └───────┘         │    │
│  │  "Empresas que ya confiaron en          │    │
│  │   [Nombre]"                             │    │
│  └─────────────────────────────────────────┘    │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  PROBLEMA / DOLOR                               │
│  ┌────────────────────┐ ┌────────────────────┐  │
│  │ "No sabés con      │ │ "No sabés con      │  │
│  │  certeza qué está  │ │  certeza qué está  │  │
│  │  limitando tu      │ │  limitando tu      │  │
│  │  crecimiento"      │ │  crecimiento"      │  │
│  └────────────────────┘ └────────────────────┘  │
│  (3–4 tarjetas de dolor + flecha hacia solución)│
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  SOLUCIÓN                                       │
│  ┌──────────────────────────────────────────┐   │
│  │  "Por eso creamos [Nombre]"              │   │
│  │  Explicación clara de qué ofrecen        │   │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │   │
│  │  │Rápi-│ │Rigo-│ │Obje-│ │Ace-│       │   │
│  │  │do   │ │roso │ │tivo │ │sible│       │   │
│  │  └─────┘ └─────┘ └─────┘ └─────┘       │   │
│  │  [Solicitar mi diagnóstico]              │   │
│  └──────────────────────────────────────────┘   │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  CÓMO FUNCIONA (3 pasos)                        │
│  ┌──────┐    ┌──────┐    ┌──────┐              │
│  │ 1.   │ →  │ 2.   │ →  │ 3.   │              │
│  │ Carga│    │Anali-│    │ Reci-│              │
│  │ datos│    │zamos │    │ bí tu│              │
│  │      │    │con IA│    │ diag.│              │
│  └──────┘    └──────┘    └──────┘              │
│  [Solicitar mi diagnóstico]                     │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  TESTIMONIO / CASO DE ÉXITO DESTACADO           │
│  ┌──────────────────────────────────────────┐   │
│  │  "Nos ayudaron a identificar un problema  │   │
│  │   que veníamos arrastrando hace 2 años.  │   │
│  │   En 7 días teníamos claridad."           │   │
│  │  — Nombre, Cargo, Empresa                 │   │
│  └──────────────────────────────────────────┘   │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  PREGUNTA FINAL + CTA                           │
│  "¿Hace cuánto que no mirás tu negocio          │
│   con claridad?"                                 │
│  [Solicitar mi diagnóstico gratis]              │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## SERVICIOS

### Objetivo

Explicar qué diagnósticos ofrecen, qué incluye cada uno y cuál es el más adecuado según la necesidad del visitante. Facilitar la decisión de compra.

### Mensaje principal

> **Elegí el diagnóstico que mejor se adapte al momento de tu empresa.**

### Llamados a la acción

| CTA | Destino |
|---|---|
| "Quiero este diagnóstico" | Formulario con producto preseleccionado |
| "No sé cuál necesito — ayudame a elegir" | Quiz breve (3 preguntas) → recomendación |
| "Ver ejemplo de informe" | Descargable PDF (lead magnet) |

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│  HERO DE SERVICIOS                               │
│  "Elegí el diagnóstico que mejor se adapte       │
│   al momento de tu empresa."                     │
│  [No sé cuál necesito — ayudame a elegir]        │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  TABLA COMPARATIVA DE SERVICIOS                  │
│                                                 │
│  ┌──────────┬──────────┬──────────┬──────────┐  │
│  │ DIAG.    │ DIAG.    │ DIAG.    │ DIAG.    │  │
│  │ INTEGRAL │ FINAN.   │ ESTRAT.  │ OPERAT.  │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │ ⭐ Rec.  │          │          │          │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │ Alcance  │ Alcance  │ Alcance  │ Alcance  │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │ 7 días   │ 5 días   │ 7 días   │ 5 días   │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │ $XXXX    │ $XXXX    │ $XXXX    │ $XXXX    │  │
│  ├──────────┼──────────┼──────────┼──────────┤  │
│  │ [Quiero] │ [Quiero] │ [Quiero] │ [Quiero] │  │
│  └──────────┴──────────┴──────────┴──────────┘  │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  DETALLE DE CADA SERVICIO (secciones plegables  │
│  o tarjetas expandibles)                        │
│                                                 │
│  ┌────────────────────────────────────────┐     │
│  │  Diagnóstico Integral                   │     │
│  │  ───────────────────────────────────── │     │
│  │  Incluye:                              │     │
│  │  ✅ Análisis financiero completo        │     │
│  │  ✅ Evaluación estratégica              │     │
│  │  ✅ Diagnóstico operativo               │     │
│  │  ✅ Análisis de riesgos                 │     │
│  │  ✅ Recomendaciones priorizadas         │     │
│  │  ✅ Informe ejecutivo + presentación    │     │
│  │                                         │     │
│  │  [Ver ejemplo de informe]               │     │
│  │  [Quiero este diagnóstico]              │     │
│  └────────────────────────────────────────┘     │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## METODOLOGÍA

### Objetivo

Construir confianza mostrando el proceso riguroso detrás de cada diagnóstico. Diferenciar de consultoras tradicionales y de plataformas automatizadas.

### Mensaje principal

> **No opinamos. Diagnosticamos.**

### Mensajes secundarios

- Metodologías de clase mundial (estrategia, finanzas, operaciones, riesgos)
- IA como acelerador, no como reemplazo del juicio humano
- Proceso estandarizado = consistencia garantizada
- Independencia: sin conflicto de interés

### Llamados a la acción

| CTA | Destino |
|---|---|
| "Solicitar diagnóstico" | Formulario |
| "Ver casos de uso" | /casos-de-uso |

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│  HERO METODOLOGÍA                                │
│  "No opinamos. Diagnosticamos."                  │
│  [Subtítulo que explica el proceso]              │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  LAS 4 ETAPAS DEL PROCESO                        │
│                                                 │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐│
│  │ 1.     │→ │ 2.     │→ │ 3.     │→ │ 4.     ││
│  │ CARGA  │  │ANÁLISIS│  │DIAGNÓS │  │ENTREGA ││
│  │ DE     │  │CON IA  │  │TICO    │  │+       ││
│  │ DATOS  │  │        │  │ESTRAT. │  │PLAN    ││
│  └────────┘  └────────┘  └────────┘  └────────┘│
│                                                 │
│  (cada etapa expandible con detalle)            │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  MARCOS METODOLÓGICOS                           │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │Estrategia│ │ Finanzas │ │Operacio.│         │
│  ├──────────┤ ├──────────┤ ├──────────┤        │
│  │ Marcos   │ │ Estándar │ │ Lean,    │        │
│  │...       │ │ ...      │ │ ...      │        │
│  └──────────┘ └──────────┘ └──────────┘        │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  IA + CRITERIO HUMANO                           │
│  Explicación de cómo se combinan ambos          │
│  (evitar tecnicismos, enfocar en beneficio)     │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  ¿POR QUÉ NO IMPLEMENTAMOS?                     │
│  Explicación del modelo de negocio como         │
│  garantía de objetividad                        │
│                                                 │
│  [Solicitar diagnóstico]                        │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## CASOS DE USO

### Objetivo

Mostrar aplicaciones concretas del servicio según el perfil del visitante. Responder "¿esto es para mí?".

### Mensaje principal

> **Sea cual sea el momento de tu empresa, tenemos un diagnóstico para vos.**

### Perfiles / situaciones

| Caso | Perfil | Mensaje clave |
|---|---|---|
| **Crecimiento** | Empresa que crece pero no sabe por qué | "Entendé qué está funcionando para potenciarlo" |
| **Estancamiento** | Empresa que no crece y no sabe por qué | "Identificá qué está frenando tu crecimiento" |
| **Riesgo** | Empresa con indicadores en rojo | "Detectá los riesgos antes de que sean crisis" |
| **Dueño saliente** | Dueño que quiere vender o delegar | "Conocé el valor real de tu empresa" |
| **Nuevo gerente** | Directivo que asume y necesita diagnóstico rápido | "En 7 días tenés un mapa completo de la situación" |

### Llamados a la acción

| CTA | Destino |
|---|---|
| "Quiero este diagnóstico" | Formulario con caso preseleccionado |
| "Soy este caso — contáctame" | Formulario |

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│  HERO CASOS DE USO                               │
│  "Sea cual sea el momento de tu empresa,         │
│   tenemos un diagnóstico para vos."              │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  TARJETAS POR CASO (grid 2×3)                   │
│                                                 │
│  ┌──────────────┐  ┌──────────────┐             │
│  │ 🚀           │  │ ⚠️           │             │
│  │ CRECIMIENTO  │  │ RIESGO       │             │
│  │ "Entendé qué  │  │ "Detectá los │             │
│  │  está funcio- │  │  riesgos an- │             │
│  │  nando para   │  │  tes de que  │             │
│  │  potenciarlo" │  │  sean crisis"│             │
│  │ [Ver más]     │  │ [Ver más]    │             │
│  └──────────────┘  └──────────────┘             │
│                                                 │
│  ┌──────────────┐  ┌──────────────┐             │
│  | 🔄           │  │ 💼           │             │
│  │ ESTANCADO    │  │ DUEÑO        │             │
│  │ ...          │  │ SALIENTE     │             │
│  └──────────────┘  └──────────────┘             │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  DETALLE DE CADA CASO (página individual)       │
│                                                 │
│  [Caso: Crecimiento]                            │
│  ─────────────────────                          │
│  Situación típica:                              │
│  "Tu empresa crece pero no sabés exactamente    │
│   qué lo está impulsando ni si es sostenible."  │
│                                                 │
│  Lo que vas a obtener:                          │
│  • Diagnóstico de las palancas de crecimiento   │
│  • Identificación de riesgos de sostenibilidad  │
│  • Recomendaciones para potenciar y consolidar  │
│                                                 │
│  [Quiero este diagnóstico]                      │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## PREGUNTAS FRECUENTES

### Objetivo

Resolver objeciones y dudas comunes que frenan la conversión. Reducir la fricción en la decisión de compra.

### Mensaje principal

> **Respondemos tus dudas. Sin vueltas, sin compromiso.**

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│  HERO FAQ                                        │
│  "Respondemos tus dudas."                        │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  ACORDEÓN DE PREGUNTAS (categorizado)           │
│                                                 │
│  ─── SOBRE EL DIAGNÓSTICO ───                   │
│                                                 │
│  ▶ ¿Qué información necesito para el            │
│    diagnóstico?                                  │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Cuánto tiempo toma?                         │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Es 100% online?                             │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Qué tipo de empresas pueden usar este       │
│    servicio?                                     │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ─── SOBRE LA METODOLOGÍA ───                   │
│                                                 │
│  ▶ ¿Qué calidad tiene el diagnóstico?           │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Quién analiza mis datos?                    │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Qué marcos metodológicos usan?              │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ─── SOBRE CONFIDENCIALIDAD ───                 │
│                                                 │
│  ▶ ¿Qué pasa con la información de mi empresa?  │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Comparten datos con terceros?               │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ─── SOBRE IMPLEMENTACIÓN ───                   │
│                                                 │
│  ▶ ¿Implementan las soluciones que              │
│    recomiendan?                                  │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ Si no implementan, ¿de qué sirve el          │
│    diagnóstico?                                  │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ─── SOBRE PRECIO ───                           │
│                                                 │
│  ▶ ¿Cuánto cuesta?                              │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Tienen financiación?                        │
│    │ Respuesta clara y breve.                   │
│                                                 │
│  ▶ ¿Tienen garantía?                            │
│    │ Respuesta clara y breve.                   │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  CTA FINAL                                       │
│  "¿Tenés otra pregunta? Respondemos en           │
│   menos de 24 horas."                            │
│  [Escribinos por WhatsApp] [Enviar mail]         │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Banco de respuestas (FAQ clave)

| Pregunta | Respuesta |
|---|---|
| **¿Qué información necesito?** | "Estado de resultados, balance general y, si está disponible, flujo de fondos de los últimos 12 meses. Si no tenés toda esta información, no te preocupes: trabajamos con lo que tengas y te guiamos en el proceso." |
| **¿Cuánto tiempo toma?** | "Entre 5 y 7 días hábiles desde que recibimos la información completa. Si el caso es complejo, te lo informamos antes de empezar." |
| **¿Es 100% online?** | "Sí. Todo el proceso es remoto: carga de datos, análisis, reunión de devolución y entrega del informe. Sin visitas presenciales." |
| **¿Qué calidad tiene?** | "Usamos metodologías probadas internacionalmente en estrategia, finanzas, operaciones y riesgos. Cada conclusión está respaldada por evidencia. La inteligencia artificial acelera el análisis, pero el criterio y la interpretación son humanas." |
| **¿Implementan las soluciones?** | "No. Esa es nuestra ventaja. Al no vender implementación, nuestras recomendaciones son 100% objetivas. No tenemos incentivo para inflar problemas ni recomendar servicios que nosotros mismos ejecutamos." |
| **¿Cuánto cuesta?** | "Depende del alcance del diagnóstico. El Integral comienza en $XX.XXX. Al solicitar el diagnóstico te confirmamos el precio exacto según la complejidad de tu caso." |

---

## CONTACTO

### Objetivo

Convertir visitantes en leads. Minimizar fricción. Recolectar información suficiente para calificar sin abrumar.

### Mensaje principal

> **Dale el primer paso. Sin compromiso, sin vueltas.**

### Llamados a la acción

| CTA | Tipo |
|---|---|
| "Solicitar diagnóstico" | Submit del formulario |
| "Hablar con un asesor" | WhatsApp (link directo) |
| "Enviar consulta" | Submit alternativo |

### Estructura recomendada

```
┌─────────────────────────────────────────────────┐
│  HERO CONTACTO                                   │
│  "Dale el primer paso."                          │
│  "Sin compromiso, sin vueltas."                  │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  FORMULARIO PRINCIPAL (2 columnas)               │
│                                                 │
│  ┌────────────────────┐ ┌────────────────────┐  │
│  │ Nombre completo     │ │ Teléfono / WhatsApp│  │
│  │ [input]             │ │ [input]            │  │
│  ├────────────────────┤ ├────────────────────┤  │
│  │ Empresa             │ │ Email              │  │
│  │ [input]             │ │ [input]            │  │
│  ├────────────────────┤ ├────────────────────┤  │
│  │ Rubro / Industria   │ │ Empleados          │  │
│  │ [select]            │ │ [select]           │  │
│  ├────────────────────┴─┴────────────────────┤  │
│  │ ¿Qué diagnóstico te interesa?             │  │
│  │ [ ] Integral  [ ] Financiero              │  │
│  │ [ ] Estratégico  [ ] Operativo            │  │
│  │ [ ] No sé / Ayudame a elegir              │  │
│  ├──────────────────────────────────────────┤  │
│  │ Mensaje / Consulta adicional              │  │
│  │ [textarea opcional]                       │  │
│  ├──────────────────────────────────────────┤  │
│  │ [✅] Acepto términos y condiciones        │  │
│  │ [✅] Acepto política de privacidad        │  │
│  ├──────────────────────────────────────────┤  │
│  │ [Solicitar diagnóstico]                  │  │
│  └──────────────────────────────────────────┘  │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  VÍA ALTERNATIVA                                 │
│  "También podés contactarnos por:"              │
│  [WhatsApp] [Email] [Teléfono]                  │
│                                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  SELLOS DE CONFIANZA                             │
│  ┌──────┐ ┌──────┐ ┌──────┐                    │
│  │Dato  │ │Confid│ │Metod.│                    │
│  │seguro│ │encial│ │inter.│                    │
│  └──────┘ └──────┘ └──────┘                    │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Reglas del formulario

| Regla | Especificación |
|---|---|
| **Campos obligatorios** | Solo nombre, email y teléfono. El resto son opcionales o con default |
| **Validación** | Email válido, teléfono con código de área |
| **Mensaje de error** | Específico: "Revisá el formato del email" en lugar de "Campo inválido" |
| **Post-submit** | Redirigir a página de "Gracias" con resumen de próximos pasos |
| **Progressive profiling** | En segunda visita, pedir datos adicionales (empleados, facturación) |

---

## ELEMENTOS GLOBALES DE CONFIANZA

### Sellos y señales de confianza (presentes en todas las páginas)

| Elemento | Ubicación |
|---|---|
| Logos de empresas que confiaron | Home (post-hero) + Servicios |
| Badge "Confidencialidad garantizada" | Footer + formulario |
| Badge "Metodologías reconocidas" | Footer + sección metodología |
| Testimonios | Home + página de servicio |
| Años de experiencia / diagnósticos realizados | Home + hero de servicios |
| Política de privacidad visible | Footer + previo a submit |

### Footer (todas las páginas)

```
┌─────────────────────────────────────────────────┐
│  ┌─────────┐  ┌──────────┐  ┌─────────────┐   │
│  │ [Logo]  │  │ Servicios│  │ Metodología  │   │
│  │         │  │ · Integral│ │ · Proceso    │   │
│  │         │  │ · Finan. │  │ · IA + Humano│   │
│  │         │  │ · Estrat.│  │ · Frameworks │   │
│  │         │  │ · Operat │  └─────────────┘   │
│  └─────────┘  └──────────┘                     │
│                                                 │
│  ┌─────────────┐  ┌──────────────────┐         │
│  │ Contacto    │  │ Legal             │         │
│  │ · WhatsApp  │  │ · Términos       │         │
│  │ · Email     │  │ · Privacidad     │         │
│  │ · Linkedin  │  │ · Defensa        │         │
│  └─────────────┘  └──────────────────┘         │
│                                                 │
│  "© 2025 [Nombre]. Todos los derechos           │
│   reservados. Diagnóstico empresarial con IA."  │
└─────────────────────────────────────────────────┘
```

---

## FLUJO DE CONVERSIÓN

### Customer journey en el sitio

```
VISITANTE LLEGA
      │
      ▼
┌─────────────────┐     ┌─────────────────┐
│  Sabe qué        │     │  No sabe qué     │
│  necesita        │     │  necesita        │
└────────┬────────┘     └────────┬────────┘
         │                       │
         ▼                       ▼
   /servicios               /casos-de-uso
         │                       │
         └───────────┬───────────┘
                     ▼
             /metodologia
            (construir confianza)
                     │
                     ▼
                /contacto
                     │
                     ▼
               FORMULARIO
                     │
                     ▼
            PÁGINA DE GRACIAS
            · Resumen de lo que sigue
            · Timeline (7 días)
            · Botón de WhatsApp
            · Invitación a calendario
```

### Página de "Gracias" post-formulario

```
┌─────────────────────────────────────────────────┐
│                                                 │
│  ✅ "Recibimos tu solicitud"                    │
│                                                 │
│  "En las próximas 24 horas hábiles te vamos a   │
│   contactar para coordinar los próximos pasos."  │
│                                                 │
│  Mientras tanto:                                │
│  ┌────────────────────────────────────────────┐ │
│  │ 📋 ¿Qué información ir preparando?         │ │
│  │ · Estado de resultados (últimos 12 meses)  │ │
│  │ · Balance general                          │ │
│  │ · Flujo de fondos (si está disponible)     │ │
│  └────────────────────────────────────────────┘ │
│                                                 │
│  ¿Tenés urgencia?                               │
│  [Escribinos por WhatsApp]                      │
│                                                 │
│  [Volver al sitio]                              │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## MÉTRICAS SUGERIDAS DE SEGUIMIENTO

| Página | KPI principal | KPI secundario |
|---|---|---|
| Home | Tasa de clic a CTA principal | Tiempo en página |
| Servicios | Tasa de conversión a formulario | Engagement con tabla comparativa |
| Metodología | Tiempo en página | Scroll depth |
| Casos de Uso | Clic en "Quiero este diagnóstico" | Tasa de rebote |
| FAQ | Tasa de expansión de preguntas | Tasa de clic a CTA final |
| Contacto | Tasa de completitud de formulario | Tasa de abandono por campo |
| Global | Tasa de conversión general | Leads calificados / leads totales |
