# Proyecto de BI Predictivo: Análisis y predicción de churn de Telco

## ¿Qué es este proyecto?

Este proyecto tiene como objetivo identificar clientes con alta probabilidad de abandonar un servicio de telecomunicaciones (churn) y convertir ese conocimiento en información útil para tomar decisiones de negocio. La idea principal es entender por qué los clientes se van y, a partir de eso, construir un modelo predictivo que ayude a anticipar fugas y diseñar acciones de retención más efectivas.

Los datos usados para este análisis provienen del dataset de Kaggle: https://www.kaggle.com/datasets/blastchar/telco-customer-churn. Allí encontramos información realista sobre clientes de una empresa de telecomunicaciones, lo que nos permite trabajar con un problema muy común en el mundo de los negocios: la pérdida de clientes.

## Lógica del proyecto

El flujo del proyecto se puede resumir en cuatro pasos principales:

1. Recolección y preparación de datos
   - Se utiliza un dataset de clientes de telecomunicaciones con variables como antigüedad, contrato, cargos mensuales, servicio de internet y estado de churn.
   - Se limpia la información para dejarla lista para análisis y modelado.
   - Se eliminan columnas que no aportan valor predictivo y se corrigen valores inconsistentes.

2. Análisis exploratorio de datos (EDA)
   - Se estudian patrones y relaciones entre las variables.
   - Se revisa cómo se distribuye la variable objetivo y qué factores están asociados con la fuga de clientes.
   - Se buscan insights de negocio que permitan explicar el problema de forma más clara.

3. Construcción de modelos predictivos
   - Se separa la información en conjuntos de entrenamiento y prueba.
   - Se entrenan modelos de clasificación para predecir si un cliente probablemente se va o no.
   - Se evalúan con métricas como precisión, sensibilidad, ROC-AUC y matriz de confusión.

4. Interpretación y comunicación de resultados
   - Se analizan las variables más importantes del modelo.
   - Se preparan hallazgos que pueden servir para campañas de retención, segmentación de clientes y decisiones estratégicas.
   - Se documenta el trabajo en un reporte y en un notebook para que sea fácil de revisar.

## ¿Qué estamos haciendo exactamente?

Estamos combinando dos enfoques:

- Business Intelligence: entender el comportamiento de los clientes y detectar patrones de fuga.
- Modelos predictivos: anticipar qué clientes tienen mayor riesgo de abandonar el servicio.

Esto permite pasar de un análisis descriptivo a una propuesta más accionable para la empresa.

## Estructura del repositorio

El proyecto está organizado de forma sencilla para separar las distintas etapas del flujo de trabajo:

```text
.
├── data/
│   ├── raw/                # Dataset original descargado o cargado desde la fuente
│   └── processed/          # Datos limpios y listos para análisis y modelado
├── documents/             # Materiales o documentos de apoyo del proyecto
├── notebooks/             # Notebook principal con el análisis exploratorio y los modelos
├── report_latex/          # Archivos fuente para generar el reporte en LaTeX
├── requirements.txt       # Dependencias de Python del proyecto
└── README.md              # Documentación general del proyecto
```

### Descripción de las carpetas

- data/raw/: contiene los archivos fuente originales del dataset, antes de cualquier limpieza.
- data/processed/: almacena la información ya transformada, preparada y lista para usar en análisis predictivos.
- notebooks/: incluye el notebook principal donde se desarrolla la lógica del proyecto, desde la carga de datos hasta la evaluación de modelos.
- documents/: sirve como espacio para documentos auxiliares, referencias o entregables complementarios.
- report_latex/: guarda los archivos necesarios para generar una versión formal del proyecto en formato LaTeX.
- requirements.txt: define las librerías y versiones necesarias para reproducir el entorno de trabajo.

## Autores

Este proyecto fue desarrollado por los estudiantes:

- ILIAN JOSEPH FELIPEZ VACA
- MARCELO FAVIO NINA CALSINA
- PAOLA MELANI QUISPE MAMANI
- MIGUEL ANGEL MOLLERICONA CUENTAS

## Requisitos

Para ejecutar este proyecto se recomienda usar Python y las librerías listadas en requirements.txt.

### Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo trabajar con el proyecto

1. Abrir el notebook en la carpeta notebooks.
2. Ejecutar las celdas para cargar, limpiar y analizar los datos.
3. Revisar los resultados del modelo y los insights generados.
4. Usar el reporte en LaTeX como soporte para la presentación final del proyecto.

## Objetivo de negocio

El objetivo final no es solo predecir churn, sino ayudar a la organización a actuar antes de que los clientes se vayan. Con esta información, se pueden diseñar estrategias de retención más precisas y enfocadas.
