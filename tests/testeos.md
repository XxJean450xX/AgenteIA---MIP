# Lista de Ejercicios de Programación Entera Mixta (MILP)

---

# Ejercicio 1 — Transporte con apertura de centros

Una empresa debe distribuir productos desde dos bodegas hacia tres ciudades.

## Datos

### Costos de transporte por unidad

| Ciudad | Bodega 1 | Bodega 2 |
| ------ | -------- | -------- |
| A      | 4        | 6        |
| B      | 5        | 3        |
| C      | 7        | 4        |

### Capacidades

* Bodega 1: 120 unidades
* Bodega 2: 150 unidades

### Demandas

* Ciudad A: 80
* Ciudad B: 70
* Ciudad C: 60

### Costos fijos

* Abrir Bodega 1 cuesta 500
* Abrir Bodega 2 cuesta 400

## Variables

* (x_{ij}): unidades enviadas desde bodega (i) a ciudad (j)
* (y_i \in {0,1}): indica si la bodega (i) se abre

## Objetivo

Minimizar costos de transporte y apertura.

---

# Ejercicio 2 — Producción de muebles

Una carpintería produce:

* Mesas
* Sillas
* Escritorios

## Recursos disponibles

| Recurso      | Disponibilidad |
| ------------ | -------------- |
| Madera       | 500 kg         |
| Mano de obra | 320 horas      |

## Consumo por unidad

| Producto   | Madera | Mano de obra | Ganancia |
| ---------- | ------ | ------------ | -------- |
| Mesa       | 10     | 5            | 120      |
| Silla      | 4      | 2            | 50       |
| Escritorio | 15     | 8            | 180      |

## Restricciones

* Se deben producir al menos 10 escritorios.
* Si se fabrican mesas, deben producirse mínimo 5.
* La producción de mesas activa una máquina especial con costo fijo de 300.

## Objetivo

Maximizar ganancias netas.

---

# Ejercicio 3 — Selección de proyectos

Una empresa tecnológica evalúa proyectos de inversión.

## Datos

| Proyecto | Ganancia | Costo |
| -------- | -------- | ----- |
| P1       | 800      | 400   |
| P2       | 600      | 300   |
| P3       | 1000     | 500   |
| P4       | 700      | 350   |

## Restricciones

* Presupuesto máximo: 1000
* Si se selecciona P3, también debe seleccionarse P1.
* P2 y P4 no pueden ejecutarse juntos.

## Variables

* (x_i \in {0,1})

## Objetivo

Maximizar ganancias.

---

# Ejercicio 4 — Planeación de turnos

Un hospital necesita asignar enfermeros a turnos.

## Turnos

* Mañana
* Tarde
* Noche

## Requerimientos mínimos

| Turno  | Enfermeros requeridos |
| ------ | --------------------- |
| Mañana | 8                     |
| Tarde  | 6                     |
| Noche  | 5                     |

## Costos por enfermero

| Turno  | Costo |
| ------ | ----- |
| Mañana | 80    |
| Tarde  | 90    |
| Noche  | 120   |

## Restricciones

* Máximo 15 enfermeros contratados.
* Activar el turno nocturno implica costo fijo de supervisión de 500.

## Objetivo

Minimizar costos totales.

---

# Ejercicio 5 — Dieta nutricional

Una persona desea minimizar el costo de su alimentación diaria.

## Alimentos

* Pollo
* Arroz
* Leche
* Huevos

## Información nutricional

| Alimento | Proteína | Calorías | Costo |
| -------- | -------- | -------- | ----- |
| Pollo    | 25       | 200      | 8     |
| Arroz    | 3        | 180      | 2     |
| Leche    | 8        | 120      | 3     |
| Huevos   | 6        | 90       | 1     |

## Requerimientos

* Al menos 70 g de proteína.
* Máximo 2200 calorías.

## Restricción especial

* Si se consumen huevos, mínimo deben consumirse 6.

## Objetivo

Minimizar costo.

---

# Ejercicio 6 — Programación de producción industrial

Una fábrica produce:

* Motores
* Bombas
* Compresores

## Recursos

| Recurso | Disponible |
| ------- | ---------- |
| Acero   | 1000       |
| Energía | 700        |

## Consumo

| Producto  | Acero | Energía | Utilidad |
| --------- | ----- | ------- | -------- |
| Motor     | 12    | 8       | 150      |
| Bomba     | 9     | 6       | 120      |
| Compresor | 20    | 15      | 250      |

## Restricciones

* Si se producen compresores, debe activarse una línea especial.
* Activar la línea cuesta 1000.
* Máximo 30 compresores.

## Objetivo

Maximizar utilidad.

---

# Ejercicio 7 — Asignación de vehículos

Una empresa debe asignar camiones a rutas.

## Datos

| Ruta | Demanda |
| ---- | ------- |
| R1   | 20      |
| R2   | 15      |
| R3   | 25      |

## Vehículos disponibles

| Vehículo | Capacidad | Costo |
| -------- | --------- | ----- |
| Pequeño  | 10        | 100   |
| Grande   | 20        | 180   |

## Restricciones

* Máximo 5 vehículos.
* Si se usa un vehículo grande, debe activarse un permiso especial de 250.

## Objetivo

Minimizar costos.

---

# Ejercicio 8 — Expansión de red de internet

Una empresa ISP desea instalar antenas.

## Antenas posibles

| Zona   | Cobertura     | Costo |
| ------ | ------------- | ----- |
| Norte  | 1200 usuarios | 5000  |
| Sur    | 900 usuarios  | 3500  |
| Centro | 1500 usuarios | 7000  |

## Restricciones

* Cobertura mínima: 2500 usuarios.
* Norte y Centro no pueden instalarse simultáneamente.
* Si se instala Centro, debe instalarse Sur.

## Variables binarias

* (x_i \in {0,1})

## Objetivo

Minimizar costo de instalación.

---

# Ejercicio 9 — Optimización agrícola

Un agricultor debe decidir cuántas hectáreas sembrar de:

* Maíz
* Trigo
* Papa

## Recursos

| Recurso | Disponible |
| ------- | ---------- |
| Tierra  | 200 ha     |
| Agua    | 5000 m³    |

## Datos

| Cultivo | Agua | Ganancia |
| ------- | ---- | -------- |
| Maíz    | 20   | 300      |
| Trigo   | 15   | 250      |
| Papa    | 35   | 500      |

## Restricciones

* Al menos 30 ha de maíz.
* Máximo 50 ha de papa.
* Sembrar papa requiere activar fertilización especial de costo fijo 1200.

## Objetivo

Maximizar utilidad.

---

# Ejercicio 10 — Producción energética

Una empresa puede generar energía usando:

* Planta solar
* Planta térmica
* Planta eólica

## Datos

| Planta  | Energía máxima | Costo por MW |
| ------- | -------------- | ------------ |
| Solar   | 100            | 20           |
| Térmica | 200            | 45           |
| Eólica  | 150            | 25           |

## Restricciones

* Demanda mínima: 250 MW.
* La planta térmica tiene costo fijo de encendido de 3000.
* La energía solar no puede superar el 40% del total generado.

## Objetivo

Minimizar costo total.
