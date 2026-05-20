import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import streamlit as st
import pandas as pd
import plotly.express as px

from backend.src import agente
from backend.src import ejecutor_mip

# Configuracion formal
st.set_page_config(
    page_title="Agente MILP - Investigacion de Operaciones",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilo minimalista y serio
st.markdown("""
<style>
    .stApp {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    h1, h2, h3 {
        font-weight: 400;
        color: #333333;
    }
    .status-box {
        padding: 15px;
        border-left: 4px solid #0052cc;
        background-color: #f4f5f7;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("Sistema Inteligente de Optimizacion MILP")
st.markdown("Ingrese el enunciado completo de su problema de Programacion Entera Mixta para iniciar el proceso de modelado, ejecucion y analisis.")

if "estado_ejecucion" not in st.session_state:
    st.session_state.estado_ejecucion = None

enunciado = st.text_area("Enunciado del Problema:", height=200, placeholder="Ejemplo: Un agricultor dispone de 100 hectareas...")

if st.button("Procesar Problema", type="primary"):
    if not enunciado.strip():
        st.error("Por favor, ingrese un enunciado valido.")
    else:
        st.session_state.estado_ejecucion = "en_proceso"
        
        try:
            # 1. Formulacion Matematica
            st.markdown("### 1. Formulacion Matematica")
            with st.spinner("El Agente IA esta formulando el modelo..."):
                formulacion = agente.formular_problema(enunciado)
            st.markdown(formulacion)
            st.divider()

            # 2. Generacion de Codigo
            st.markdown("### 2. Codigo de Solucion (PuLP)")
            with st.spinner("El Agente IA esta generando el codigo optimo..."):
                codigo_pulp = agente.generar_codigo_pulp(enunciado, formulacion)
            st.code(codigo_pulp, language="python")
            st.divider()

            # 3. Ejecucion
            st.markdown("### 3. Ejecucion del Solver")
            with st.spinner("Ejecutando CBC Solver..."):
                resultados = ejecutor_mip.ejecutar_codigo_pulp(codigo_pulp)
            
            if resultados.get("estado") == "Error":
                st.error("Error durante la ejecucion del codigo.")
                st.code(resultados.get("error"))
            else:
                st.success(f"Estado Final del Solver: {resultados.get('estado')}")
                st.metric("Valor de la Funcion Objetivo (Z)", round(resultados.get('objetivo', 0), 4))
                
                # Renderizado generico de variables de decision
                variables = resultados.get("variables", {})
                if variables:
                    st.markdown("**Variables de Decision Optimas:**")
                    df_vars = pd.DataFrame({
                        "Variable": list(variables.keys()),
                        "Valor": list(variables.values())
                    })
                    st.dataframe(df_vars, use_container_width=True)
                    
                    # Grafico dinamico requerido por el usuario
                    st.markdown("### Analisis Visual")
                    fig = px.bar(df_vars, x="Variable", y="Valor", 
                                 title="Distribucion de Valores de Variables Optimas",
                                 text="Valor", color="Variable")
                    fig.update_traces(textposition='outside')
                    st.plotly_chart(fig, use_container_width=True)

                st.divider()

                # 4. Analisis Final
                st.markdown("### 4. Conclusion del Agente IA")
                with st.spinner("El Agente IA esta analizando los resultados..."):
                    explicacion = agente.explicar_resultados(enunciado, resultados)
                st.markdown(explicacion)

        except Exception as e:
            st.error(f"Error critico en el flujo: {str(e)}")
            
        st.session_state.estado_ejecucion = "completado"