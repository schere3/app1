import streamlit as st

st.title("Optimización documental con NotebookLM")
# Configuración de la página
st.set_page_config(
    page_title="Presentación NotebookLM - Scherezade",
    page_icon="📚",
    layout="centered"
)

# Estilos personalizados para mejorar la estética
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMarkdown h1 {
        color: #1E88E5;
        text-align: center;
    }
    .highlight-box {
        background-color: #e3f2fd;
        padding: 20px;
        border-left: 5px solid #1E88E5;
        border-radius: 5px;
        margin: 10px 0;
    }
    .quote {
        font-style: italic;
        font-size: 1.2em;
        text-align: center;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INICIO DEL DISCURSO ---

# Introducción
st.title("NotebookLM: De la Infoxicación al Conocimiento")
st.subheader("Presentado por: Scherezade")

st.markdown("---")

col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://www.gstatic.com/lamda/images/favicon_v1_150160d13988654cbfd5.png", width=100)
with col2:
    st.write("### ¡Buenos días!")
    if st.button("Lanzar pregunta al público"):
        st.info("¿Quién de ustedes NO ha usado inteligencia artificial alguna vez para estudiar, investigar o trabajar?")

# El problema: Infoxicación
st.markdown('<p class="quote">"Hoy en día se dice que tenemos el conocimiento del mundo al alcance de nuestra mano..."</p>', unsafe_allow_html=True)

with st.expander("Pero, seamos honestos: ¿Qué hay realmente detrás de esa abundancia?"):
    st.write("""
    Existe un término, acuñado por **Alfons Cornella**, denominado fenómeno de la **infoxicación**. 
    Es la sobrecarga informativa que nuestro cerebro difícilmente puede procesar:
    - Páginas web desactualizadas.
    - Noticias mal contrastadas.
    - Bombardeo de anuncios.
    - Algoritmos que solo buscan retenernos en pantalla.
    """)

st.warning("Estamos pasando de la era de **'Buscar'** (Google) a la era de **'Sintetizar'** (IA Generativa).")

# La Solución: NotebookLM
st.markdown("---")
st.header("🎯 La Respuesta: NotebookLM")
st.write("""
Es la herramienta de investigación y toma de notas de Google potenciada por **Gemini Pro**. 
Su diferencia crucial es el **Grounding (Anclaje)**.
""")

st.info("**Grounding:** La IA razona limitándose estrictamente a los documentos que TÚ le proporcionas.")

# Metáfora visual
st.markdown("""
<div class="highlight-box">
    <strong>Imagina esto:</strong> Es como si le entregaras una pila de 50 libros a la persona más inteligente del mundo y le dijeras: 
    <em>"Léete todo esto en 10 segundos y conviértete en el mayor experto sobre este tema".</em>
</div>
""", unsafe_allow_html=True)

# Funcionalidades
st.markdown("---")
st.header("🛠️ ¿Cómo funciona?")
tabs = st.tabs(["Proceso", "Funciones Especiales", "Aplicaciones"])

with tabs[0]:
    st.steps([
        "Entras y creas un cuaderno.",
        "Subes tus PDFs, textos o enlaces.",
        "La IA se convierte en un experto instantáneo."
    ])
    st.success("Cero alucinaciones externas: Solo sabe lo que tú le has dado.")

with tabs[1]:
    st.write("NotebookLM va mucho más allá de un simple chat:")
    st.markdown("""
    - 🎙️ **Audio Overview:** Convierte tus documentos en un podcast con dos locutores.
    - 📝 **Guías de estudio:** Genera cuestionarios y resúmenes estructurados.
    - 💡 **Preguntas específicas:** Cita directamente la fuente en el documento.
    """)

with tabs[2]:
    st.subheader("Tres bloques clave:")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("**1. Foco y Eficiencia**")
        st.caption("Elimina el ruido. Ideal para exámenes u oposiciones.")
    with col_b:
        st.markdown("**2. Análisis Profundo**")
        st.caption("Cruza datos entre documentos: ¿En qué se diferencia A de B?")
    with col_c:
        st.markdown("**3. Reactivación**")
        st.caption("Recicla proyectos antiguos y dales nueva vida.")

# Conclusión
st.markdown("---")
st.markdown("""
<div style="text-align: center;">
    <h3>En conclusión...</h3>
    <p>NotebookLM convierte el <strong>ruido en señal</strong>.</p>
    <p>Nos permite dejar de perder tiempo buscando y empezar a invertir tiempo <strong>comprendiendo</strong>.</p>
    <br>
    <h4>¡Muchas gracias por su atención!</h4>
</div>
""", unsafe_allow_html=True)

if st.balloons():
    pass
