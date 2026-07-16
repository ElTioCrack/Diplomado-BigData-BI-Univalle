import pandas as pd

# Crear el diccionario traducido
diccionario_traducido = pd.DataFrame({
    'Nombre_Columna': [
        'ID_Cliente_Digital',
        'ID_Sesion_Web',
        'Fecha_Sesion',
        'Origen_Trafico',
        'Medio_Trafico',
        'Tipo_Dispositivo',
        'Num_Paginas_Vistas',
        'Indicador_Rebote',
        'Productos_Vistos',
        'Agregados_Carrito',
        'Inicios_Checkout',
        'Compras_Completadas',
        'Ingresos',
        'Num_Transacciones'
    ],
    'Tipo': [
        'uint64',
        'int64',
        'Fecha',
        'Texto',
        'Texto',
        'Texto',
        'float',
        'int',
        'int',
        'int',
        'int',
        'int',
        'float',
        'int'
    ],
    'Descripcion': [
        'Identificador único del visitante. Un mismo usuario puede aparecer en varias sesiones.',
        'Identificador único de la sesión de navegación. Cada registro corresponde a una sesión.',
        'Fecha en la que ocurrió la sesión (formato DD/MM/YYYY).',
        'Origen del tráfico desde el cual llegó el usuario al sitio web (Directo, Orgánico, YouTube, Redes Sociales, Afiliados, Email, Otros sitios).',
        'Medio de adquisición asociado al origen del tráfico (Ninguno, Orgánico, Recomendación, Afiliado, CPC/Búsqueda pagada, CPM/Display).',
        'Tipo de dispositivo utilizado durante la sesión (Escritorio, Móvil o Tableta).',
        'Número total de páginas visualizadas durante la sesión. Puede tomar valores altos cuando el usuario navega intensamente (máximo observado: 466).',
        'Indicador de rebote. 1 = sesión con rebote, 0 = sesión sin rebote. Traducido como "Con rebote" / "Sin rebote".',
        'Cantidad de eventos de visualización de productos registrados durante la sesión. Un usuario puede visualizar múltiples productos.',
        'Cantidad de eventos "Agregar al carrito" registrados durante la sesión. Un usuario puede añadir varios productos.',
        'Cantidad de eventos de inicio del proceso de checkout registrados durante la sesión. Puede ser mayor que uno cuando existen múltiples intentos.',
        'Cantidad de eventos de compra registrados durante la sesión. Una misma sesión puede registrar varios eventos de compra.',
        'Ingreso generado durante la sesión como resultado de las transacciones. Su valor es acumulado por sesión.',
        'Contador de transacciones de comercio electrónico registradas durante la sesión. Una sesión puede contener varias transacciones/productos.'
    ]
})

# Guardar el diccionario traducido
diccionario_traducido.to_csv('2/diccionario_datos_TRADUCIDO.csv', index=False, encoding='utf-8-sig')

print("="*80)
print("📚 DICCIONARIO DE DATOS TRADUCIDO")
print("="*80)
print(diccionario_traducido.to_string(index=False))
print("="*80)
print(f"\n✅ Diccionario guardado en: 2/diccionario_datos_TRADUCIDO.csv")