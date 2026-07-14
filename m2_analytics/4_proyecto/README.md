# Análisis de Clustering de Perfiles Musicales

## Descripción del Proyecto

Este proyecto implementa un análisis exhaustivo de agrupamiento de perfiles musicales mediante técnicas de aprendizaje no supervisado. A través de la aplicación de algoritmos de clustering como K-Means y DBSCAN, se busca identificar patrones inherentes en características musicales y agrupar canciones con perfiles similares.

## Objetivos

- Adquirir y preparar un conjunto de datos de canciones populares de Spotify.
- Realizar un análisis exploratorio completo de las características musicales.
- Implementar algoritmos de clustering (K-Means y DBSCAN) para identificar grupos homogéneos.
- Comparar la efectividad de diferentes métodos de agrupamiento.
- Documentar los hallazgos en un informe formal según estándares IEEE.

## Estructura del Proyecto

- `data/`
  - Almacena los datos crudos y procesados utilizados en el análisis.
  - `data/raw/`: datos originales sin limpiar.
  - `data/processed/`: datos transformados, muestreados y escalados para el modelado.
  - **Nota:** los conjuntos de datos completos no están incluidos aquí porque superan los 100 MB y no se pueden subir a GitHub.
    Para reproducir el proyecto, puede obtener los datos desde:
    [Dataset en Kaggle](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/data)

- `docs/`
  - Contiene la documentación del proyecto y el informe en formato IEEE.
  - `docs/main.tex`: archivo principal de LaTeX del informe.
  - `docs/main.pdf`: versión final del informe en formato IEEE.
  - `docs/references.bib`: bibliografía del informe.
  - `docs/figures/`: figuras y gráficos usados en el documento.
  - `docs/sections/`: secciones del informe organizadas por temas.

- `notebooks/`
  - Notebooks de Jupyter que documentan el flujo completo del análisis de clustering.
  - `01_adquisicion_dataset.ipynb`: adquisición y exploración inicial del dataset.
  - `02_preprocesamiento.ipynb`: limpieza y transformación de datos.
  - `03_eda.ipynb`: análisis exploratorio de datos (EDA).
  - `04_muestreo_escalado.ipynb`: muestreo y escalado de características.
  - `05_K-Means.ipynb`: análisis usando el algoritmo K-Means.
  - `06_DBSCAN.ipynb`: análisis usando el algoritmo DBSCAN.

- `requirements.txt`: Lista de dependencias necesarias para la reproducibilidad del proyecto.

## Requisitos de Instalación

Para ejecutar este proyecto, se requiere Python 3.7 o superior. Instale las dependencias utilizando:

```bash
pip install -r requirements.txt
```

## Flujo de Análisis

El proyecto sigue un flujo estructurado y secuencial que va desde la adquisición de datos hasta la evaluación de modelos:

1. **Adquisición del Dataset** (`01_adquisicion_dataset.ipynb`): Obtención y exploración inicial del conjunto de datos de Spotify.
2. **Preprocesamiento** (`02_preprocesamiento.ipynb`): Limpieza de valores faltantes, eliminación de duplicados y transformación de variables.
3. **Análisis Exploratorio de Datos** (`03_eda.ipynb`): Visualización y caracterización estadística de las características musicales.
4. **Muestreo y Escalado** (`04_muestreo_escalado.ipynb`): Reducción de datos y normalización de características para el modelado.
5. **Modelado con K-Means** (`05_K-Means.ipynb`): Implementación y evaluación del algoritmo K-Means con optimización de hiperparámetros.
6. **Modelado con DBSCAN** (`06_DBSCAN.ipynb`): Implementación y evaluación del algoritmo DBSCAN con análisis comparativo.

## 📌 Enlaces importantes

| Recurso | Enlace |
|---------|--------|
| **Informe IEEE (PDF)** | [`docs/main.pdf`](https://github.com/ElTioCrack/musical-profile-clustering-spotify/blob/main/docs/main.pdf) |
| **Presentación del proyecto** | [Canva - Presentación](https://www.canva.com/design/DAHIGgBrhUQ/22gKk63En8oZHxa3BO7ZWw/edit) |
| **Dataset original** | [Kaggle - Top Spotify Songs](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated/data) |
| **Repositorio GitHub** | [musical-profile-clustering-spotify](https://github.com/ElTioCrack/musical-profile-clustering-spotify) |

---

## 👥 Integrantes del equipo

- Felipez, Ilian
- Mollericona, Miguel
- Nina, Marcelo
- Quispe, Paola
- Tintaya, Eugenia

---

*Proyecto realizado para la asignatura de Ciencia de Datos - IEEE format*