import pandas as pd
import os

# Ruta del archivo (está en la carpeta 2/)
ruta_archivo = '2/digital_funnel_clean.csv'

# Cargar el dataset
df = pd.read_csv(ruta_archivo)

print("="*80)
print("ANÁLISIS DE VALORES ÚNICOS - digital_funnel_clean.csv")
print("="*80)
print(f"\n📊 Total de registros: {len(df):,}")
print(f"📋 Total de columnas: {len(df.columns)}")
print("\n" + "="*80)

# Recorrer todas las columnas
for columna in df.columns:
    print(f"\n🔍 COLUMNA: {columna}")
    print(f"   Tipo de dato: {df[columna].dtype}")
    print(f"   Valores nulos: {df[columna].isnull().sum():,}")
    print(f"   Valores únicos: {df[columna].nunique():,}")
    
    # Si tiene menos de 20 valores únicos, mostrarlos todos
    if df[columna].nunique() <= 20:
        print("   Valores únicos:")
        for valor in sorted(df[columna].unique()):
            # Contar cuántas veces aparece cada valor
            conteo = df[columna].value_counts()[valor]
            porcentaje = (conteo / len(df)) * 100
            print(f"      • {valor} → {conteo:,} ({porcentaje:.1f}%)")
    else:
        # Si tiene muchos valores, mostrar solo los primeros 10
        print("   Ejemplos de valores únicos (primeros 10):")
        for valor in sorted(df[columna].unique())[:10]:
            conteo = df[columna].value_counts()[valor]
            print(f"      • {valor} → {conteo:,}")
        print(f"   ... y {df[columna].nunique() - 10} valores más")
    
    print("-"*80)

# Resumen rápido de las columnas categóricas principales
print("\n" + "="*80)
print("📌 RESUMEN RÁPIDO - COLUMNAS CLAVE")
print("="*80)

# Traffic_Source
print("\n🌐 TRAFFIC_SOURCE (Origen del tráfico):")
for valor in sorted(df['Traffic_Source'].unique()):
    conteo = df['Traffic_Source'].value_counts()[valor]
    print(f"   • {valor} → {conteo:,}")

# Traffic_Medium
print("\n📱 TRAFFIC_MEDIUM (Medio de adquisición):")
for valor in sorted(df['Traffic_Medium'].unique()):
    conteo = df['Traffic_Medium'].value_counts()[valor]
    print(f"   • {valor} → {conteo:,}")

# Device_Type
print("\n💻 DEVICE_TYPE (Tipo de dispositivo):")
for valor in sorted(df['Device_Type'].unique()):
    conteo = df['Device_Type'].value_counts()[valor]
    print(f"   • {valor} → {conteo:,}")

# Bounce_Flag
print("\n🔄 BOUNCE_FLAG (Rebote):")
for valor in sorted(df['Bounce_Flag'].unique()):
    conteo = df['Bounce_Flag'].value_counts()[valor]
    print(f"   • {valor} → {conteo:,}")

print("\n" + "="*80)
print("✅ Análisis completado!")
print("="*80)