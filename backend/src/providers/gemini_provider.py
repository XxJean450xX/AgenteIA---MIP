import os
from google import genai
from .base import ProveedorIA

class GeminiProveedor(ProveedorIA):
    """Proveedor de IA que utiliza el modelo Gemini de Google."""
    def __init__(self, modelo: str = "gemini-2.5-flash-lite"):
        """Inicializa el proveedor con el modelo especificado.
        Args:
            modelo (str): El nombre del modelo de Gemini a utilizar.
        """
        api_key = os.getenv("API_GEM") or os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("Falta API_GEM o GEMINI_API_KEY para usar Gemini.")

        self._modelo = modelo
        self._client = genai.Client(api_key=api_key)


    @property
    def nombre(self) -> str:
        return f"Gemini ({self._modelo})"
 
    def generar(self, prompt: str) -> str:
        response = self._client.models.generate_content(
            model=self._modelo,
            contents=prompt,
        )
        return response.text
 