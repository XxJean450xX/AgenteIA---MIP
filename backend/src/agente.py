import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

try:
    client = genai.Client(api_key=os.getenv("API_GEM", "dummy_key_for_tests"))
except Exception:
    client = None

def _generar_respuesta(prompt: str) -> str:
    if not client:
        return "Error: Cliente Gemini no inicializado (falta API key)."
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error al consultar al agente: {e}"

def formular_problema(enunciado: str) -> str:
    prompt = f"""
Eres un experto académico en Investigación de Operaciones y Programación Entera Mixta (MILP).
El usuario te dará un enunciado de un problema en lenguaje natural.
Tu tarea es leerlo y extraer la formulación matemática de manera formal.
Identifica:
1. Variables de decisión (continuas, enteras o binarias).
2. Función Objetivo (Max o Min).
3. Restricciones.

REGLAS OBLIGATORIAS:
- Usa un tono formal, serio y estrictamente académico.
- NUNCA uses emojis.
- DEBES usar obligatoriamente el entorno matemático de LaTeX para TODAS las ecuaciones y variables. Usa `$$` para bloques matemáticos (ej. `$$ \max Z = \dots $$`) y `$` para variables en línea (ej. `$x_i$`).
- Sé directo y conciso. Evita párrafos largos de texto introductorio. Ve directo a las matemáticas.

Enunciado:
{enunciado}
"""
    return _generar_respuesta(prompt)

def generar_codigo_pulp(enunciado: str, formulacion: str) -> str:
    prompt = f"""
Eres un programador experto en Python y la librería PuLP especializado en Investigación de Operaciones.
Debes traducir EXACTAMENTE el siguiente problema y su formulación matemática a código Python real y funcional.

ENUNCIADO ORIGINAL:
{enunciado}

FORMULACIÓN MATEMÁTICA:
{formulacion}

Genera un bloque de código Python que resuelva este problema específico usando PuLP.
REGLAS CRÍTICAS Y OBLIGATORIAS:
1. NO inventes un problema genérico (ej. no uses variables dummy como x1, x2 si el problema habla de bodegas y ciudades).
2. DEBES crear las variables exactas, definir los costos reales, las capacidades y demandas dadas en el enunciado.
3. El bloque debe comenzar con ```python y terminar con ```.
4. Al final del script debes crear obligatoriamente un diccionario llamado `resultados` con este formato exacto:
resultados = {{
    "estado": pulp.LpStatus[prob.status],
    "objetivo": pulp.value(prob.objective),
    "variables": {{v.name: v.varValue for v in prob.variables()}}
}}
5. Resuelve el problema usando pulp.PULP_CBC_CMD(msg=False).
6. IMPORTANTE: Si usas expresiones generadoras dentro de funciones como `pulp.LpVariable.dicts`, DEBES envolverlas en corchetes `[]` (list comprehensions) para evitar el error 'SyntaxError: Generator expression must be parenthesized'.
7. No uses emojis.
"""
    respuesta = _generar_respuesta(prompt)
    
    # Extraemos solo el código Python en caso de que el LLM agregue texto extra
    if "```python" in respuesta:
        codigo = respuesta.split("```python")[1].split("```")[0].strip()
        return codigo
    return respuesta

def explicar_resultados(enunciado: str, resultados: dict) -> str:
    prompt = f"""
Eres un experto académico en Investigación de Operaciones.
El usuario proporcionó originalmente este enunciado:
{enunciado}

El solver de PuLP generó matemáticamente estos resultados:
- Estado: {resultados.get('estado')}
- Valor Función Objetivo (Z): {resultados.get('objetivo')}
- Valores de Variables: {resultados.get('variables')}

Por favor, redacta una explicación técnica y formal de estos resultados.
Concluye de manera concisa cuál es la decisión que debe tomarse para optimizar el modelo.
Mantén un tono completamente serio, académico y NUNCA uses emojis.
"""
    return _generar_respuesta(prompt)
