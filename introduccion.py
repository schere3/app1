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
st.info("En esta sección se dividen las tareas realizadas por bloques.")
# --- BLOQUE 1 ---
with st.expander("🤖  Bloque I: IA y Gestión de la Información.", expanded=True):
    st.markdown("""
    1. **Extracción y Limpieza:** Consolidación de fuentes de datos provenientes de los servicios operativos de GSC.
    2. **Tratamiento de Nulos:** Aplicación de técnicas estadísticas para la imputación de valores faltantes en las bases de datos.
    """)

# --- BLOQUE 2 ---
with st.expander("📊 Bloque II: Ciencia de Datos."):
    st.markdown("""
    1. **Análisis Descriptivo:** Cálculo de métricas de tendencia central y dispersión de los tiempos de respuesta.
    2. **Visualización de Datos:** Creación de gráficos interactivos con *Matplotlib* y *Seaborn* para identificar patrones.
    3. **Detección de Outliers:** Identificación de casos atípicos en los servicios de urgencias para mejorar la precisión del modelo.
    """)

# --- BLOQUE 3 ---
with st.expander("🤖 Bloque III: Business Intelligence, Modelización Predictiva y Despliegue de Soluciones."):
    st.markdown("""
    1. **Selección de Características:** Uso de *scikit-learn* para identificar las variables más influyentes en el flujo de datos.
    2. **Entrenamiento de Modelos:** Implementación de algoritmos de regresión/clasificación para predecir demanda de servicios.
    3. **Evaluación de Resultados:** Validación cruzada y cálculo de error para medir la fiabilidad de las conclusiones.
    4. **Generación de Reportes:** Automatización del informe final de resultados mediante el uso de herramientas computacionales.
    """)

# Nota visual para cerrar la sección
st.divider()