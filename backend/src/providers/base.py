from abc import ABC, abstractmethod


class ProveedorIA(ABC):
    @abstractmethod
    def generar(self, prompt: str) -> str:
        """Genera una respuesta a partir de un prompt dado.
        Args:
            prompt (str): El texto de entrada para generar la respuesta.
        Returns:
            str: La respuesta generada.
        """
        ...


    @property
    @abstractmethod
    def nombre(self) -> str:
        """El nombre del proveedor de IA.
        Returns:
            str: El nombre del proveedor.
        """
        ...