"""
Tests para ModeloMIP — Solver de Programación Entera Mixta.

Enfoque TDD vertical: cada test verifica comportamiento observable
a través de la interfaz pública de ModeloMIP.
"""
import pytest


# ---------------------------------------------------------------------------
# Slice 1 — Tracer bullet: el solver produce una solución óptima
# ---------------------------------------------------------------------------
class TestSolverProduceSolucion:
    """El solver con parámetros por defecto debe encontrar una solución óptima."""

    def test_resolver_retorna_estado_optimal(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        assert resultado["estado"] == "Optimal"

    def test_resolver_retorna_objetivo_positivo(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        assert resultado["objetivo"] > 0

    def test_resolver_retorna_produccion_para_cada_producto(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        assert "produccion" in resultado
        assert len(resultado["produccion"]) == 4  # 4 productos

    def test_resolver_retorna_turnos_para_cada_maquina(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        assert "turnos" in resultado
        assert len(resultado["turnos"]) == 3  # 3 máquinas

    def test_resolver_retorna_activacion_para_cada_maquina(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        assert "activacion" in resultado
        assert len(resultado["activacion"]) == 3


# ---------------------------------------------------------------------------
# Slice 2 — Restricciones de demanda: producción ≤ demanda máxima
# ---------------------------------------------------------------------------
class TestRestriccionesDemanda:
    """La producción de cada producto no debe exceder su demanda máxima."""

    def test_produccion_no_excede_demanda(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()
        params = resultado["parametros_usados"]

        for producto, unidades in resultado["produccion"].items():
            demanda_max = params["demandas"][producto]
            assert unidades <= demanda_max + 1e-6, (
                f"Producto {producto}: producción {unidades} > demanda {demanda_max}"
            )


# ---------------------------------------------------------------------------
# Slice 3 — Variables mixtas: tipos correctos
# ---------------------------------------------------------------------------
class TestVariablesMixtas:
    """El modelo MIP debe tener los 3 tipos de variables."""

    def test_produccion_es_continua_no_negativa(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        for producto, unidades in resultado["produccion"].items():
            assert unidades >= -1e-6, (
                f"Producto {producto}: producción negativa {unidades}"
            )

    def test_turnos_son_enteros(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        for maquina, turnos in resultado["turnos"].items():
            assert turnos == int(turnos), (
                f"Máquina {maquina}: turnos no entero {turnos}"
            )
            assert turnos >= 0

    def test_activacion_es_binaria(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        for maquina, activa in resultado["activacion"].items():
            assert activa in (0, 1, 0.0, 1.0), (
                f"Máquina {maquina}: activación no binaria {activa}"
            )


# ---------------------------------------------------------------------------
# Slice 4 — Restricción de capacidad: horas usadas ≤ horas disponibles
# ---------------------------------------------------------------------------
class TestRestriccionesCapacidad:
    """Las horas-máquina usadas no deben exceder la capacidad por turnos."""

    def test_uso_capacidad_no_excede_100_porciento(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        for maquina, uso in resultado["uso_capacidad"].items():
            assert uso <= 100.0 + 1e-6, (
                f"Máquina {maquina}: uso capacidad {uso}% > 100%"
            )

    def test_maquina_inactiva_no_tiene_turnos(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        for maquina in resultado["activacion"]:
            if resultado["activacion"][maquina] == 0:
                assert resultado["turnos"][maquina] == 0, (
                    f"Máquina {maquina}: inactiva pero tiene turnos"
                )


# ---------------------------------------------------------------------------
# Slice 5 — Restricción de presupuesto
# ---------------------------------------------------------------------------
class TestRestriccionPresupuesto:
    """El costo total de materia prima no debe exceder el presupuesto."""

    def test_costo_materia_prima_no_excede_presupuesto(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()
        params = resultado["parametros_usados"]

        costo_total = sum(
            params["costos_materia_prima"][p] * resultado["produccion"][p]
            for p in resultado["produccion"]
        )
        assert costo_total <= params["presupuesto"] + 1e-6


# ---------------------------------------------------------------------------
# Slice 6 — Escenarios What-If
# ---------------------------------------------------------------------------
class TestEscenariosWhatIf:
    """generar_escenario() debe resolver con parámetros modificados."""

    def test_escenario_con_mayor_presupuesto(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        base = modelo.resolver()
        escenario = modelo.generar_escenario({"presupuesto": 20000})

        assert escenario["estado"] == "Optimal"
        # Con más presupuesto, la ganancia debe ser >= la base
        assert escenario["objetivo"] >= base["objetivo"] - 1e-6

    def test_escenario_con_demanda_reducida(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        escenario = modelo.generar_escenario({
            "demandas": {"A": 10, "B": 10, "C": 10, "D": 10}
        })

        assert escenario["estado"] == "Optimal"
        for prod, unidades in escenario["produccion"].items():
            assert unidades <= 10 + 1e-6

    def test_escenario_retorna_parametros_modificados(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        escenario = modelo.generar_escenario({"presupuesto": 50000})

        assert escenario["parametros_usados"]["presupuesto"] == 50000


# ---------------------------------------------------------------------------
# Slice 7 — Formulación LaTeX
# ---------------------------------------------------------------------------
class TestFormulacionLaTeX:
    """obtener_formulacion() retorna la representación LaTeX del modelo."""

    def test_formulacion_contiene_funcion_objetivo(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        latex = modelo.obtener_formulacion()

        assert "Max" in latex or "max" in latex or "\\max" in latex

    def test_formulacion_contiene_restricciones(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        latex = modelo.obtener_formulacion()

        assert "\\leq" in latex or "leq" in latex or "<=" in latex


# ---------------------------------------------------------------------------
# Slice 8 — Desglose de costos y resultados completos
# ---------------------------------------------------------------------------
class TestDesgloseCostos:
    """El resultado debe incluir un desglose detallado de costos."""

    def test_desglose_tiene_componentes(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        desglose = resultado["desglose_costos"]
        assert "ingresos" in desglose
        assert "costos_fijos" in desglose
        assert "costos_turnos" in desglose
        assert "costos_materia_prima" in desglose

    def test_ganancia_neta_coincide_con_objetivo(self):
        from backend.src.modelo_mip import ModeloMIP

        modelo = ModeloMIP()
        resultado = modelo.resolver()

        desglose = resultado["desglose_costos"]
        ganancia_calculada = (
            desglose["ingresos"]
            - desglose["costos_fijos"]
            - desglose["costos_turnos"]
            - desglose["costos_materia_prima"]
        )
        assert abs(ganancia_calculada - resultado["objetivo"]) < 1e-4
