# IDENTIDAD VISUAL — Guía de Marca Klar Analytics

## 1. Filosofía Visual

La identidad visual traduce al lenguaje gráfico los atributos centrales de la marca: **claridad, inteligencia, confianza, profesionalismo y modernidad**.

El sistema visual debe sentirse como un diagnóstico bien hecho: ordenado, preciso, sin elementos superfluos. Cada decisión visual existe por una razón.

### Símbolo de marca elegido

El logotipo de Klar Analytics es el concepto **Señal / Indicador**: una gráfica con línea de base que detecta un pico preciso, rematado por un punto sólido Azul 800 con un punto interior Teal 500. Representa el acto de diagnosticar: detectar la anomalía, señalar con exactitud el hallazgo.

```
Archivos de logo:
  Klar_Analytics_Logo.svg      — Logotipo horizontal completo (símbolo + nombre + tagline)
  Klar_Analytics_Favicon.svg   — Símbolo reducido para favicon y avatar
```

### Tratamiento del nombre en la identidad

**Klar Analytics** debe leerse visualmente como una unidad, pero con pesos diferenciados:

| Elemento | Peso | Rol |
|---|---|---|
| **Klar** | Bold (700) o ExtraBold (800) | El nombre propio — lidera, es contundente |
| **Analytics** | Regular (400) o Light (300) | El descriptor — acompaña, define el dominio |
| **Espaciado entre términos** | 0.3–0.5em | Separación limpia que permite leer ambos con claridad |

En versión vertical, "Klar" va arriba con mayor peso, "Analytics" abajo en tamaño reducido (~60–70% del tamaño de Klar).

### Principios rectores del diseño

| Principio | Aplicación |
|---|---|
| **Claridad ante todo** | Espacio en blanco abundante, jerarquía visual limpia |
| **Precisión quirúrgica** | Alineación rigurosa, espaciados consistentes |
| **Calma profesional** | Sin ruido visual, sin elementos decorativos sin función |
| **Tecnología al servicio humano** | Interfaces y materiales que se sienten inteligentes pero cálidos |
| **Klar = directo, sin ambigüedad** | Cada elemento visual tiene una razón clara de existir |

---

## 2. Paleta de Color Principal

La paleta se construye sobre azules que transmiten confianza, inteligencia y profesionalismo, con luminosidad para evitar el peso visual de los azules corporativos tradicionales.

### Azul Profundo — Confianza y autoridad

Usar en: títulos principales, headers, fondos de secciones importantes, botones primarios.

| Token | HEX | RGB | CMYK | Uso |
|---|---|---|---|---|
| `--blue-900` | `#0A2540` | 10, 37, 64 | 96, 78, 38, 61 | Fondos oscuros, textos sobre fondo claro |
| `--blue-800` | `#134078` | 19, 64, 120 | 90, 68, 20, 21 | Títulos, botones primarios |
| `--blue-700` | `#1A5A9E` | 26, 90, 158 | 86, 54, 7, 5 | Headers, acentos principales |

### Azul Medio — Inteligencia y claridad

Usar en: subtítulos, íconos, gráficos, enlaces, fondos de tarjetas.

| Token | HEX | RGB | CMYK | Uso |
|---|---|---|---|---|
| `--blue-500` | `#3182CE` | 49, 130, 206 | 76, 37, 0, 0 | Botones secundarios, íconos, links |
| `--blue-400` | `#63B3ED` | 99, 179, 237 | 58, 12, 0, 0 | Gráficos, acentos |

### Azul Claro / Celeste — Claridad y apertura

Usar en: fondos de sección, backgrounds de dashboard, ilustraciones, badges.

| Token | HEX | RGB | CMYK | Uso |
|---|---|---|---|---|
| `--blue-200` | `#BEE3F8` | 190, 227, 248 | 22, 5, 0, 0 | Fondos de tarjetas, secciones alternadas |
| `--blue-100` | `#EBF4FF` | 235, 244, 255 | 8, 3, 0, 0 | Fondos generales, hover states |
| `--blue-50` | `#F5FAFF` | 245, 250, 255 | 3, 1, 0, 0 | Fondos de página, backgrounds amplios |

---

## 3. Paleta Secundaria — Neutros

