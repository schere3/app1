import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Mi IA Personal", page_icon="🤖")

st.title("🤖 Asistente LLM")
st.caption("Una app creada desde la nube con Streamlit")

# Sidebar para la configuración
with st.sidebar:
    st.header("Configuración")
    api_key = st.text_input("Introduce tu OpenAI API Key", type="password")

# Chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "¿En qué puedo ayudarte hoy?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not api_key:
        st.info("Por favor, añade tu API Key de OpenAI para continuar.")
        st.stop()

    client = OpenAI(api_key=api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)