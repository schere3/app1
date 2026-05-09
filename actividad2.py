import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")

st.title("Análisis comparativo de Modelos de Inteligencia Artificial.")

# Leemos el contenido de tu archivo HTML
with open("index2.html", "r", encoding="utf-8") as f:
    html_content = f.read()
    
# El height aquí debe ser alto para que no aparezca una doble barra de scroll
# 700 es un buen número para presentaciones estándar
components.html(html_presentacion, height=700)
