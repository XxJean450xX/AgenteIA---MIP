import traceback

def ejecutar_codigo_pulp(codigo: str) -> dict:
    """
    Ejecuta un código Python (PuLP) dinámicamente y extrae la variable 'resultados'.
    Espera que el código generado defina un diccionario 'resultados' con estado, objetivo y variables.
    """
    entorno_local = {}
    try:
        # Ejecutamos el código con exec en un entorno vacío
        exec(codigo, {}, entorno_local)
        
        # Extraemos 'resultados' si el agente lo generó correctamente
        if 'resultados' in entorno_local:
            return entorno_local['resultados']
        else:
            return {
                "estado": "Error",
                "error": "El código ejecutó sin errores pero no definió la variable 'resultados'."
            }
            
    except Exception as e:
        error_trace = traceback.format_exc()
        return {
            "estado": "Error",
            "error": error_trace
        }
