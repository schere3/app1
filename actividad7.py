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


# --- FUNCIONES DE CARGA DE DATOS ---
def pagina_principal():
    st.title("Modelización Predictiva")
    st.write("Estamos antes la página principal de nuestro estudio")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    # Todo el contenido Markdown debe ir entre comillas triples dentro de st.markdown
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    
    # Todo el contenido Markdown debe ir entre comillas triples dentro de st.markdown
    st.markdown("""
    ## Índice
    1. [Introducción](#introducción)
    2. [Requisitos Previos](#requisitos-previos)
    3. [Instalación y Configuración](#instalación-y-configuración)
    4. [Ir a Visualización de Datos](otra-pagina.md#requisitos-previos)
    ---
    ## Introducción
    Aquí va tu texto de introducción...
    
    ## Requisitos Previos
    Aquí los requisitos...
    
    ## Instalación y Configuración
    Pasos de instalación...
    """)
    
def visualizar_datos():
    st.title("Análisis de Robustez")
    st.write("Carga un archivo CSV para visualizar los datos.")
    archivo_cargado = st.file_uploader("Elige un archivo CSV", type="csv")

    if archivo_cargado is not None:
        df = pd.read_csv(archivo_cargado)
        st.write("Datos del archivo csv:")
        st.write(df)
        st.write("Estadísticas descriptivas")
        st.write(df.describe())

# menu para llamar a la funcion
st.sidebar.title("Navegación")
pagina1 = st.sidebar.selectbox("Selecciona una página", ["Página Principal", 
                                                        "Visualización de Datos"])
if pagina1 == "Página Principal":
    pagina_principal()
elif pagina1 == "Visualización de Datos":
    visualizar_datos()
