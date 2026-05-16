# AgenteIA---MIP

Sistema inteligente basado en IA para la formulación, análisis y resolución de problemas de **Programación Entera Mixta (MIP)** mediante una interfaz web interactiva.

## Implementación en producción

**Demo en línea:**  
https://agenteia---mip-vzvmgce9nzfzafcfdqd6qe.streamlit.app/

---

## Descripción

AgenteIA---MIP es una aplicación desarrollada para asistir en la resolución de problemas de **Investigación de Operaciones**, específicamente en el área de **Programación Entera Mixta (Mixed Integer Programming - MIP)**.

El sistema permite que el usuario:

- Ingrese un problema en lenguaje natural
- Obtenga interpretación matemática del problema
- Reciba una formulación estructurada del modelo
- Visualice restricciones y variables
- Obtenga apoyo inteligente para análisis y comprensión

La aplicación combina:

- **Streamlit** para la interfaz interactiva
- **Google Generative AI** para procesamiento inteligente
- Arquitectura modular frontend/backend
- Despliegue cloud para acceso remoto

---

## Objetivo

Facilitar el aprendizaje y aplicación de modelos de optimización entera mixta mediante asistencia automática impulsada por inteligencia artificial.

Está orientado a:

- Estudiantes de Ingeniería
- Cursos de Investigación de Operaciones
- Modelado matemático
- Optimización aplicada
- Apoyo académico

---

## Arquitectura del proyecto

```text
AgenteIA---MIP/
│
├── backend/
│   └── src/
│       └── agente.py
│
├── frontend/
│   └── src/
│       └── GUI.py
│
├── pyproject.toml
└── README.md
