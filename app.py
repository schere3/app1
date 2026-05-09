import streamlit as st
import pandas as pd

# Asignación de páginas
pg_intro = st.Page("introduccion.py", title="Introducción")
pg1 = st.Page("actividad1.py", title="Actividad 1")
pg2 = st.Page("actividad2.py", title="Actividad 2")
pg3 = st.Page("actividad3.py", title="Actividad 3")      
pg4 = st.Page("actividad4.py", title="Actividad 4")                     
pg5 = st.Page("actividad5.py", title="Actividad 5")        
pg6 = st.Page("actividad6.py", title="Actividad 6")        
pg7 = st.Page("actividad7.py", title="Actividad 7")        
pg8 = st.Page("actividad8.py", title="Actividad 8")     
pg9 = st.Page("actividad9.py", title="Actividad 9")        


navigation_env = st.navigation(
    {
        "": [pg_intro],
        "Bloque I: IA y Gestión de la Información" : [pg1,pg2],
        "Bloque I: IA y Gestión de la Información": [pg3,pg4,pg5],
        "Bloque I: IA y Gestión de la Información": [pg6,pg7,pg8,pg9]
    }
)
navigation_env.run()