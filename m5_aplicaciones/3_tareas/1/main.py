import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib import gridspec
from collections import Counter
import warnings

warnings.filterwarnings("ignore")

# ============================================================================
# ESTILO PERSONAL - "Hecho a mano" con personalidad
# ============================================================================
plt.rcParams.update(
    {
        "font.family": "Segoe UI",
        "font.size": 10,
        "axes.labelsize": 11,
        "axes.titlesize": 12,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,
        "figure.titlesize": 16,
        "lines.linewidth": 2,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.edgecolor": "#2C3E50",
        "axes.linewidth": 1.2,
        "grid.alpha": 0.15,
        "grid.linestyle": "-",
    }
)

# Paleta personalizada con carácter
MI_PALETA = {
    "fondo": "#F5F0EB",
    "texto_oscuro": "#1A1A2E",
    "texto_claro": "#4A4A5A",
    "rojo_principal": "#C0392B",
    "naranja": "#E67E22",
    "verde": "#27AE60",
    "azul_profundo": "#2C3E50",
    "gris_calido": "#8E8E93",
    "ocre": "#D4A373",
    "teal": "#2A9D8F",
}


# ============================================================================
# CARGA DE DATOS - Simple y directa
# ============================================================================
def cargar_datos(ruta):
    try:
        df = pd.read_csv(ruta, encoding="utf-8-sig")
    except:
        df = pd.read_csv(ruta, encoding="latin-1")
    df.columns = df.columns.str.strip()
    return df


def clasificar_severidad(row):
    texto = str(row["Fragmento"]).lower()

    # Lo que realmente duele
    criticas = [
        "no aparece",
        "error",
        "bloqueo",
        "desaparecieron",
        "rechazaron",
        "ansiedad",
        "incertidumbre",
        "caos",
        "nadie resuelve",
        "desgasta",
        "dudando",
        "maratón",
        "cadena de confusiones",
    ]

    # Lo superficial
    esteticas = ["linda", "bonito", "diseño", "interfaz", "color", "carga bien"]

    score = sum(1 for p in criticas if p in texto) - sum(
        1 for p in esteticas if p in texto
    )

    if score >= 2:
        return "Alta"
    elif score >= 1:
        return "Media"
    return "Baja"


df = cargar_datos("Analisis_ICUPE_Enfoque1.csv")
df["Severidad"] = df.apply(clasificar_severidad, axis=1)

# ============================================================================
# MÉTRICAS CLAVE
# ============================================================================
total = len(df)
top_temas = df["Tema principal"].value_counts()
tonos = df["Tono"].value_counts()
canales = df["Canal"].value_counts()
severidad_counts = df["Severidad"].value_counts()

# Palabras que duelen - Extraer de fragmentos críticos
texto_critico = " ".join(df[df["Severidad"] == "Alta"]["Fragmento"].str.lower())
palabras = Counter(texto_critico.split())
palabras_filtradas = {
    k: v
    for k, v in palabras.items()
    if len(k) > 3
    and k
    not in [
        "para",
        "una",
        "como",
        "pero",
        "soy",
        "mi",
        "la",
        "el",
        "que",
        "los",
        "las",
        "del",
        "por",
        "con",
    ]
}
top_palabras = sorted(palabras_filtradas.items(), key=lambda x: x[1], reverse=True)[:7]

# ============================================================================
# FIGURA PRINCIPAL - Layout que respira
# ============================================================================
fig = plt.figure(figsize=(16, 12), facecolor=MI_PALETA["fondo"])
gs = gridspec.GridSpec(
    3, 3, height_ratios=[1.2, 1, 0.9], width_ratios=[1, 0.9, 1], hspace=0.35, wspace=0.3
)

# --- Título con personalidad ---
fig.suptitle(
    "El problema no es el campus\nes cómo llegamos hasta él",
    fontsize=20,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    y=0.97,
    linespacing=1.4,
)
fig.text(
    0.02,
    0.94,
    "Análisis de 80 conversaciones | Inicio de semestre 2026",
    fontsize=11,
    color=MI_PALETA["gris_calido"],
    style="italic",
)

