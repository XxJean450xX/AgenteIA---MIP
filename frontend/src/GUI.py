import streamlit as st
from backend.src import agente

st.set_page_config(
    page_title="Agente MIP",
    page_icon="🤖"
)

st.title("🤖 Agente Inteligente MIP")

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