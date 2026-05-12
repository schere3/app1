import streamlit as st

st.title("Modelización Predictiva y Análisis de Robustez")
st.subheader("Consumo Energético: Proyecciones 2026")

# Sección de Contexto
st.markdown("""
### 📊 Descripción del Proyecto
Este análisis emplea técnicas de **Machine Learning (ML)** sobre series temporales de gasto eléctrico correspondientes a los periodos **2024-2025**. El objetivo es modelar el comportamiento histórico para generar predicciones precisas hacia el año 2026.
""")

# Sección de Robustez con mejores elementos visuales
st.markdown("### 🛡️ Análisis de Robustez del Modelo")
st.write("Para garantizar la fiabilidad de las predicciones, se han implementado los siguientes protocolos de validación:")

# Usar columnas o una lista con mejor formato
st.info("""
1. **Backtesting (2023-2024):** Se entrenó el modelo con datos históricos previos para predecir el año 2025 y comparar los resultados con los datos reales, validando la precisión del algoritmo.
2. **Pruebas con Datos Sintéticos:** Generación de una serie temporal de 10 años para evaluar la estabilidad del modelo a largo plazo y contrastar la coherencia de la predicción 2026.
""")
