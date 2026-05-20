import pytest
from backend.src.agente import formular_problema, generar_codigo_pulp, explicar_resultados

def test_formular_problema(monkeypatch):
    class MockModels:
        def generate_content(self, model, contents):
            class MockResponse:
                text = "Formulación Matemática Mock"
            return MockResponse()
    class MockClient:
        def __init__(self, api_key=None):
            self.models = MockModels()
            
    monkeypatch.setattr("backend.src.agente.client", MockClient())
    respuesta = formular_problema("Un granjero tiene 100 hectáreas...")
    assert "Mock" in respuesta

def test_generar_codigo_pulp(monkeypatch):
    class MockModels:
        def generate_content(self, model, contents):
            class MockResponse:
                text = "```python\nimport pulp\n# ...\n```"
            return MockResponse()
    class MockClient:
        def __init__(self, api_key=None):
            self.models = MockModels()
            
    monkeypatch.setattr("backend.src.agente.client", MockClient())
    respuesta = generar_codigo_pulp("Enunciado mock", "Formulación Mock")
    assert "import pulp" in respuesta

def test_explicar_resultados(monkeypatch):
    class MockModels:
        def generate_content(self, model, contents):
            class MockResponse:
                text = "Explicación Mock"
            return MockResponse()
    class MockClient:
        def __init__(self, api_key=None):
            self.models = MockModels()
            
    monkeypatch.setattr("backend.src.agente.client", MockClient())
    respuesta = explicar_resultados("Problema", {"estado": "Optimal", "objetivo": 100, "variables": {}})
    assert "Mock" in respuesta