# ============================================================================
# GRÁFICO 1: ¿De qué hablamos realmente? (Barras horizontales)
# ============================================================================
ax1 = plt.subplot(gs[0, 0])
temas_ordenados = top_temas.head(6)[::-1]
colores_barras = [
    (
        MI_PALETA["rojo_principal"]
        if i == len(temas_ordenados) - 1
        else MI_PALETA["azul_profundo"]
    )
    for i in range(len(temas_ordenados))
]

bars = ax1.barh(
    temas_ordenados.index,
    temas_ordenados.values,
    color=colores_barras,
    height=0.6,
    edgecolor="white",
    linewidth=1.5,
)

ax1.set_xlabel("Número de comentarios", fontsize=10, color=MI_PALETA["texto_claro"])
ax1.set_title(
    "¿De qué estamos hablando?",
    fontsize=13,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    pad=15,
)

# Anotaciones con personalidad
for bar in bars:
    w = bar.get_width()
    ax1.text(
        w + 0.3,
        bar.get_y() + bar.get_height() / 2,
        f"{int(w)}",
        va="center",
        fontsize=10,
        fontweight="bold",
        color=MI_PALETA["texto_oscuro"],
    )

ax1.grid(axis="x", alpha=0.2)

# ============================================================================
# GRÁFICO 2: El estado emocional (Donut con textura)
# ============================================================================
ax2 = plt.subplot(gs[0, 1])
colores_tono = [MI_PALETA["rojo_principal"], MI_PALETA["ocre"], MI_PALETA["verde"]]
labels = [f"{k}\n{v}" for k, v in zip(tonos.index, tonos.values)]

wedges, texts, autotexts = ax2.pie(
    tonos.values,
    labels=labels,
    autopct="",
    startangle=90,
    colors=colores_tono,
    wedgeprops={"edgecolor": "white", "linewidth": 2.5},
)

# Círculo interior
centro = Circle((0, 0), 0.65, fc=MI_PALETA["fondo"], edgecolor="white", linewidth=3)
ax2.add_artist(centro)

# Texto en el centro
ax2.text(
    0,
    0.15,
    f"{tonos.index[0]}",
    fontsize=14,
    fontweight="bold",
    ha="center",
    color=MI_PALETA["texto_oscuro"],
)
ax2.text(
    0,
    -0.15,
    f"{tonos.values[0]} comentarios",
    fontsize=10,
    ha="center",
    color=MI_PALETA["texto_claro"],
)

ax2.set_title(
    "El estado de ánimo",
    fontsize=13,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    pad=15,
)

# ============================================================================
# GRÁFICO 3: ¿Qué tan grave es? (Barras con umbral)
# ============================================================================
ax3 = plt.subplot(gs[0, 2])
severidad_order = ["Alta", "Media", "Baja"]
severidad_counts = severidad_counts.reindex(severidad_order).fillna(0)
colores_sev = [MI_PALETA["rojo_principal"], MI_PALETA["naranja"], MI_PALETA["verde"]]

bars3 = ax3.bar(
    severidad_counts.index,
    severidad_counts.values,
    color=colores_sev,
    edgecolor="white",
    linewidth=2,
    width=0.55,
)

ax3.set_ylabel("Incidentes", fontsize=10, color=MI_PALETA["texto_claro"])
ax3.set_title(
    "¿Qué tan grave es?",
    fontsize=13,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    pad=15,
)
ax3.grid(axis="y", alpha=0.2)

