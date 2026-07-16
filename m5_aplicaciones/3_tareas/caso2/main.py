import pandas as pd

# Cargar dataset
df = pd.read_csv("caso2/bpi_2017_cleaned v2.csv")

# ============================================================================
# PREPROCESAMIENTO - Preparación de datos para todos los análisis
# ============================================================================

# 1. Contar eventos por caso
eventos_por_caso = df.groupby("case:concept:name")["EventID"].count().reset_index()
eventos_por_caso.columns = ["case:concept:name", "Total_Eventos"]
df_merged = df.merge(eventos_por_caso, on="case:concept:name")

# 2. Crear segmento de aceptación
df["Segmento_Aceptacion"] = df["Accepted"].apply(
    lambda x: (
        "Aceptado" if x == True else "No Aceptado" if x == False else "Sin Decision"
    )
)

# 3. Convertir timestamp
df["time:timestamp"] = pd.to_datetime(df["time:timestamp"], format="ISO8601")

# 4. Calcular duración por caso
duracion_caso = df.groupby("case:concept:name").agg(
    Fecha_Inicio=("time:timestamp", "min"), Fecha_Fin=("time:timestamp", "max")
)
duracion_caso["Duracion_Horas"] = (
    duracion_caso["Fecha_Fin"] - duracion_caso["Fecha_Inicio"]
).dt.total_seconds() / 3600

# 5. Unir todo en un solo dataframe
df_completo = df_merged.merge(duracion_caso[["Duracion_Horas"]], on="case:concept:name")

# 6. Agregar información de aceptación (solo una vez por caso)
df_aceptacion = df[["case:concept:name", "Segmento_Aceptacion"]].drop_duplicates()
df_completo = df_completo.merge(df_aceptacion, on="case:concept:name")

# 7. Calcular fricción
df_completo["Friccion"] = df_completo["Total_Eventos"] * df_completo["Duracion_Horas"]

# ============================================================================
# PREGUNTA 1: ¿Se comportan igual todos los tipos de caso?
# ============================================================================
print("=" * 80)
print("PREGUNTA 1: ¿Se comportan igual todos los tipos de caso?")
print("=" * 80)

# Por LoanGoal
loan_goal_stats = (
    df_completo.groupby("case:LoanGoal")
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
        Eventos_Total=("EventID", "count"),
        Duracion_Promedio=("Duracion_Horas", "mean"),
    )
    .reset_index()
    .sort_values("Eventos_Promedio", ascending=False)
)

print("\nRESUMEN POR LOANGOAL (ordenado de más a menos complejo):")
print(loan_goal_stats.to_string(index=False))

# Por ApplicationType
app_type_stats = (
    df_completo.groupby("case:ApplicationType")
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
        Eventos_Total=("EventID", "count"),
    )
    .reset_index()
)

print("\nRESUMEN POR APPLICATIONTYPE:")
print(app_type_stats.to_string(index=False))

# ============================================================================
# PREGUNTA 2: ¿Qué diferencias observan según tipo de solicitud, objetivo o aceptación?
# ============================================================================
print("\n" + "=" * 80)
print("PREGUNTA 2: Diferencias según tipo de solicitud, objetivo y nivel de aceptación")
print("=" * 80)

# Por nivel de aceptación
aceptacion_stats = (
    df_completo.groupby("Segmento_Aceptacion")
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
        Eventos_Total=("EventID", "count"),
    )
    .reset_index()
)

print("\n1. POR NIVEL DE ACEPTACIÓN:")
print(aceptacion_stats.to_string(index=False))

# Cruce completo: LoanGoal x ApplicationType x Aceptación
cruce_completo = (
    df_completo.groupby(
        ["case:LoanGoal", "case:ApplicationType", "Segmento_Aceptacion"]
    )
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
    )
    .reset_index()
)

print("\n2. CRUCE COMPLETO (LoanGoal x ApplicationType x Aceptación):")
print(cruce_completo.to_string(index=False))

# ============================================================================
# PREGUNTA 3: ¿Qué segmentos parecen más simples y cuáles más complejos?
# ============================================================================
print("\n" + "=" * 80)
print("PREGUNTA 3: Segmentos más simples y más complejos")
print("=" * 80)

# Identificar el más simple y el más complejo por LoanGoal
mas_simple = loan_goal_stats.loc[loan_goal_stats["Eventos_Promedio"].idxmin()]
mas_complejo = loan_goal_stats.loc[loan_goal_stats["Eventos_Promedio"].idxmax()]

