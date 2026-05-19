"""
context_loader.py

SRP: responsabilidad única → cargar y cachear archivos .md de contexto.
El AgentService no sabe NI CÓMO ni DE DÓNDE viene el contexto.
"""

from pathlib import Path
from functools import lru_cache


class ContextLoader:
    """Lee archivos .md y los entrega como strings cacheados."""

    def __init__(self, base_dir: str = "promts"):
        base_path = Path(base_dir)
        if not base_path.is_absolute():
            base_path = Path(__file__).resolve().parent / base_path
        self._base = base_path

    @lru_cache(maxsize=16)
    def cargar(self, nombre_archivo: str) -> str:
        """
        Lee un archivo .md relativo a base_dir.

        Args:
            nombre_archivo: Ej. "contexto.md" o "sub/especialidad.md"

        Returns:
            Contenido del archivo como string.

        Raises:
            FileNotFoundError: si el archivo no existe.
        """
        ruta = self._base / nombre_archivo
        if not ruta.exists():
            raise FileNotFoundError(f"Contexto no encontrado: {ruta}")
        return ruta.read_text(encoding="utf-8")

    def invalida_cache(self) -> None:
        """Limpia la caché (útil en desarrollo al editar los .md)."""
        self.cargar.cache_clear()