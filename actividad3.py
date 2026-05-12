import streamlit as st
# Título y textos
st.title("Microcredencial sobre Introducción al Machine Learning")
st.write("Certificado por la Universidad de la Laguna")

# --- MOSTRAR IMAGEN ---
st.image("cursoPowerBI.png", caption="Certificado de Power BI")

# --- MOSTRAR PDF ---
def display_pdf(file_path):
    # Leer el archivo PDF y convertirlo a base64
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    
    # Crear el objeto HTML para embeber el PDF
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
    
    # Renderizar en la app
    st.markdown(pdf_display, unsafe_allow_html=True)

# Reemplaza "Nombre_de_tu_archivo.pdf" por el nombre real que aparece en tu lista de archivos de GitHub
display_pdf("certificadoPowerBI.pdf")