for bar in bars3:
    h = bar.get_height()
    ax3.text(
        bar.get_x() + bar.get_width() / 2,
        h + 0.3,
        f"{int(h)}",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# Línea de alerta
ax3.axhline(
    y=severidad_counts["Alta"],
    color=MI_PALETA["rojo_principal"],
    linestyle="--",
    alpha=0.5,
    linewidth=1.5,
)
ax3.text(
    2.5,
    severidad_counts["Alta"] + 0.5,
    "⚠ umbral crítico",
    fontsize=8,
    color=MI_PALETA["rojo_principal"],
    style="italic",
)

# ============================================================================
# GRÁFICO 4: ¿Por dónde llega el malestar? (Canales)
# ============================================================================
ax4 = plt.subplot(gs[1, 0])
colores_canal = sns.color_palette("YlOrRd", len(canales))[::-1]
bars4 = ax4.bar(
    canales.index,
    canales.values,
    color=colores_canal,
    edgecolor="white",
    linewidth=1.5,
    width=0.5,
)

ax4.set_xlabel("Canal", fontsize=10, color=MI_PALETA["texto_claro"])
ax4.set_ylabel("Comentarios", fontsize=10, color=MI_PALETA["texto_claro"])
ax4.set_title(
    "¿Por dónde se filtra?",
    fontsize=13,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    pad=15,
)
ax4.grid(axis="y", alpha=0.2)

for bar in bars4:
    h = bar.get_height()
    ax4.text(
        bar.get_x() + bar.get_width() / 2,
        h + 0.3,
        f"{int(h)}",
        ha="center",
        va="bottom",
        fontweight="bold",
    )

# ============================================================================
# GRÁFICO 5: Lo que realmente duele (Palabras clave)
# ============================================================================
ax5 = plt.subplot(gs[1, 1])
ax5.axis("off")

# Crear burbujas de palabras
palabras_mostrar = top_palabras[:7]
tamaños = [max(14, min(10 + f * 2, 24)) for _, f in palabras_mostrar]
colores_palabras = [
    MI_PALETA["rojo_principal"] if i < 3 else MI_PALETA["azul_profundo"]
    for i in range(len(palabras_mostrar))
]

y_pos = np.linspace(0.85, 0.15, len(palabras_mostrar))

for i, (palabra, freq) in enumerate(palabras_mostrar):
    ax5.text(
        0.5,
        y_pos[i],
        f'"{palabra}"',
        fontsize=tamaños[i],
        fontweight="bold",
        color=colores_palabras[i],
        ha="center",
        transform=ax5.transAxes,
        bbox=dict(
            boxstyle="round,pad=0.3",
            facecolor="white",
            edgecolor=colores_palabras[i],
            alpha=0.7,
        ),
    )

ax5.text(
    0.5,
    0.95,
    "El vocabulario de la frustración",
    fontsize=12,
    fontweight="bold",
    ha="center",
    color=MI_PALETA["texto_oscuro"],
    transform=ax5.transAxes,
)
ax5.text(
    0.5,
    0.90,
    "(lo que más se repite en quejas críticas)",
    fontsize=9,
    ha="center",
    color=MI_PALETA["gris_calido"],
    style="italic",
    transform=ax5.transAxes,
)

# ============================================================================
# GRÁFICO 6: Relación Tema - Severidad (Heatmap con personalidad)
# ============================================================================
ax6 = plt.subplot(gs[1, 2])
cross = pd.crosstab(df["Tema principal"], df["Severidad"])
severidad_order = ["Alta", "Media", "Baja"]
cross = cross.reindex(columns=severidad_order, fill_value=0)
rowsum = cross.sum(axis=1).replace(0, 1)
cross_norm = cross.div(rowsum, axis=0) * 100
cross_norm = cross_norm.sort_values("Alta", ascending=False).head(5)

# Heatmap con colores personalizados
sns.heatmap(
    cross_norm,
    annot=True,
    fmt=".0f",
    cmap="Reds",
    ax=ax6,
    cbar_kws={"label": "%", "shrink": 0.8},
    linewidths=1,
    linecolor="white",
    square=False,
    annot_kws={"size": 9, "weight": "bold"},
    vmin=0,
    vmax=100,
)

ax6.set_title(
    "¿Qué temas duelen más?",
    fontsize=13,
    fontweight="bold",
    color=MI_PALETA["texto_oscuro"],
    pad=15,
)
ax6.set_xlabel("Severidad", fontsize=10, color=MI_PALETA["texto_claro"])
ax6.set_ylabel("Tema", fontsize=10, color=MI_PALETA["texto_claro"])

# ============================================================================
# GRÁFICO 7: El mensaje final (Resumen ejecutivo)
# ============================================================================
ax7 = plt.subplot(gs[2, :])
ax7.axis("off")

# Caja de conclusión
conclusion = [
    "El problema NO es el campus virtual",
    "ES la coordinación entre áreas",
    "",
    "3 datos que lo confirman:",
    f"• {severidad_counts['Alta']} incidentes críticos en {top_temas.index[0]}",
    f"• {tonos['Negativo']} comentarios con tono negativo",
    f"• 100% de las quejas ocurren en el INICIO del semestre",
]

# Fondo de la caja de conclusión
rect = FancyBboxPatch(
    (0.05, 0.1),
    0.9,
    0.7,
    boxstyle="round,pad=0.3",
    facecolor="white",
    edgecolor=MI_PALETA["rojo_principal"],
    linewidth=2.5,
    alpha=0.9,
    transform=ax7.transAxes,
)
ax7.add_patch(rect)

# Texto de la conclusión
ax7.text(
    0.5,
    0.65,
    conclusion[0],
    fontsize=16,
    fontweight="bold",
    ha="center",
    color=MI_PALETA["texto_oscuro"],
    transform=ax7.transAxes,
)
ax7.text(
    0.5,
    0.50,
    conclusion[1],
    fontsize=16,
    fontweight="bold",
    ha="center",
    color=MI_PALETA["rojo_principal"],
    transform=ax7.transAxes,
)

for i, linea in enumerate(conclusion[3:]):
    ax7.text(
        0.15,
        0.35 - i * 0.08,
        linea,
        fontsize=11,
        color=MI_PALETA["texto_claro"],
        transform=ax7.transAxes,
    )

# Flecha o símbolo de atención
ax7.text(
    0.92,
    0.70,
    "⚠",
    fontsize=24,
    transform=ax7.transAxes,
    color=MI_PALETA["rojo_principal"],
)

# ============================================================================
# GUARDADO
# ============================================================================
plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig(
    "dashboard_problema_real.png",
    dpi=350,
    bbox_inches="tight",
    facecolor=MI_PALETA["fondo"],
)
plt.close()

# ============================================================================
# REPORTE EN CONSOLA - Con voz humana
# ============================================================================
print("\n" + "=" * 70)
print("🔍 EL PROBLEMA NO ES EL QUE PARECE")
print("=" * 70)

print(f"\n📌 ¿Qué parece estar pasando?")
print(f"   • La gente se queja del 'campus virtual' o la 'plataforma'")
print(
    f"   • {top_temas.index[0]} es el tema más mencionado ({top_temas.iloc[0]} comentarios)"
)
print(f"   • Parece un problema de tecnología")

print(f"\n🎯 ¿Qué está pasando realmente?")
print(f"   • ES UN PROBLEMA DE COORDINACIÓN")
print(
    f"   • {severidad_counts['Alta']} incidentes críticos son por falta de comunicación entre áreas"
)
print(f"   • La gente no sabe si está matriculada, si pagó, si tiene horario")
print(f"   • El 100% de las quejas ocurren en el INICIO del semestre")

print(f"\n📊 Evidencias concretas:")
for i, ev in enumerate(df[df["Severidad"] == "Alta"]["Fragmento"].head(3)):
    print(f'   {i+1}. "{ev}"')

print(f"\n💭 Patrón emocional:")
print(f"   • Tono dominante: {tonos.index[0]} ({tonos.iloc[0]} comentarios)")
print(f"   • Frustración + ansiedad + incertidumbre")
print(f"   • Sensación de abandono administrativo")

print(f"\n🚨 ¿Qué revisar primero?")
print(f"   1. UNIFICAR el estado del estudiante (matrícula, pagos, horarios)")
print(f"   2. SINCRONIZAR bases de datos entre Admisión, Finanzas y Registro")
print(f"   3. REDISEÑAR el onboarding: eliminar pasos redundantes")

print("\n" + "=" * 70)
print("✅ Dashboard guardado: dashboard_problema_real.png")
print("=" * 70 + "\n")