Los neutros proporcionan la estructura visual y aseguran legibilidad y jerarquía sin competir con los azules.

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--white` | `#FFFFFF` | 255, 255, 255 | Fondos primarios, tarjetas |
| `--gray-50` | `#F8F9FA` | 248, 249, 250 | Fondos alternados |
| `--gray-100` | `#F1F3F5` | 241, 243, 245 | Bordes sutiles, separadores |
| `--gray-200` | `#E2E6EA` | 226, 230, 234 | Bordes, inputs |
| `--gray-400` | `#9CA3AF` | 156, 163, 175 | Texto secundario, metadatos |
| `--gray-600` | `#4B5563` | 75, 85, 99 | Texto corporal |
| `--gray-800` | `#1F2937` | 31, 41, 55 | Texto principal |
| `--gray-900` | `#111827` | 17, 24, 39 | Títulos, encabezados |

---

## 4. Colores de Acento

Los acentos se usan con moderación para destacar información clave sin romper la armonía general.

### Acento principal — Teal / Azul verdoso

Comunica modernidad, frescura y un toque humano. Se usa en CTAs secundarios, highlights y elementos interactivos.

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--teal-500` | `#14B8A6` | 20, 184, 166 | Acentos, badges, indicadores positivos |

### Acento secundario — Ámbar suave

Para alertas, advertencias o destacar oportunidades. Cálido sin ser agresivo.

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--amber-400` | `#FBBF24` | 251, 191, 36 | Advertencias, estrellas, ratings |

### Acento de dato — Verde para positivo, Rojo suave para negativo

Usar exclusivamente en gráficos e indicadores de desempeño.

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--green-500` | `#10B981` | 16, 185, 129 | Indicadores positivos, crecimiento |
| `--red-400` | `#F87171` | 248, 113, 113 | Indicadores de alerta, riesgo |

---

## 5. Tipografía

### Tipografía principal — Inter (Sans-serif)

**Inter** es la tipografía oficial para **Klar Analytics**. Diseñada específicamente para interfaces digitales y lectura en pantalla. Combina excelente legibilidad con un carácter técnico pero accesible.

**Uso en el logotipo:** "Klar" se compone en Inter Bold (700) con tracking −0.5px para darle contundencia. "Analytics" se compone en Inter Light (300) con tracking +1px para equilibrar y airear. La diferencia de peso refuerza la jerarquía: **el nombre pesa, el descriptor fluye**.

| Propósito | Peso | Tamaño | Altura de línea |
|---|---|---|---|
| Título principal | Bold (700) | 40–48px | 1.2 |
| Título secundario | SemiBold (600) | 28–36px | 1.25 |
| Subtítulo | Medium (500) | 20–24px | 1.3 |
| Cuerpo | Regular (400) | 16–18px | 1.6 |
| Cuerpo pequeño | Regular (400) | 14px | 1.5 |
| Metadato / Label | Medium (500) | 12–13px | 1.4 |
| Caption | Regular (400) | 11–12px | 1.4 |

### Tipografía secundaria — Outfit (Display)

**Outfit** se usa para aplicaciones display: hero sections, títulos de landing page, material de marca impreso.

| Propósito | Peso | Tamaño |
|---|---|---|
| Hero / Grandes títulos | Bold (700) | 56–72px |
| Títulos de sección destacados | SemiBold (600) | 40–48px |

### Tipografía para datos — JetBrains Mono (Monospace)

Para tablas, dashboards, gráficos con valores, informes descargables.

| Propósito | Peso | Tamaño |
|---|---|---|
| Valores numéricos, tablas | Regular (400) | 14–16px |
| Códigos, IDs | Medium (500) | 12–14px |

---

## 6. Sistema Visual

### Formas y geometría

El sistema visual se basa en formas limpias y precisas:

| Elemento | Regla |
|---|---|
| **Esquinas de tarjetas** | Border-radius: 12px (tarjetas), 8px (botones) |
| **Botones** | Border-radius: 8px, padding vertical 12px, horizontal 24px |
| **Inputs** | Border-radius: 8px, borde 1.5px solid gray-200 |
| **Sombras** | Sombra suave y cercana (`0 2px 8px rgba(10, 37, 64, 0.06)`) |
| **Separadores** | Línea fina de 1px, color gray-100 |
| **Grid** | Sistema de 12 columnas, gutter 24px |

### Espaciado

| Token | Valor | Uso |
|---|---|---|
| `--space-xs` | 4px | Espaciados mínimos |
| `--space-sm` | 8px | Entre elementos relacionados |
| `--space-md` | 16px | Entre elementos agrupados |
| `--space-lg` | 24px | Entre secciones |
| `--space-xl` | 40px | Entre bloques mayores |
| `--space-2xl` | 64px | Entre secciones de página |

