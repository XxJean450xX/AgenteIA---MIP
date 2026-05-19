import os
from openai import OpenAI
from .base import ProveedorIA


class OpenRouterProveedor(ProveedorIA):
    """Proveedor de IA que utiliza el modelo OpenRouter."""

    def __init__(self, modelo: str = "deepseek/deepseek-v4-flash:free"):
        """Inicializa el proveedor con el modelo especificado.
        Args:
            modelo (str): El nombre del modelo de OpenRouter a utilizar.
        """
        api_key = os.environ.get("OPEN_ROUTE_API_KEY") or os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("Falta OPEN_ROUTE_API_KEY o OPENROUTER_API_KEY para usar OpenRouter.")

        self._modelo = modelo
        self._client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )

    @property
    def nombre(self) -> str:
        return f"OpenRouter ({self._modelo})"

    def generar(self, prompt: str) -> str:
        response = self._client.chat.completions.create(
            model=self._modelo,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
