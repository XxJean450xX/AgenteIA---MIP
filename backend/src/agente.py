import os
from google import genai
from dotenv import load_dotenv

load_dotenv()


client = genai.Client(api_key=os.getenv("API_GEM"))

contexto = """
Eres un agente experto en investigación de operaciones
especializado en programación entera mixta.

Debes:
- Explicar conceptos
- Resolver dudas
- Analizar resultados matemáticos
- Ayudar a tomar decisiones
"""

def consultar_agente(consulta):
    prompt = contexto + "\n\nEl usuario te esta hablando: " + consulta
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )
    
    return response.text;
