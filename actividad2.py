import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Presentación IA 2026 - Scherezade",
    page_icon="🤖",
    layout="wide"
)

# --- ESTILOS PERSONALIZADOS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #4285F4; color: white; }
    .script-container {
        background-color: #1e1e1e;
        color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border-left: 8px solid #FBBC04;
        font-family: 'Helvetica', sans-serif;
        font-size: 1.2em;
        line-height: 1.6;
        margin-top: 20px;
    }
    .slide-viewer {
        border: 2px solid #333;
        border-radius: 10px;
        overflow: hidden;
    }
    .presenter-label {
        color: #FBBC04;
        font-weight: bold;
        letter-spacing: 2px;
        margin-bottom: 10px;
        display: block;
    }
    .highlight { color: #4285F4; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DEL DISCURSO ---
slides_content = [
    {
        "titulo": "Introducción",
        "script": "Buenos días, mi nombre es Scherezade. Somos conscientes de que **2026** será recordado como el año en que la IA se volvió tan común como la electricidad. Sin embargo, la gente cree que la IA es solo 'el ChatGPT', pero eso es solo la punta del iceberg. Mi objetivo hoy es sumergiros bajo el agua y descubrir todo ese ecosistema que existe fuera."
    },
    {
        "titulo": "Definición y Funcionamiento",
        "script": "Es una rama de la informática que desarrolla sistemas para realizar tareas propias de la inteligencia humana. Funciona mediante **redes neuronales** que identifican estructuras donde el ojo humano solo percibe ruido. Los 4 enfoques se dividen en actuar o pensar como humanos, o de forma racional."
    },
    {
        "titulo": "Niveles de Inteligencia",
        "script": "Tenemos tres niveles: La **IA débil** (la actual, tareas específicas), la **IA fuerte** (capacidad de razonar en cualquier dominio) y la **Superinteligencia**, que es esa teoría futura donde la IA nos superaría en todos los aspectos."
    },
    {
        "titulo": "Asistentes vs. Agentes",
        "script": "Esta diferencia es clave: El **asistente** recibe instrucciones (como Gemini resumiendo). En cambio, el **agente** de IA persigue un objetivo y decide de forma autónoma cómo alcanzarlo."
    },
    {
        "titulo": "Bloque 1: Los Cerebros (Texto)",
        "script": "Abrimos los 'Cerebros' con **Claude Sonnet 4**. Seguridad y baja tasa de errores. Seguimos con **Perplexity AI**, el bibliotecario obsesivo que busca en tiempo real con fuentes citadas. Y terminamos con **LLaMA 4** de Meta: el motor que puedes instalar en tu propia casa sin que tus datos viajen fuera."
    },
    {
        "titulo": "Bloque 2: Los Creativos (Multimedia)",
        "script": "En imagen manda **Midjourney V7** con piezas con carácter. **DALL·E 4** es el diseñador que vive dentro de tu chat. En video, **Runway** permite decidir movimientos de cámara complejos. Y en sonido, **ElevenLabs** clona la intención y emoción humana, superando la barrera robótica."
    },
    {
        "titulo": "Bloque 3: Los Productivos (Agentes)",
        "script": "**Microsoft 365 Copilot** ya no solo resume; analiza tendencias en Excel y asiste a reuniones. Para programadores, **Cursor** entiende proyectos enteros. Y para el pensamiento: **AudioPen Pro**, que convierte tus divagaciones en texto estructurado."
    },
    {
        "titulo": "Conclusión",
        "script": "Hemos pasado de la era de buscar a la era de sintetizar y actuar. Espero que este mapa os ayude a navegar el ecosistema más allá de la sombra de ChatGPT. Muchas gracias por su atención."
    }
]

# --- LÓGICA DE NAVEGACIÓN ---
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

def move_next():
    if st.session_state.current_step < len(slides_content) - 1:
        st.session_state.current_step += 1

def move_prev():
    if st.session_state.current_step > 0:
        st.session_state.current_step -= 1

# --- INTERFAZ DE USUARIO ---

st.title("🚀 Presentación: El Ecosistema de la IA en 2026")

# Layout de dos columnas: Izquierda Diapositiva, Derecha Control
col_left, col_right = st.columns([2, 1])

with col_left:
    # Mostramos el iframe de Google Slides (se mantiene estático o podrías vincular slides específicos si tuvieras los IDs)
    st.markdown(f"""
        <div class="slide-viewer">
            <iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT2jE_82S8wLEL--86yE8CbkBHr1b2dM4aGa14DexqdEd0BkK21jwGWzoc307UXnA/embed?start=false&loop=false&delayms=3000" 
            frameborder="0" width="100%" height="500" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
        </div>
        """, unsafe_allow_html=True)
    
    st.info(f"📍 Sección actual: **{slides_content[st.session_state.current_step]['titulo']}**")

with col_right:
    st.markdown("### Control de Presentación")
    c1, c2 = st.columns(2)
    with c1:
        st.button("⬅️ Anterior", on_click=move_prev)
    with c2:
        st.button("Siguiente ➡️", on_click=move_next)
    
    st.write("---")
    # Barra de progreso
    progress = (st.session_state.current_step + 1) / len(slides_content)
    st.progress(progress)
    st.caption(f"Paso {st.session_state.current_step + 1} de {len(slides_content)}")

# --- AREA DEL GUION (TELEPROMPTER) ---
st.markdown('<div class="script-container">', unsafe_allow_html=True)
st.markdown('<span class="presenter-label">🎙️ GUIÓN EN VIVO - SCHEREZADE:</span>', unsafe_allow_html=True)

# El texto del guion
current_script = slides_content[st.session_state.current_step]['script']
st.write(current_script)

st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555;'>Herramienta de soporte para Scherezade | IA Presenter 2026</p>", unsafe_allow_html=True)
