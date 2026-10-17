# Calculadora de Biomasa y Biogás

## Descripción

Este proyecto consiste en una aplicación web desarrollada en Python que permite calcular la cantidad de biomasa disponible y estimar la producción de biogás a partir de residuos orgánicos de origen animal.

La calculadora está orientada a la Ingeniería de la Energía y busca demostrar cómo la programación puede utilizarse para analizar el aprovechamiento energético de la biomasa.

## Objetivo

Desarrollar una aplicación interactiva que permita estimar la producción diaria de biogás y su potencial energético mediante cálculos matemáticos implementados en Python.

## Funcionalidades

- Ingresar cantidades de estiércol de cuyes, cerdos y vacas.
- Calcular la biomasa total disponible en kg/día.
- Estimar la producción diaria de biogás en litros y metros cúbicos.
- Calcular el potencial energético térmico en kWh/día.
- Modificar los rendimientos estimados de biogás.
- Visualizar los resultados automáticamente al ejecutar el cálculo.

## Tecnologías utilizadas

**Python:** lenguaje de programación empleado para desarrollar los cálculos.

**Streamlit:** biblioteca utilizada para crear la interfaz interactiva de la aplicación web.

**GitHub:** plataforma utilizada para almacenar y compartir el código fuente.

**Streamlit Community Cloud:** servicio previsto para publicar la aplicación en internet.

## Fórmulas utilizadas

### Biomasa total

Biomasa total = Biomasa de cuyes + Biomasa de cerdos + Biomasa de vacas.

### Producción de biogás

Biogás total = Σ (masa diaria de cada residuo × rendimiento específico).

### Conversión a litros

Biogás (L/día) = Biogás (m³/día) × 1000.

### Potencial energético

Energía (kWh/día) = Biogás (m³/día) × Poder calorífico (kWh/m³).

Los rendimientos iniciales son valores ilustrativos ajustables. Los resultados representan estimaciones teóricas y no sustituyen un análisis experimental de la biomasa.

## Archivos del proyecto

- **app.py:** programa principal desarrollado en Python.
- **requirements.txt:** contiene las dependencias necesarias para ejecutar la aplicación.
- **README.md:** documentación del proyecto.

## Ejecución del programa

Para ejecutar el proyecto localmente se necesita Python y las bibliotecas indicadas en requirements.txt.

Instalar las dependencias:

`pip install -r requirements.txt`

Ejecutar la aplicación:

`streamlit run app.py`

La aplicación se abrirá en el navegador web.

## Importancia en Ingeniería de la Energía

El proyecto permite relacionar los conocimientos de programación con el aprovechamiento de energías renovables, especialmente la conversión de residuos orgánicos en biogás mediante digestión anaerobia.

## Autor

**LeonelPortocarrero**

Proyecto académico de Lenguaje de Programación — Ingeniería de la Energía.