print(f"SEGMENTO MÁS SIMPLE: {mas_simple['case:LoanGoal']}")
print(f"  - Eventos promedio: {mas_simple['Eventos_Promedio']:.1f}")
print(f"  - Duración promedio: {mas_simple['Duracion_Promedio']:.1f} horas")
print(f"  - Casos: {mas_simple['Casos']}")

print(f"\nSEGMENTO MÁS COMPLEJO: {mas_complejo['case:LoanGoal']}")
print(f"  - Eventos promedio: {mas_complejo['Eventos_Promedio']:.1f}")
print(f"  - Duración promedio: {mas_complejo['Duracion_Promedio']:.1f} horas")
print(f"  - Casos: {mas_complejo['Casos']}")

# ============================================================================
# PREGUNTA 4: ¿Qué segmentos muestran más eventos, más fricción o mayor duración?
# ============================================================================
print("\n" + "=" * 80)
print("PREGUNTA 4: Segmentos con más eventos, fricción y duración")
print("=" * 80)

# Estadísticas detalladas por LoanGoal
detalle_loan = (
    df_completo.groupby("case:LoanGoal")
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
        Eventos_Max=("Total_Eventos", "max"),
        Duracion_Promedio=("Duracion_Horas", "mean"),
        Duracion_Mediana=("Duracion_Horas", "median"),
        Friccion_Promedio=("Friccion", "mean"),
    )
    .reset_index()
    .sort_values("Friccion_Promedio", ascending=False)
)

print("DETALLE POR LOANGOAL (ordenado por fricción):")
print(detalle_loan.to_string(index=False))

# Top 5 con mayor fricción
print("\nTOP 5 SEGMENTOS CON MAYOR FRICCIÓN:")
print(
    detalle_loan[
        ["case:LoanGoal", "Friccion_Promedio", "Eventos_Promedio", "Duracion_Promedio"]
    ]
    .head(5)
    .to_string(index=False)
)

# Top 5 con mayor duración
print("\nTOP 5 SEGMENTOS CON MAYOR DURACIÓN:")
print(
    detalle_loan[["case:LoanGoal", "Duracion_Promedio", "Eventos_Promedio"]]
    .head(5)
    .to_string(index=False)
)

# ============================================================================
# PREGUNTA 5: ¿Qué utilidad tendría esta segmentación para la gestión?
# ============================================================================
print("\n" + "=" * 80)
print("PREGUNTA 5: Utilidad de la segmentación para la toma de decisiones")
print("=" * 80)

# Resumen ejecutivo
print("HALLAZGOS CLAVE:")
print("-" * 60)

# 1. Diferencias por LoanGoal
print(f"\n1. OBJETIVO DEL PRÉSTAMO (LoanGoal):")
print(
    f"   > Más complejo: {mas_complejo['case:LoanGoal']} ({mas_complejo['Eventos_Promedio']:.1f} eventos, {mas_complejo['Duracion_Promedio']:.0f} horas)"
)
print(
    f"   > Más simple: {mas_simple['case:LoanGoal']} ({mas_simple['Eventos_Promedio']:.1f} eventos, {mas_simple['Duracion_Promedio']:.0f} horas)"
)
print(
    f"   > Diferencia: {mas_complejo['Eventos_Promedio'] / mas_simple['Eventos_Promedio']:.1f}x más eventos"
)

# 2. Diferencias por ApplicationType
app_mas = app_type_stats.loc[app_type_stats["Eventos_Promedio"].idxmax()]
app_menos = app_type_stats.loc[app_type_stats["Eventos_Promedio"].idxmin()]
print(f"\n2. TIPO DE SOLICITUD (ApplicationType):")
print(
    f"   > {app_mas['case:ApplicationType']}: {app_mas['Eventos_Promedio']:.1f} eventos"
)
print(
    f"   > {app_menos['case:ApplicationType']}: {app_menos['Eventos_Promedio']:.1f} eventos"
)
print(
    f"   > Diferencia: {app_mas['Eventos_Promedio'] / app_menos['Eventos_Promedio']:.1f}x más eventos"
)

