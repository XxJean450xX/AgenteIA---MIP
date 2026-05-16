import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../..")
    )
)

from backend.src import agente
import streamlit as st

st.set_page_config(
    page_title="Agente MIP",
    page_icon="❁"
)

st.title("🤖 Agente - Programación Entera Mixta")

if "chat" not in st.session_state:
    st.session_state.chat = []

# Mostrar historial
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada
if consulta := st.chat_input("Escribe tu consulta..."):

    st.session_state.chat.append({
        "role": "user",
        "content": consulta
    })

    with st.chat_message("user"):
        st.markdown(consulta)
    
    respuesta = agente.consultar_agente(consulta)

    st.session_state.chat.append({
        "role": "assistant",
        "content": respuesta
    })

    with st.chat_message("assistant"):
        st.markdown(respuesta)