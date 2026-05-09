import streamlit as st

# Título principal de la aplicación
st.title("Memoria de Experiencia Formativa")

# --- SECCIÓN 1: INTRODUCCIÓN ---
st.header("1. Introducción")
st.write("""
La presente memoria resume la experiencia formativa desarrollada en la empresa pública 
**Gestión de Servicios para la Salud y Seguridad en Canarias (GSC)**.
""")

# 1.1. Descripción de la empresa
st.subheader("1.1. Descripción de la empresa")
st.write("""
La estancia formativa se desarrolló en **GSC**, empresa pública instrumental que depende de la 
Consejería de Sanidad del Gobierno de Canarias, cuya función es la gestión, operación y coordinación 
ágil de servicios esenciales de salud, seguridad y emergencias. 

**Servicios operativos clave gestionados:**
* Servicio de Urgencias Canario (SUC)
* Centro Coordinador de Emergencias y Seguridad (CECOES) 1-1-2
* Transporte Sanitario No Urgente (TSNU)
* Servicio de Atención a Mujeres Víctimas de Violencia de Género
* Línea de información sobre el Coronavirus
* Farmacovigilancia y Facturación del Servicio Canario de la Salud
""")

# 1.2. Periodo y departamentos
st.subheader("1.2. Periodo y departamentos donde se realizaron")
st.markdown("""
- **Calendario:** Del 17 de enero al 13 de mayo de 2026 (~4 meses).
- **Asistencia:** Regular de tres días por semana (lunes, miércoles y viernes).
- **Unidad:** Unidad de Control y Servicios Generales (División Económica, Control y Servicios Generales del GSC).
""")

# 1.3. Objetivos
st.subheader("1.3. Objetivos planteados")
st.markdown("""
* **Sector Público:** Comprender el funcionamiento, estructura organizativa y régimen laboral.
* **Perfil Profesional:** Explorar salidas profesionales para definir el perfil técnico.
* **Integración Académica:** Aplicar conceptos matemáticos y computacionales del Grado en Matemáticas en un entorno laboral real mediante el flujo de análisis de datos.
""")

# --- SECCIÓN 2: DESARROLLO ---
st.header("2. Desarrollo y resultados")

st.subheader("2.1. Tareas y actividades realizadas.")
st.write("En esta sección se dividen las tareas realizadas por bloques.")
# --- BLOQUE 1 ---
with st.expander("🤖  Bloque I: IA y Gestión de la Información.", expanded=True):
    st.markdown("""
    1. **Optimización de gestión documental mediante NotebookLM:** Con el objetivo de optimizar el análisis de gran cantidad de información, se llevó a cabo una investigación técnica sobre la herramienta NotebookLM. El proceso incluyó una fase de curación de datos y pruebas de rendimiento en la organización de fuentes de información. La actividad concluyó con una sesión de transferencia de conocimiento ante el tutor externo y la compañera de prácticas del momento.
    2. **Análisis Análisis comparativo de modelos de Inteligencia Artificial:** Con el fin de analizar el ecosistema tecnológico actual y determinar las capacidades diferenciales de cada inteligencia artificial, se procede a categorizarlas. La actividad concluyó con la presentación de un informe técnico donde se detallaron las ventajas competitivas de cada herramienta.
    """)

# --- BLOQUE 2 ---
with st.expander("📊 Bloque II: Ciencia de Datos."):
    st.markdown("""
    3. **Microcredencial certificada:** Se completó con éxito la Microcredencial universitaria en Introducción al Machine Learning por la Universidad de La Laguna (ULL). Esta formación proporcionó las bases matemáticas y algorítmicas necesarias para el desarrollo de soluciones basadas en aprendizaje supervisado y no supervisado.
    4. **Proyecto 1:** Creación de gráficos interactivos con *Matplotlib* y *Seaborn* para identificar patrones.
    5. **Proyecto Final:** Identificación de casos atípicos en los servicios de urgencias para mejorar la precisión del modelo.
    """)

# --- BLOQUE 3 ---
with st.expander("🤖 Bloque III: Business Intelligence, Modelización Predictiva y Despliegue de Soluciones."):
    st.markdown("""
    6. **Formación avanzada en Microsoft Power BI (Santander Open Academy):** Se adquirieron capacidades en arquitectura de datos (ETL) y modelado, con un enfoque práctico en la creación de cuadros de mando interactivos. Esto permite convertir datos brutos en información estratégica, mejorando la eficiencia y claridad en la presentación de resultados para la gestión pública.
    7. **Modelización predictiva y análisis de robustez del consumo energético:** Implementación de algoritmos de regresión/clasificación para predecir demanda de servicios.e desarrolló un estudio predictivo sobre el consumo y gasto eléctrico de las plantas del GSC empleando técnicas de Machine Learning (librería Prophet) orientadas a series temporales. El objetivo central fue generar proyecciones del 2026, partiendo de los datos históricos de 2024 y 2025, con el fin de facilitar la detección de tendencias. Para validar la precisión del modelo, se implementó un proceso de verificación utilizando datos históricos de 2023 para comparar las estimaciones generadas por el algoritmo con los registros reales obtenidos en 2025. Adicionalmente, se realizó un ejercicio de simulación mediante la generación de datos sintéticos mediante inteligencia artificial (con una profundidad retroactiva de 10 años) para evaluar el comportamiento del modelo frente a distintos volúmenes de datos. Este proceso de validación garantizó la fiabilidad y solidez de las predicciones resultantes.
    8. **Diseño de un cuadro de mando (Dashboard) en Power BI:** Esta herramienta permite monitorizar de forma dinámica el gasto energético y las previsiones calculadas en la Actividad 7, facilitando una lectura ejecutiva de los datos. El proyecto finalizó con una presentación ante el tutor externo.
    9. **Desarrollo y despliegue web de resultados técnicos:** Se llevó a cabo una labor de autoformación en tecnologías de despliegue web y control de versiones. Mediante el uso del framework Streamlit, se desarrolló una interfaz interactiva alojada en GitHub, que consolida y expone de forma dinámica los resultados de las actividades 7 y 8.
    """)

# Nota visual para cerrar la sección
st.divider()
