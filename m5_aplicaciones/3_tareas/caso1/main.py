import pandas as pd

# Cargar el dataset traducido
df = pd.read_csv('2/digital_funnel_clean_ES.csv')

# Crear columna combinada de Fuente/Medio
df['Origen_Medio'] = df['Origen_Trafico'] + ' / ' + df['Medio_Trafico']

# =================================================================
# PREGUNTA 1: ¿Qué fuente o medio trae tráfico de mejor calidad?
# =================================================================
print("PREGUNTA 1: ¿Qué fuente o medio trae tráfico de mejor calidad?")
print("-" * 60)

# Definimos calidad usando tasa de rebote (menor es mejor), páginas vistas (mayor es mejor) y tasa de compra (mayor es mejor)
calidad = df.groupby('Origen_Medio').agg(
    Sesiones=('ID_Sesion_Web', 'count'),
    Tasa_Rebote=('Indicador_Rebote', lambda x: (x == 'Con rebote').mean()),
    Promedio_Paginas=('Num_Paginas_Vistas', 'mean'),
    Tasa_Compra=('Compras_Completadas', lambda x: (x > 0).mean())
)

# Filtramos fuentes con más de 50 sesiones para evitar sesgos
calidad_filtrada = calidad[calidad['Sesiones'] > 50].sort_values(by='Tasa_Compra', ascending=False)
print(calidad_filtrada.head(10))

# =================================================================
# PREGUNTA 2: ¿En qué etapa del embudo ocurre la mayor caída?
# =================================================================
print("\nPREGUNTA 2: ¿En qué etapa del embudo ocurre la mayor caída?")
print("-" * 60)

total_sesiones = len(df)
viewed = df['Productos_Vistos'].sum()
added = df['Agregados_Carrito'].sum()
checkout = df['Inicios_Checkout'].sum()
purchase = df['Compras_Completadas'].sum()

embudo = pd.DataFrame({
    'Etapa': ['1. Sesion', '2. Ver Producto', '3. Agregar Carrito', '4. Iniciar Checkout', '5. Compra'],
    'Usuarios': [total_sesiones, viewed, added, checkout, purchase]
})

embudo['% Conversion Total'] = (embudo['Usuarios'] / total_sesiones) * 100
embudo['% Caida vs Etapa Anterior'] = (1 - (embudo['Usuarios'] / embudo['Usuarios'].shift(1).fillna(total_sesiones))) * 100
print(embudo.to_string(index=False))

# =================================================================
# PREGUNTA 3: ¿Hay diferencias relevantes entre dispositivos?
# =================================================================
print("\nPREGUNTA 3: ¿Hay diferencias relevantes entre dispositivos?")
print("-" * 60)

dispositivos = df.groupby('Tipo_Dispositivo').agg(
    Sesiones=('ID_Sesion_Web', 'count'),
    Tasa_Rebote=('Indicador_Rebote', lambda x: (x == 'Con rebote').mean()),
    Tasa_Compra=('Compras_Completadas', lambda x: (x > 0).mean()),
    Paginas_Promedio=('Num_Paginas_Vistas', 'mean')
)
dispositivos['% Del Trafico Total'] = (dispositivos['Sesiones'] / total_sesiones) * 100
print(dispositivos)

# =================================================================
# PREGUNTA 4: ¿Qué indicador muestra con mayor claridad la principal fricción?
# =================================================================
print("\nPREGUNTA 4: ¿Qué indicador muestra con mayor claridad la principal friccion?")
print("-" * 60)

tasa_rebote = (df['Indicador_Rebote'] == 'Con rebote').mean() * 100
abandono_sin_ver = (1 - (viewed / total_sesiones)) * 100
abandono_carrito = (1 - (added / viewed)) * 100 if viewed > 0 else 0
abandono_checkout = (1 - (checkout / added)) * 100 if added > 0 else 0
abandono_pago = (1 - (purchase / checkout)) * 100 if checkout > 0 else 0

