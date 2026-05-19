try:
    from .providers.base import ProveedorIA
    from .context_loader import ContextLoader
except ImportError:
    from providers.base import ProveedorIA
    from context_loader import ContextLoader


class AgentService:
    """Servicio principal del agente, que orquesta proveedores de IA y carga de contexto."""

    def __init__(
        self,
        proveedor: ProveedorIA,
        context_loader: ContextLoader,
        archivo_contexto: str = "contexto.md",
    ):
        """
        self._proveedor = proveedor
        self._context_loader = context_loader
        Args:
            proveedor: Una instancia de ProveedorIA para generar respuestas.
            context_loader: Una instancia de ContextLoader para cargar archivos de contexto.
            archivo_contexto: El nombre del archivo .md que contiene el contexto por defecto.
        """
        self._proveedor = proveedor
        self._context_loader = context_loader
        self._archivo_contexto = archivo_contexto

    def consultar(self, consulta: str) -> str:
        """
        Procesa la consulta del usuario combinando contexto + pregunta.

        Args:
            consulta: Texto libre del usuario.

        Returns:
            Respuesta del modelo activo.
        """
        contexto = self._context_loader.cargar(self._archivo_contexto)
        prompt = f"{contexto}\n\nEl usuario te está hablando: {consulta}"
        return self._proveedor.generar(prompt)

    @property
    def proveedor_activo(self) -> str:
        """Nombre del proveedor actualmente configurado."""
        return self._proveedor.nombre
