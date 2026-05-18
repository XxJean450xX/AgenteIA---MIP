from dotenv import load_dotenv

try:
    from .providers import DeepSeekProveedor, OpenRouterProveedor, GeminiProveedor
    from .context_loader import ContextLoader
    from .agent_service import AgentService
except ImportError:
    from providers import DeepSeekProveedor, OpenRouterProveedor, GeminiProveedor
    from context_loader import ContextLoader
    from agent_service import AgentService

load_dotenv()

PROVEEDORES_REGISTRADOS = {
    "OpenRouter": {
        "clase": OpenRouterProveedor,
        "env_vars": ["OPEN_ROUTE_API_KEY", "OPENROUTER_API_KEY"],
    },
    "DeepSeek": {
        "clase": DeepSeekProveedor,
        "env_vars": ["DEEPSEEK_API_KEY"],
    },
    "Gemini": {
        "clase": GeminiProveedor,
        "env_vars": ["API_GEM", "GEMINI_API_KEY"],
    },
}

LISTA_PROVEEDORES = tuple(PROVEEDORES_REGISTRADOS.keys())


def crear_proveedor(nombre: str, modelo: str):
    return PROVEEDORES_REGISTRADOS[nombre]["clase"](modelo=modelo)

def main():

    # provider = DeepSeekProveedor()
    provider = OpenRouterProveedor()


    loader = ContextLoader(base_dir="promts")
    agente = AgentService(proveedor=provider, context_loader=loader)

    while True:
        try:
            consulta = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo.")
            break
 
        if not consulta:
            continue
        if consulta.lower() in {"salir", "exit", "quit"}:
            break
 
        respuesta = agente.consultar(consulta)
        print(f"\nAgente: {respuesta}\n")
 
 
if __name__ == "__main__":
    main()
