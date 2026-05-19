import os
from openai import OpenAI
from .base import ProveedorIA


class DeepSeekProveedor(ProveedorIA):
    """Proveedor de IA que utiliza el modelo DeepSeek."""

    def __init__(self, modelo: str = "deepseek-v4-flash"):
        """Inicializa el proveedor con el modelo especificado.
        Args:
            modelo (str): El nombre del modelo de DeepSeek a utilizar.
        """
        api_key = os.environ.get("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("Falta la variable DEEPSEEK_API_KEY para usar DeepSeek.")

        self._modelo = modelo
        self._client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com",
        )

    @property
    def nombre(self) -> str:
        return f"DeepSeek ({self._modelo})"

    def generar(self, prompt: str) -> str:
        response = self._client.chat.completions.create(
            model=self._modelo,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