print(f"1. Tasa de Rebote: {tasa_rebote:.2f}%")
print(f"2. Abandono sin ver producto: {abandono_sin_ver:.2f}%")
print(f"3. Abandono en Carrito (Vio pero no agrego): {abandono_carrito:.2f}%")
print(f"4. Abandono en Checkout (Agrego pero no inicio checkout): {abandono_checkout:.2f}%")
print(f"5. Abandono en Pago (Inicio checkout pero no compro): {abandono_pago:.2f}%")

# =================================================================
# PREGUNTA 5: ¿Qué acción concreta recomendarían para mejorar la conversión?
# =================================================================
print("\nPREGUNTA 5: ¿Qué acción concreta recomendarían para mejorar la conversión?")
print("-" * 60)

caidas = [
    (abandono_sin_ver, "Optimizar el buscador interno, mejorar el catalogo inicial y aumentar la velocidad de carga de la web."),
    (abandono_carrito, "Mejorar las fichas de producto con fotos, reseñas, precios claros y boton de agregar al carrito mas visible."),
    (abandono_checkout, "Reducir los pasos para llegar al checkout, evitar costos de envio sorpresa y agregar boton de compra rapida."),
    (abandono_pago, "Simplificar el formulario de pago, ofrecer multiples metodos de pago y asegurar que la pasarela de pago funcione correctamente.")
]

mejor_accion = max(caidas, key=lambda x: x[0])
print(f"Accion recomendada: {mejor_accion[1]}")

# =================================================================
# PREGUNTA FINAL: ¿Qué está fallando antes de la compra y cómo lo demostrarían con datos del embudo?
# =================================================================
print("\nPREGUNTA FINAL: ¿Qué está fallando antes de la compra y como lo demostrarian con datos del embudo?")
print("-" * 60)

# Identificar la mayor caída del embudo
mayor_caida_idx = embudo['% Caida vs Etapa Anterior'].idxmax()
mayor_caida_etapa = embudo.loc[mayor_caida_idx, 'Etapa']
mayor_caida_valor = embudo.loc[mayor_caida_idx, '% Caida vs Etapa Anterior']

print(f"La mayor caida ocurre en la etapa: {mayor_caida_etapa}")
print(f"Con una caida del {mayor_caida_valor:.2f}% de los usuarios.")

# Analizar el comportamiento antes de la compra
usuarios_con_version = df[df['Productos_Vistos'] > 0]
usuarios_con_carrito = df[df['Agregados_Carrito'] > 0]
usuarios_con_checkout = df[df['Inicios_Checkout'] > 0]

print(f"\nEvidencia del problema:")
print(f"- {len(usuarios_con_version):,} usuarios vieron productos")
print(f"- {len(usuarios_con_carrito):,} usuarios agregaron al carrito")
print(f"- {len(usuarios_con_checkout):,} usuarios iniciaron checkout")
print(f"- {purchase:,} compras completadas")

# Calcular ratios de conversión entre etapas
ratio_vista_carrito = len(usuarios_con_carrito) / len(usuarios_con_version) if len(usuarios_con_version) > 0 else 0
ratio_carrito_checkout = len(usuarios_con_checkout) / len(usuarios_con_carrito) if len(usuarios_con_carrito) > 0 else 0
ratio_checkout_compra = purchase / len(usuarios_con_checkout) if len(usuarios_con_checkout) > 0 else 0

print(f"\nRatios de conversion:")
print(f"- Vista → Carrito: {ratio_vista_carrito * 100:.2f}%")
print(f"- Carrito → Checkout: {ratio_carrito_checkout * 100:.2f}%")
print(f"- Checkout → Compra: {ratio_checkout_compra * 100:.2f}%")

# Identificar el cuello de botella principal
cuellos_botella = {
    'Vista → Carrito': ratio_vista_carrito,
    'Carrito → Checkout': ratio_carrito_checkout,
    'Checkout → Compra': ratio_checkout_compra
}

peor_ratio = min(cuellos_botella, key=cuellos_botella.get)
print(f"\nEl mayor cuello de botella es: {peor_ratio}")
print(f"Donde se pierde el {(1 - cuellos_botella[peor_ratio]) * 100:.2f}% de los usuarios.")