### Jerarquía visual

1. **Título** → Azul 800, Bold, 40px
2. **Subtítulo** → Gray 600, Regular, 20px
3. **Cuerpo** → Gray 600, Regular, 16px
4. **Dato destacado** → Teal 500 o Azul 500, SemiBold
5. **Metadato** → Gray 400, Medium, 13px

---

## 7. Estilo de Iconografía

### Principios

- Trazo uniforme (2px para iconos de 24×24)
- Sin relleno (outline style)
- Esquinas con radio suave (1.5px)
- Estilo coherente: misma familia (recomendado: Phosphor Icons o Lucide)

### Paleta de iconos

| Contexto | Color de icono |
|---|---|
| Navegación principal | Azul 500 |
| Acciones primarias | Azul 800 |
| Indicadores positivos | Teal 500 |
| Alertas | Amber 400 |
| Datos / Analytics | Azul 500 |
| Íconos sobre fondo de color | Blanco |

### Categorías de iconos

- **Diagnóstico**: lupa, radar, escáner, checklist, termómetro
- **Estrategia**: brújula, mapa, nodos, flechas, diana
- **Análisis**: gráfico de barras, gráfico de torta, tabla, lupa con documento
- **Decisión**: check, switch, filtro, ordenar
- **Confianza**: escudo, candado, verificado

---

## 8. Estilo Fotográfico

### Qué buscar

- Personas reales en entornos laborales auténticos (no estudios fotográficos)
- Empresarios, dueños de PyME, equipos reducidos trabajando
- Espacios de trabajo luminosos, ordenados, con luz natural
- Expresiones de concentración, colaboración, confianza
- Ambientes que reflejen trabajo serio pero no corporativo pesado

### Qué evitar

- Fotos de stock genéricas con modelos sonriendo artificialmente
- Ejecutivos en traje y corbata en salas de reunión impersonales
- Fotos con fondos negros o saturados
- Imágenes con saturación excesiva o filtros dramáticos
- Escenas de tecnología abstracta (luces borrosas, servidores, cables)

### Tratamiento de color en fotografía

| Atributo | Valor |
|---|---|
| Saturación | Ligeramente desaturada (−10%) |
| Temperatura | Neutro-ligeramente fría (4800K) |
| Contraste | Suave, sombras levantadas |
| Tono | Inclinación sutil hacia azules en sombras |

---

## 9. Sistema de Componentes

### Tarjetas / Cards

```
┌─────────────────────────────┐
│                             │
│  [Icono]   Título           │  ← Azul 800, SemiBold
│                             │
│  Texto descriptivo          │  ← Gray 600, Regular, 16px
│  breve y conciso.           │
│                             │
│  ───────────────────────    │  ← Separador gray-100
│  → Acción                  │  ← Azul 500, Medium
│                             │
└─────────────────────────────┘
  Sombra: 0 2px 8px rgba(10,37,64,0.06)
  Border-radius: 12px
  Background: white
  Padding: 24px
```

### Botones

| Tipo | Fondo | Texto | Hover |
|---|---|---|---|
| Primario | Azul 800 | Blanco | Azul 700 |
| Secundario | Blanco, borde Azul 500 | Azul 500 | Azul 50 |
| Terciario | Transparente | Azul 500 | Gray 50 |
| Acento | Teal 500 | Blanco | Teal 600 |

### Dashboard / Indicadores

- **KPI cards**: Fondo blanco, número grande en Azul 800 o Gray 900, label en Gray 400
- **Progreso**: Barra delgada (4px), color Azul 500, fondo Gray 100
- **Estado**: Badge pequeño, border-radius 999px, relleno según contexto
  - Verde: `--green-500` fondo, blanco texto
  - Rojo: `--red-400` fondo, blanco texto
  - Neutro: Gray 100 fondo, Gray 600 texto

---

## 10. Reglas de Accesibilidad

### Contraste mínimo WCAG 2.1 AA

| Combinación | Ratio mínimo | Ejemplo |
|---|---|---|
| Texto normal sobre fondo | 4.5:1 | Gray 800 sobre blanco ✓ |
| Texto grande (≥18px bold o ≥24px) | 3:1 | Azul 800 sobre blanco ✓ |
| Componentes UI | 3:1 | Borde de input sobre fondo ✓ |

### Combinaciones validadas

