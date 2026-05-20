# AgenteIA — MIP

Sistema inteligente basado en IA para la formulación, análisis y resolución de problemas de **Programación Entera Mixta (MIP)** mediante una interfaz web interactiva premium.

Este proyecto integra un motor matemático riguroso (PuLP con solver CBC) con Inteligencia Artificial (Gemini) para crear una herramienta que no solo resuelve problemas, sino que ayuda a interpretarlos, simularlos y tomar decisiones de negocio.

## Implementación en producción

**Demo en línea:**  
https://agenteia---mip-vzvmgce9nzfzafcfdqd6qe.streamlit.app/

---

## Características Principales

1. **Solver MIP Realista:**
   - Resuelve el clásico problema de planificación de producción de fábrica.
   - Modela simultáneamente 3 tipos de variables: continuas (producción), enteras (turnos) y binarias (activación de máquinas).
   - Optimización de costos fijos, variables y de materia prima frente a restricciones de capacidad, presupuesto y demanda.

2. **Agente IA Enriquecido (Gemini):**
   - **Explicar resultados:** Traduce los datos matemáticos a lenguaje natural comprensible.
   - **Generar escenarios:** Propone alternativas "What-If" para explorar sensibilidades del modelo.
   - **Proponer mejoras:** Analiza holguras y uso de capacidades para identificar cuellos de botella operativos.
   - **Apoyar decisiones:** Evalúa y compara rigurosamente distintos escenarios de producción.

3. **Interfaz Gráfica Premium (Streamlit):**
   - Diseño moderno con tema oscuro, gradientes CSS inyectados y componentes fluidos.
   - **Visualizaciones interactivas** con Plotly: distribución de costos, uso de máquinas, plan óptimo.
   - Panel interactivo para análisis de sensibilidad y comparativa en vivo (What-If).

---

## Modelo Matemático Implementado

**Función Objetivo (Maximizar):**
```latex
Max Z = Σ_p (c_p * x_p) - Σ_m (F_m * y_m) - Σ_m (T_m * t_m) - Σ_p (Mat_p * x_p)
```
> Ganancia neta = ingresos - costos fijos - costos de turnos - costos materia prima.

**Restricciones:**
1. Capacidad: `Σ_p (a_mp * x_p) <= H_m * t_m`
2. Activación: `t_m <= T_max * y_m`
3. Demanda: `x_p <= d_p`
4. Presupuesto: `Σ_p (Mat_p * x_p) <= Budget`

---

## Instalación y Ejecución Local

1. Clona el repositorio e instala dependencias:
```bash
pip install pulp plotly pandas google-genai streamlit python-dotenv pytest
```

2. Configura tus credenciales:
Crea un archivo `.env` en la raíz del proyecto y agrega tu API Key de Gemini:
```env
API_GEM=tu_api_key_aqui
```

3. Ejecuta la aplicación:
```bash
streamlit run frontend/src/GUI.py
```

4. Ejecuta las pruebas unitarias (TDD):
```bash
python -m pytest tests/
```

---

## Arquitectura del Proyecto

```text
AgenteIA---MIP/
│
├── backend/
│   ├── src/
│   │   ├── agente.py          # Lógica de prompts inyectados con Gemini
│   │   └── modelo_mip.py      # Motor de optimización PuLP + CBC
│   └── __init__.py
│
├── frontend/
│   └── src/
│       └── GUI.py             # Interfaz premium con 4 tabs y Plotly
│
├── tests/
│   ├── test_modelo_mip.py     # TDD Tests del solver (vertical slices)
│   └── test_agente.py         # Tests lógicos de prompts
│
├── data/                      # Documentación académica
├── .env                       # Credenciales de IA
├── pyproject.toml             # Dependencias
└── README.md
```
