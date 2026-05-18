import os
import sys
from pathlib import Path

import streamlit as st

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from backend.src.agent_service import AgentService
from backend.src.context_loader import ContextLoader
from backend.src.main import LISTA_PROVEEDORES, PROVEEDORES_REGISTRADOS

st.set_page_config(page_title="Agente MIP", page_icon="❁", layout="wide")

st.title("Agente MIP")
st.caption("Asistente para Programación Entera Mixta con selección de proveedor y validación de acceso.")

MODELOS_PREDEFINIDOS = {
    "OpenRouter": [
        "deepseek/deepseek-v4-flash:free",
        "deepseek/deepseek-chat",
        "openai/gpt-4o-mini",
    ],
    "DeepSeek": [
        "deepseek-v4-flash",
        "deepseek-chat",
        "deepseek-reasoner",
    ],
    "Gemini": [
        "gemini-2.5-flash-lite",
        "gemini-2.5-flash",
        "gemini-2.5-pro",
    ],
}


def _tiene_api_key(nombre_proveedor: str) -> tuple[bool, list[str]]:
    env_vars = PROVEEDORES_REGISTRADOS[nombre_proveedor]["env_vars"]
    presentes = [nombre for nombre in env_vars if os.getenv(nombre)]
    faltantes = [nombre for nombre in env_vars if not os.getenv(nombre)]
    return len(presentes) > 0, faltantes


def _crear_proveedor(nombre_proveedor: str, modelo: str):
    return PROVEEDORES_REGISTRADOS[nombre_proveedor]["clase"](modelo=modelo)


def _clasificar_error(exc: Exception) -> str:
    mensaje = str(exc).lower()
    if any(palabra in mensaje for palabra in ["quota", "credit", "credits", "insufficient", "429", "402", "payment required"]):
        return "Sin créditos o cuota disponible para ese proveedor/modelo."
    if any(palabra in mensaje for palabra in ["api key", "apikey", "authentication", "unauthorized", "401", "forbidden"]):
        return "La API key no está disponible o fue rechazada por el proveedor."
    return f"Error del proveedor: {exc}"


def _validar_acceso(nombre_proveedor: str, modelo: str) -> tuple[bool, str]:
    try:
        proveedor = _crear_proveedor(nombre_proveedor, modelo)
        prueba = proveedor.generar("Responde solo con la palabra OK.")
        return True, f"Acceso válido. Respuesta de prueba: {prueba[:120]}"
    except Exception as exc:
        return False, _clasificar_error(exc)

if "chat" not in st.session_state:
    st.session_state.chat = []
if "proveedor" not in st.session_state:
    st.session_state.proveedor = LISTA_PROVEEDORES[0]
if "modelo" not in st.session_state:
    st.session_state.modelo = MODELOS_PREDEFINIDOS[st.session_state.proveedor][0]

with st.sidebar:
    st.header("Configuración")
    st.session_state.proveedor = st.selectbox(
        "Proveedor",
        LISTA_PROVEEDORES,
        index=LISTA_PROVEEDORES.index(st.session_state.proveedor),
    )

    modelos = MODELOS_PREDEFINIDOS[st.session_state.proveedor]
    if st.session_state.modelo not in modelos:
        st.session_state.modelo = modelos[0]

    st.session_state.modelo = st.selectbox(
        "Modelo",
        modelos,
        index=modelos.index(st.session_state.modelo),
    )

    st.divider()
    st.subheader("Validación")

    api_disponible, faltantes = _tiene_api_key(st.session_state.proveedor)
    if api_disponible:
        st.success("API key detectada")
    else:
        st.error(f"Falta configurar: {', '.join(faltantes)}")

    if st.button("Comprobar acceso y créditos", use_container_width=True):
        con_acceso, detalle = _validar_acceso(st.session_state.proveedor, st.session_state.modelo)
        if con_acceso:
            st.success(detalle)
        else:
            st.error(detalle)

tabs = st.tabs(["Chat", "Modelos", "Estado"])

with tabs[0]:
    proveedor_actual = st.session_state.proveedor
    modelo_actual = st.session_state.modelo
    api_disponible, faltantes = _tiene_api_key(proveedor_actual)

    st.caption(f"Proveedor activo: {proveedor_actual} · Modelo activo: {modelo_actual}")

    if not api_disponible:
        st.error(f"Falta configurar la API key: {', '.join(faltantes)}")

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    consulta = st.chat_input("Escribe tu consulta...", disabled=not api_disponible)

    if consulta:
        st.session_state.chat.append({"role": "user", "content": consulta})

        with st.chat_message("user"):
            st.markdown(consulta)

        try:
            proveedor = _crear_proveedor(proveedor_actual, modelo_actual)
            loader = ContextLoader(base_dir="promts")
            agente = AgentService(proveedor=proveedor, context_loader=loader)
            respuesta = agente.consultar(consulta)
        except ValueError as exc:
            respuesta = str(exc)
        except Exception as exc:
            respuesta = _clasificar_error(exc)

        st.session_state.chat.append({"role": "assistant", "content": respuesta})

        with st.chat_message("assistant"):
            st.markdown(respuesta)

with tabs[1]:
    st.subheader("Modelos predefinidos")
    st.write(f"Proveedor actual: {st.session_state.proveedor}")
    st.write(f"Modelo actual: {st.session_state.modelo}")
    st.caption("Los modelos siguen definidos en la interfaz; el backend solo expone la lista de proveedores.")

with tabs[2]:
    st.subheader("Estado de credenciales")
    for nombre_proveedor in LISTA_PROVEEDORES:
        tiene_key, faltantes = _tiene_api_key(nombre_proveedor)
        if tiene_key:
            st.success(f"{nombre_proveedor}: API key disponible")
        else:
            st.warning(f"{nombre_proveedor}: faltan {', '.join(faltantes)}")