| Fondo | Texto | Ratio | Cumple |
|---|---|---|---|
| Blanco #FFFFFF | Gray 800 #1F2937 | 13.5:1 | ✅ AA / AAA |
| Blanco #FFFFFF | Azul 800 #134078 | 8.2:1 | ✅ AA / AAA |
| Blanco #FFFFFF | Azul 500 #3182CE | 4.8:1 | ✅ AA |
| Azul 50 #F5FAFF | Gray 800 #1F2937 | 13:1 | ✅ AA / AAA |
| Azul 800 #134078 | Blanco #FFFFFF | 8.2:1 | ✅ AA / AAA |
| Azul 900 #0A2540 | Azul 200 #BEE3F8 | 7.5:1 | ✅ AA / AAA |
| Teal 500 #14B8A6 | Blanco #FFFFFF | 4.2:1 | ✅ AA (solo texto grande ≥24px) |

### Tamaño mínimo de texto

| Contexto | Mínimo |
|---|---|
| Cuerpo web | 16px |
| Cuerpo mobile | 15px |
| Labels / Metadatos | 12px |
| Botones | 14px |

### Áreas táctiles

| Elemento | Mínimo |
|---|---|
| Botones y links | 44×44px |
| Inputs | 44px de altura |
| Iconos clickeables | 44×44px (área de toque) |

### Otras consideraciones

- Todos los iconos deben incluir etiqueta `aria-label` cuando no tengan texto acompañante
- Los gráficos deben tener alternativas textuales (tablas de datos asociadas)
- El contraste de los gráficos debe mantenerse incluso en escala de grises
- No usar el color como único indicador de estado (incluir texto o iconos)
- Respetar el movimiento reducido en animaciones (`prefers-reduced-motion`)

---

## 11. Aplicaciones de Marca

### Papelería digital

| Elemento | Especificación |
|---|---|
| **Logotipo** | Símbolo Señal/Indicador + "Klar" en Inter Bold + "Analytics" en Inter Light — horizontal |
| **Favicon** | 32×32px, 16×16px, 180×60px. Símbolo: pico + punto. Archivo: `Klar_Analytics_Favicon.svg` |
| **Presentaciones** | Fondo blanco o Azul 900, tipografía Inter, gráficos en Azul 500. Slide titular: "Klar Analytics" centrado |
| **Informes PDF** | Márgenes 2.5cm, headers con línea Azul 500 de 2px. Logotipo en header (horizontal) |
| **Email signature** | 320px de ancho máximo, "Klar Analytics" + nombre + cargo + datos |
| **Color de enlaces en firma** | Azul 500 `#3182CE` |

### Aplicación del nombre en materiales

| Material | Formato recomendado |
|---|---|
| **Web** | Klar Analytics (completo) — logo horizontal en header |
| **Redes sociales** | "Klar Analytics" o solo "Klar" si el espacio es reducido |
| **Informes** | Klar Analytics (completo) — versión vertical en portada |
| **Presentaciones** | Klar Analytics (completo) — "Klar" notablemente más bold |
| **Favicon / App icon** | Símbolo o "K" — sin "Analytics" |
| **Marca de agua** | "Klar Analytics" en gris claro al 10% opacidad |

---

## 12. Moodboard verbal (look & feel)

| La marca se ve como... | La marca NO se ve como... |
|---|---|
| Un dashboard bien diseñado | Un balance contable escaneado |
| Un libro de estrategia moderno | Un manual corporativo de los 90 |
| Un consultorio luminoso y ordenado | Un escritorio de abogados |
| Una app profesional bien resuelta | Una página de banco institucional |
| Una consultora boutique de alto nivel | Una startup de garaje |

---

## 13. Resumen de códigos HEX

### Paleta rápida (10 colores esenciales)

| Color | HEX | Rol |
|---|---|---|
| Azul profundo | `#0A2540` | Fondo oscuro, contraste máximo |
| Azul corporativo | `#134078` | Títulos, botones primarios |
| Azul medio | `#3182CE` | Íconos, links, gráficos |
| Azul claro | `#63B3ED` | Gráficos, acentos secundarios |
| Celeste fondo | `#BEE3F8` | Fondos de tarjeta |
| Celeste claro | `#EBF4FF` | Fondos de sección |
| Casi blanco | `#F5FAFF` | Fondos de página |
| Teal acento | `#14B8A6` | CTAs, indicadores positivos |
| Gris cuerpo | `#4B5563` | Texto corporal |
| Gris título | `#1F2937` | Títulos, encabezados |
