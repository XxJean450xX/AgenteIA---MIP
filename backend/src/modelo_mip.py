import pulp
import copy

class ModeloMIP:
    def __init__(self, parametros=None):
        if parametros is None:
            self.parametros = {
                "productos": ["A", "B", "C", "D"],
                "maquinas": ["M1", "M2", "M3"],
                "ganancias": {"A": 120, "B": 150, "C": 90, "D": 200},
                "demandas": {"A": 100, "B": 80, "C": 120, "D": 60},
                "costos_materia_prima": {"A": 30, "B": 45, "C": 20, "D": 60},
                "horas_maquina": {
                    "M1": {"A": 2.0, "B": 3.0, "C": 1.5, "D": 4.0},
                    "M2": {"A": 1.5, "B": 2.0, "C": 2.5, "D": 1.0},
                    "M3": {"A": 1.0, "B": 1.5, "C": 2.0, "D": 3.0},
                },
                "horas_turno": {"M1": 160, "M2": 140, "M3": 180},
                "costo_fijo": {"M1": 500, "M2": 400, "M3": 600},
                "costo_turno": {"M1": 200, "M2": 180, "M3": 250},
                "max_turnos": {"M1": 3, "M2": 3, "M3": 3},
                "presupuesto": 8000
            }
        else:
            self.parametros = copy.deepcopy(parametros)

    def resolver(self) -> dict:
        p = self.parametros
        productos = p["productos"]
        maquinas = p["maquinas"]

        # Crear problema
        prob = pulp.LpProblem("Planificacion_Produccion", pulp.LpMaximize)

        # Variables de decisión
        # 1. Unidades a producir (Continuas >= 0)
        x = pulp.LpVariable.dicts("x", productos, lowBound=0, cat=pulp.LpContinuous)
        
        # 2. Turnos por máquina (Enteras >= 0)
        t = pulp.LpVariable.dicts("t", maquinas, lowBound=0, cat=pulp.LpInteger)

        # 3. Máquina activa (Binarias)
        y = pulp.LpVariable.dicts("y", maquinas, cat=pulp.LpBinary)

        # Función objetivo
        ingresos = pulp.lpSum(p["ganancias"][prod] * x[prod] for prod in productos)
        costos_fijos = pulp.lpSum(p["costo_fijo"][maq] * y[maq] for maq in maquinas)
        costos_turnos = pulp.lpSum(p["costo_turno"][maq] * t[maq] for maq in maquinas)
        costos_materia_prima = pulp.lpSum(p["costos_materia_prima"][prod] * x[prod] for prod in productos)
        
        prob += ingresos - costos_fijos - costos_turnos - costos_materia_prima, "Z"

        # Restricciones
        # 1. Capacidad de máquinas
        for maq in maquinas:
            horas_necesarias = pulp.lpSum(p["horas_maquina"][maq][prod] * x[prod] for prod in productos)
            horas_disponibles = p["horas_turno"][maq] * t[maq]
            prob += horas_necesarias <= horas_disponibles, f"Capacidad_{maq}"

        # 2. Activación de máquina (Lógica)
        for maq in maquinas:
            prob += t[maq] <= p["max_turnos"][maq] * y[maq], f"Activacion_{maq}"

        # 3. Demanda máxima
        for prod in productos:
            prob += x[prod] <= p["demandas"][prod], f"Demanda_{prod}"

        # 4. Presupuesto
        prob += costos_materia_prima <= p["presupuesto"], "Presupuesto"

        # Resolver usando CBC (incluido en PuLP)
        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        # Recopilar resultados
        estado = pulp.LpStatus[prob.status]
        
        produccion_optima = {}
        for prod in productos:
            produccion_optima[prod] = x[prod].varValue if x[prod].varValue else 0.0

        turnos_optimos = {}
        activacion_optima = {}
        uso_capacidad = {}
        for maq in maquinas:
            turnos_optimos[maq] = t[maq].varValue if t[maq].varValue else 0
            activacion_optima[maq] = y[maq].varValue if y[maq].varValue else 0
            
            horas_usadas = sum(p["horas_maquina"][maq][prod] * produccion_optima[prod] for prod in productos)
            horas_disp = p["horas_turno"][maq] * turnos_optimos[maq]
            
            if horas_disp > 0:
                uso_capacidad[maq] = (horas_usadas / horas_disp) * 100
            else:
                uso_capacidad[maq] = 0.0

        # Calcular componentes de costo para el resultado
        ingresos_val = sum(p["ganancias"][prod] * produccion_optima[prod] for prod in productos)
        costos_fijos_val = sum(p["costo_fijo"][maq] * activacion_optima[maq] for maq in maquinas)
        costos_turnos_val = sum(p["costo_turno"][maq] * turnos_optimos[maq] for maq in maquinas)
        costos_mat_val = sum(p["costos_materia_prima"][prod] * produccion_optima[prod] for prod in productos)

        desglose = {
            "ingresos": ingresos_val,
            "costos_fijos": costos_fijos_val,
            "costos_turnos": costos_turnos_val,
            "costos_materia_prima": costos_mat_val
        }

        holguras = {}
        for name, constraint in prob.constraints.items():
            holguras[name] = constraint.slack

        return {
            "estado": estado,
            "objetivo": pulp.value(prob.objective) if prob.objective else 0.0,
            "produccion": produccion_optima,
            "turnos": turnos_optimos,
            "activacion": activacion_optima,
            "uso_capacidad": uso_capacidad,
            "desglose_costos": desglose,
            "holguras": holguras,
            "parametros_usados": copy.deepcopy(p)
        }

    def generar_escenario(self, cambios: dict) -> dict:
        """Genera y resuelve un escenario modificado."""
        nuevos_params = copy.deepcopy(self.parametros)
        
        # Aplicar cambios recursivamente para diccionarios anidados
        for k, v in cambios.items():
            if isinstance(v, dict) and k in nuevos_params and isinstance(nuevos_params[k], dict):
                nuevos_params[k].update(v)
            else:
                nuevos_params[k] = v
                
        nuevo_modelo = ModeloMIP(nuevos_params)
        return nuevo_modelo.resolver()

    def obtener_formulacion(self) -> str:
        """Devuelve la formulación LaTeX del modelo básico."""
        latex = r'''
$$ \max Z = \sum_{p \in P} (c_p \cdot x_p) - \sum_{m \in M} (F_m \cdot y_m) - \sum_{m \in M} (T_m \cdot t_m) - \sum_{p \in P} (\text{Mat}_p \cdot x_p) $$

Sujeto a:
1. Capacidad: $\sum_{p} (a_{mp} \cdot x_p) \leq H_m \cdot t_m \quad \forall m \in M$
2. Activación: $t_m \leq T_{\text{max}} \cdot y_m \quad \forall m \in M$
3. Demanda: $x_p \leq d_p \quad \forall p \in P$
4. Presupuesto: $\sum_{p} (\text{Mat}_p \cdot x_p) \leq \text{Budget}$
5. $x_p \geq 0$ (continua), $t_m \in \mathbb{Z}^+$, $y_m \in \{0,1\}$
'''
        return latex