# 3. Diferencias por Aceptación
acep_mas = aceptacion_stats.loc[aceptacion_stats["Eventos_Promedio"].idxmax()]
acep_menos = aceptacion_stats.loc[aceptacion_stats["Eventos_Promedio"].idxmin()]
print(f"\n3. NIVEL DE ACEPTACIÓN:")
print(
    f"   > {acep_mas['Segmento_Aceptacion']}: {acep_mas['Eventos_Promedio']:.1f} eventos"
)
print(
    f"   > {acep_menos['Segmento_Aceptacion']}: {acep_menos['Eventos_Promedio']:.1f} eventos"
)
print(
    f"   > Diferencia: {acep_mas['Eventos_Promedio'] / acep_menos['Eventos_Promedio']:.1f}x más eventos"
)

# Recomendaciones
print("\n" + "=" * 80)
print("RECOMENDACIONES PARA LA GESTIÓN:")
print("=" * 80)
print("""
1. PRIORIZAR RECURSOS:
   > Asignar más personal y seguimiento a "Remaining debt home" y "Not speficied"
   > Estandarizar procesos para "Tax payments" y "Business goal"

2. OPTIMIZAR PROCESOS:
   > Reducir pasos en segmentos con alta fricción (Remaining debt home)
   > Simplificar validaciones para casos simples (Tax payments)

3. MEJORAR CONVERSIÓN:
   > Investigar por qué los casos "No Aceptados" tienen más eventos
   > Revisar criterios de aceptación para reducir complejidad innecesaria

4. SEGMENTACIÓN ESTRATÉGICA:
   > Crear equipos especializados por tipo de préstamo
   > Desarrollar flujos de trabajo diferenciados

5. MONITOREO CONTINUO:
   > Seguimiento de métricas por segmento
   > Identificar desviaciones y oportunidades de mejora
""")

# ============================================================================
# COMPARACIÓN ENTRE SEGMENTOS (Top vs Bottom)
# ============================================================================
print("\n" + "=" * 80)
print("COMPARACIÓN ENTRE SEGMENTOS EXTREMOS")
print("=" * 80)

# Segmentos combinados
df_completo["Segmento_Combinado"] = (
    df_completo["case:LoanGoal"] + " | " + df_completo["case:ApplicationType"]
)

segmentos = (
    df_completo.groupby("Segmento_Combinado")
    .agg(
        Casos=("case:concept:name", "nunique"),
        Eventos_Promedio=("Total_Eventos", "mean"),
        Duracion_Promedio=("Duracion_Horas", "mean"),
        Tasa_Aceptacion=("Accepted", lambda x: x.mean() * 100),
    )
    .reset_index()
)

segmentos = segmentos[segmentos["Casos"] >= 10].sort_values(
    "Eventos_Promedio", ascending=False
)

print("\nTOP 5 SEGMENTOS MÁS COMPLEJOS:")
print(
    segmentos.head(5)[
        [
            "Segmento_Combinado",
            "Casos",
            "Eventos_Promedio",
            "Duracion_Promedio",
            "Tasa_Aceptacion",
        ]
    ].to_string(index=False)
)

print("\nTOP 5 SEGMENTOS MÁS SIMPLES:")
print(
    segmentos.tail(5)[
        [
            "Segmento_Combinado",
            "Casos",
            "Eventos_Promedio",
            "Duracion_Promedio",
            "Tasa_Aceptacion",
        ]
    ].to_string(index=False)
)

# Comparación extremos
print("\n" + "=" * 80)
print("COMPARACIÓN EXTREMA:")
print("=" * 80)

segmento_complejo = segmentos.iloc[0]
segmento_simple = segmentos.iloc[-1]

print(f"SEGMENTO MÁS COMPLEJO: {segmento_complejo['Segmento_Combinado']}")
print(f"  > Eventos: {segmento_complejo['Eventos_Promedio']:.1f}")
print(f"  > Duración: {segmento_complejo['Duracion_Promedio']:.1f} horas")
print(f"  > Tasa aceptación: {segmento_complejo['Tasa_Aceptacion']:.1f}%")

print(f"\nSEGMENTO MÁS SIMPLE: {segmento_simple['Segmento_Combinado']}")
print(f"  > Eventos: {segmento_simple['Eventos_Promedio']:.1f}")
print(f"  > Duración: {segmento_simple['Duracion_Promedio']:.1f} horas")
print(f"  > Tasa aceptación: {segmento_simple['Tasa_Aceptacion']:.1f}%")

print(f"\nDIFERENCIA:")
print(
    f"  > Eventos: {segmento_complejo['Eventos_Promedio'] / segmento_simple['Eventos_Promedio']:.1f}x más"
)
print(
    f"  > Duración: {segmento_complejo['Duracion_Promedio'] / segmento_simple['Duracion_Promedio']:.1f}x más"
)

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)
