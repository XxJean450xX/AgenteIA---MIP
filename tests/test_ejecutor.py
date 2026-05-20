import pytest
from backend.src.ejecutor_mip import ejecutar_codigo_pulp

def test_ejecutor_pulp_basico():
    codigo = """
import pulp

prob = pulp.LpProblem("Test", pulp.LpMaximize)
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

prob += x + 2*y
prob += x + y <= 10

prob.solve(pulp.PULP_CBC_CMD(msg=False))

resultados = {
    "estado": pulp.LpStatus[prob.status],
    "objetivo": pulp.value(prob.objective),
    "variables": {v.name: v.varValue for v in prob.variables()}
}
"""
    resultado = ejecutar_codigo_pulp(codigo)
    assert resultado["estado"] == "Optimal"
    assert resultado["objetivo"] == 20.0
    assert resultado["variables"]["x"] == 0.0
    assert resultado["variables"]["y"] == 10.0

def test_ejecutor_pulp_error():
    codigo = "esto no es python"
    resultado = ejecutar_codigo_pulp(codigo)
    assert resultado["estado"] == "Error"
    assert "SyntaxError" in resultado["error"] or "NameError" in resultado["error"]
