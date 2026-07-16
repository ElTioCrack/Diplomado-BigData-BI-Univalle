import pandas as pd
import os

# Ruta del archivo original (está en carpeta 2/)
ruta_origen = '2/digital_funnel_clean.csv'
ruta_destino = '2/digital_funnel_clean_TRADUCIDO.csv'

# Cargar el dataset
df = pd.read_csv(ruta_origen)

print("="*80)
print("🔄 TRADUCIENDO DATASET - PORTUGUÉS → ESPAÑOL")
print("="*80)
print(f"📊 Registros a procesar: {len(df):,}")
print("-"*80)

# Diccionario de traducciones para Traffic_Source
traduccion_source = {
    'afiliados / parceiros': 'Afiliados & Socios',  # Cambié / por &
    'direta': 'Directo',
    'email': 'Email',
    'organico': 'Orgánico',
    'outros sites': 'Otros sitios',
    'redes sociais': 'Redes Sociales',
    'youTube': 'YouTube'
}

# Diccionario de traducciones para Traffic_Medium
traduccion_medium = {
    'afiliado': 'Afiliado',
    'cpc / busca Paga': 'CPC & Búsqueda pagada',  # Cambié / por &
    'cpm / display': 'CPM & Display',  # Cambié / por &
    'indicacao': 'Recomendación',
    'nenhum': 'Ninguno',
    'organico': 'Orgánico'
}

# Diccionario de traducciones para Device_Type
traduccion_device = {
    'desktop': 'Escritorio',
    'mobile': 'Móvil',
    'tablet': 'Tableta'
}

# CREAR NUEVO DATAFRAME CON COLUMNAS TRADUCIDAS
df_traducido = pd.DataFrame()

# 1. Traducir valores de las columnas categóricas
df_traducido['ID_Cliente_Digital'] = df['ID_DigitalCustomer']
df_traducido['ID_Sesion_Web'] = df['ID_WebVisit']
df_traducido['Fecha_Sesion'] = df['Dt_WebVisit']
df_traducido['Origen_Trafico'] = df['Traffic_Source'].map(traduccion_source)
df_traducido['Medio_Trafico'] = df['Traffic_Medium'].map(traduccion_medium)
df_traducido['Tipo_Dispositivo'] = df['Device_Type'].map(traduccion_device)

# 2. Mantener las columnas numéricas igual
df_traducido['Num_Paginas_Vistas'] = df['NumPageViews']
df_traducido['Indicador_Rebote'] = df['Bounce_Flag'].map({0: 'Sin rebote', 1: 'Con rebote'})
df_traducido['Productos_Vistos'] = df['Viewed_Product']
df_traducido['Agregados_Carrito'] = df['Added_To_Cart']
df_traducido['Inicios_Checkout'] = df['Started_Checkout']
df_traducido['Compras_Completadas'] = df['Purchase_Completed']
df_traducido['Ingresos'] = df['Revenue']
df_traducido['Num_Transacciones'] = df['NumTransactions']

# 🔥 EXTRA: Reemplazar TODOS los " / " por " & " en TODAS las columnas de texto
print("\n🔄 Reemplazando ' / ' por ' & ' en todas las columnas...")
for columna in df_traducido.select_dtypes(include=['object', 'string']).columns:
    df_traducido[columna] = df_traducido[columna].str.replace(' / ', ' & ', regex=False)
    print(f"   ✅ Columna '{columna}' procesada")

# Guardar el archivo traducido
df_traducido.to_csv(ruta_destino, index=False, encoding='utf-8-sig')

print(f"\n✅ Archivo traducido guardado en: {ruta_destino}")
print("-"*80)

# Mostrar un ejemplo de cómo quedó
print("\n📋 EJEMPLO DE DATOS TRADUCIDOS (primeras 5 filas):")
print("="*80)
print(df_traducido.head(5).to_string())
print("="*80)

# Verificar que no hay columnas duplicadas
print(f"\n📊 Total de columnas en el archivo traducido: {len(df_traducido.columns)}")
print("📋 Columnas:")
for col in df_traducido.columns:
    print(f"   • {col}")

# Resumen de las traducciones
print("\n" + "="*80)
print("📊 RESUMEN DE TRADUCCIONES APLICADAS:")
print("-"*80)

print("\n🌐 TRAFFIC_SOURCE → ORIGEN_TRÁFICO:")
for portugues, espanol in traduccion_source.items():
    print(f"   {portugues} → {espanol}")

print("\n📱 TRAFFIC_MEDIUM → MEDIO_TRÁFICO:")
for portugues, espanol in traduccion_medium.items():
    print(f"   {portugues} → {espanol}")

print("\n💻 DEVICE_TYPE → TIPO_DISPOSITIVO:")
for portugues, espanol in traduccion_device.items():
    print(f"   {portugues} → {espanol}")

print("\n🔄 BOUNCE_FLAG → INDICADOR_REBOTE:")
print("   0 → Sin rebote")
print("   1 → Con rebote")

print("\n" + "="*80)
print("✅ ¡Traducción completada con éxito!")
print("="*80)