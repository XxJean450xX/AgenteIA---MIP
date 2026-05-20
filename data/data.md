# Grupo 4: Programación Lineal Entera Mixta

**Heylin Daniela Hernández Pérez, Ana Laura Morcote Chacón, Oscar Manuel Contreras Gacha, Juan Pablo Bustos Ureña, Daniel Mateo Ballesteros**

**Universidad Distrital Francisco José de Caldas**

---

## I. Introducción

A medida que los problemas reales se han vuelto más complejos, también lo han hecho las herramientas matemáticas diseñadas para abordarlos. Dentro de este conjunto de herramientas, la Programación Lineal Entera Mixta (Mixed Integer Linear Programming, MILP) se ha consolidado como una de las técnicas más robustas y versátiles para modelar problemas en los que coexisten decisiones discretas (por ejemplo, seleccionar o no un proveedor, instalar o no una planta) junto a cantidades continuas (como niveles de producción o flujos de transporte).

La MILP es una extensión de la programación lineal clásica, donde algunas variables de decisión deben ser necesariamente enteras o binarias, mientras que otras pueden asumir valores reales continuos. Esta estructura híbrida le permite capturar una gama más amplia de problemas reales que no pueden ser representados únicamente con variables continuas. En consecuencia, se convierte en una técnica fundamental en situaciones en las que la lógica de decisión es binaria o discreta, como ocurre comúnmente en planificación de producción, logística, diseño de redes, gestión de cadenas de suministro y asignación de recursos. Tal como lo señala Ramos (s.f.), "los modelos MILP permiten incluir restricciones lógicas, condiciones de selección y combinaciones complejas que no son posibles de representar con modelos de programación lineal estándar".

La importancia de la MILP no es solamente práctica, sino también teórica. En términos de complejidad computacional, estos modelos pertenecen a la clase de problemas NP-duros, lo cual implica que, a medida que el tamaño del problema crece, su solución se vuelve exponencialmente más difícil. Este hecho ha impulsado el desarrollo de sofisticados algoritmos y métodos de solución como Branch and Bound, Branch and Cut, así como heurísticas metaheurísticas, permitiendo avanzar en la resolución de problemas a gran escala. Según resalta Prada (s.f.), estos avances han sido posibles gracias a la evolución paralela de herramientas computacionales y técnicas matemáticas que han permitido aplicar MILP en contextos industriales reales con altos volúmenes de datos y restricciones complejas.

El presente texto tiene como objetivo describir y analizar la Programación Lineal Entera Mixta (MILP) desde una perspectiva conceptual y práctica. Se comenzará por establecer su formulación matemática general, comparándola con otros paradigmas como la programación lineal continua y la programación entera. Posteriormente, se examinarán sus propiedades teóricas más relevantes, así como los métodos de solución más empleados en la práctica. Finalmente, se abordarán algunas aplicaciones representativas con el fin de ilustrar la utilidad de esta técnica en contextos reales de decisión operativa.

En suma, la MILP se presenta no solo como una técnica matemática poderosa, sino también como una herramienta fundamental en el diseño de sistemas eficientes, sostenibles y racionales en un entorno donde las decisiones deben ser cada vez más ágiles, precisas y estratégicamente justificadas.

---

## II. Conceptualización y Términos Clave

### ¿Qué es la Programación Lineal Entera Mixta (MILP)?

Es una generalización de la programación lineal pura y de la programación lineal entera, que integra lo mejor de ambas técnicas para modelar de gran manera tanto decisiones discretas como proporciones continuas, la cual estudia problemas de optimización en donde se busca maximizar o minimizar una función objetivo, que está sujeta a un conjunto de restricciones, tanto la función como las restricciones en el campo lineal. Teniendo su primera característica en las restricciones, las cuales necesariamente alguna de las variables debe asumir valores enteros (o también binarios), y las demás pueden ser continuas.

**En términos algebraicos:**

$$\text{Max/min} \; c^T x \quad \text{sujeto a} \quad Ax \leq b, \quad x_i \in \mathbb{Z} \; \text{para} \; i \in \beta, \quad x_j \in \mathbb{R} \; \text{para} \; j \in \delta$$

Donde $x$ es el vector de variables de decisión, $c$ es el vector de coeficientes de la función objetivo, $A$ es una matriz de coeficientes para las restricciones, $b$ es el vector de recursos, $\beta$ y $\delta$ son los subconjuntos de índices de variables discretas y continuas, respectivamente.

Contextualizando el uso de esta técnica en el ámbito real, estos problemas aparecen frecuentemente cuando en un sistema se deben tomar decisiones combinatorias, por ejemplo: decidir si se selecciona un proveedor, se instala una planta o si un producto se produce en un determinado periodo. En la mayoría de los casos, estas decisiones no se pueden representar con variables continuas, por ende, se usan variables discretas, o en otros casos, binarias. Debido a esto, la MILP es una herramienta bastante útil en estos contextos, donde se modelan restricciones lógicas o de selección, y que, al mismo tiempo, se requiere gestionar cantidades o flujos que sí pueden variar en tiempo continuo.

En el ámbito geométrico, esta inclusión de variables discretas provoca que la región factible de la gráfica de la función objetivo deje de ser convexa, lo cual es lo usual en la programación lineal. En MILP, la región pasa a ser discontinua, compuesta por un conjunto de puntos aislados o subconjuntos discretos dentro del espacio de soluciones continuas. Lo que implica que no existe una posibilidad de aplicar técnicas de optimización basadas en gradientes o derivadas, es decir, que los métodos convencionales como el simplex o de punto interior no sean directamente aplicables en su forma original.

### Tabla I: Comparación con conceptos afines (Programación Lineal)

| Característica | LP | MILP |
|---|---|---|
| Variables | Continuas | Mixtas (enteras + continuas) |
| Región factible | Convexa (poliedro) | No convexa |
| Dificultad computacional | Pseudo-polinomial | NP-duro |
| Algoritmos clásicos | Simplex, Punto Interior | Branch and Bound, Branch and Cut |
| Solución óptima | En vértices del politopo | No necesariamente en vértices |
| Aplicaciones | Producción, finanzas | Logística, planificación, redes |

### Propiedades y Teoremas

**Teorema fundamental de LP**

> "Toda solución óptima de un LP se encuentra en un vértice del conjunto factible"

Este teorema no se extiende directamente a MILP debido a la presencia de las variables discretas, lo cual fragmenta la región factible.

**Unimodularidad**

Plantea que, si la matriz de restricciones es totalmente unimodular, es decir, que los únicos elementos de la matriz están en el conjunto {-1, 0, 1} y el vector de recursos es discreto, entonces todas las soluciones básicas del LP son discretas, lo que hace innecesario el uso de MILP.

**Envoltura convexa**

Afirma que el conjunto de soluciones discretas de un MILP forma un poliedro convexo; sin embargo, existe una "envoltura" que sí es convexa la cual contiene todas las soluciones discretas factibles.

### Métodos de solución

Existen ciertos métodos de solución para resolver este tipo de problemas; los más comunes son:

**1. Relajación Lineal**

Se relaja, es decir, se simplifica un problema complejo eliminando temporalmente ciertas restricciones, la condición de integridad y se resuelve como un problema de LP común. Si al momento de obtener la solución, esta cumple con las condiciones de discreción, es óptima también para el MILP.

**2. Branch & Bound (B&B)**

Es el siguiente subconjunto de reglas:

a. Divide el problema en subproblemas más simples al ramificar en variables discretas  
b. Acota soluciones mediante LP simplificados  
c. Poda ramas que no pueden mejorar la solución actual

**3. Branch and Cut**

Combina B&B con planos de corte para eliminar regiones fraccionales sin excluir soluciones discretas.

**4. Heurísticas**

Se aplican algoritmos genéticos, búsquedas locales y simulaciones en problemas muy grandes o cuando se necesita una solución rápida.

### Aplicaciones

**I. Planificación de la producción**

La planificación de la producción busca decidir qué productos fabricar, en qué cantidad, en qué momento y con qué cantidad de recursos, de modo que se minimicen los costos y se maximicen las ganancias.

El modelamiento mediante MILP se basa en utilizar variables discretas (en este caso binarios) para representar si se produce o no un producto en un período determinado y variables continuas para indicar la cantidad exacta de producción.

Esta técnica es usada en empresas como Toyota o Nestlé para la organización de líneas de producción semanales o mensuales.

**II. VRP – Problemas de Ruteo de Vehículos**

El objetivo en estos problemas es diseñar rutas óptimas para una flota de vehículos que debe visitar un conjunto de clientes, minimizando el costo, ya sea la distancia, el tiempo o el dinero. Además de utilizar restricciones logísticas como la capacidad de carga.

Al igual que la aplicación anterior, se utilizan variables binarias para indicar si un vehículo va de un cliente a otro, cantidad de veces que un cliente es visitado y restricciones continuas para límites de capacidad del vehículo.

Esta aplicación ha sido bastante útil para problemas de recolección de basura, reparto de medicinas y hasta planificación de evacuaciones ante desastres naturales.

---

## III. Representación algorítmica (flujogramas)

En el ámbito de la Investigación de Operaciones, los problemas de Programación Entera Mixta (PEM) representan una clase de modelos matemáticos en los que algunas variables de decisión deben tomar valores enteros, mientras que otras pueden ser continuas. Estos problemas surgen frecuentemente en situaciones reales donde ciertas decisiones no pueden fraccionarse, como el número de productos a fabricar, camiones a despachar o personal a contratar.

A continuación se presentan dos diagramas de flujo que guían al analista tanto en la identificación de un problema como PEM (Imagen 1), como en su resolución mediante el método de ramificación y acotamiento (Branch and Bound) (Imagen 2). Estas representaciones gráficas son fundamentales para estructurar el proceso de análisis y resolución de manera sistemática y eficiente, asegurando la correcta clasificación del modelo y la aplicación del algoritmo más adecuado para su solución.

*(Ver Imagen I: Flujograma N°1 — Identificación de PEM)*

*(Ver Imagen II: Flujograma N°2 — Resolución por Branch and Bound)*

---

## IV. Mapa Mental

*(Ver Imagen III: Mapa mental explicativo de la temática)*

---

## V. Ejercicios

En esta sección se desarrollan ejercicios que ilustran la programación entera mixta. A continuación, se presenta la estructura de las tablas Simplex con las cuales fueron resueltos los problemas:

| Cj | C1 | C2 | 0 | 0 | |
|---|---|---|---|---|---|
| V.B (variables básicas) | x_1 | x_2 | S_1 | S_2 | bj |
| x_1 (C1) | a11 | a12 | 1 | 0 | b1 |
| S_2 (0) | a21 | a22 | 0 | 1 | b2 |
| Zj (producto punto) | Z1 | Z2 | Z3 | Z4 | Z (Óptimo) |
| Cj - Zj | C1-Z1 | C2-Z2 | -Z3 | -Z4 | |

- En la fila Cj se ubican los coeficientes de las variables del problema a optimizar.
- En V.B se ubican las variables que tienen como solución un bj. En caso de que una variable no se encuentre en dicha sección al acabar el método, su valor será 0.
- Los coeficientes $a_{ij}$ hacen referencia a los coeficientes de cada restricción.
- Los $Z_j$ son la suma de los productos del $C_j$ correspondiente de la variable básica con el $a_{ij}$ de su misma fila. Ejemplo: $Z_2 = C_1 \cdot a_{12} + 0 \cdot a_{22}$.
- Para seleccionar la **columna pivote**, se tiene que ubicar el elemento en la fila $C_j - Z_j$ el cual sea mayor en caso de maximización y menor en caso de minimización.
- Para seleccionar el **elemento pivote** se divide cada $b_j$ por el elemento de la columna pivote que le corresponda; el menor cociente mayor a cero es el que indica la fila. La intercepción entre la columna pivote y dicha fila es el elemento pivote.
- En las tablas simplex intermedias en el proceso, se denota el número de eliminación de fila a la izquierda de la tabla.

---

### A. Ejercicio 1 [6, p. 328, ej. 12]

| Ejercicio original | Ejercicio modificado para MILP |
|---|---|
| $\max$ y $\min \; Q = 2x + 5y$ | $\max \; Q = 2x_1 + 5x_2$ |
| $x + y \geq 4$ | $x_1 + x_2 \geq 5$ |
| $-x + y \leq 6$ | $-x_1 + x_2 \leq 8$ |
| $x + 3y \leq 30$ | $x_1 + 3x_2 \leq 17$ |
| $x \leq 12$ | $x_1 \leq 12$ |
| $x \geq 0, \; y \geq 0$ | $x_1, x_2 \geq 0$; $x_1$ es entero |

**Modelo reescrito:**

$$\max \; Q = 2x_1 + 5x_2 + 0S_1 + 0S_2 + 0S_3 + 0S_4 - MR_1$$

$$x_1 + x_2 - S_1 + R_1 = 5$$
$$-x_1 + x_2 + S_2 = 8$$
$$x_1 + 3x_2 + S_3 = 17$$
$$x_1 + S_4 = 12$$
$$x_1, x_2 \geq 0 \quad x_1 \text{ es entero}$$

**Respuesta:**

$$q = 32{,}33333 \;;\; x_1 = 12 \;;\; x_2 = 1{,}66666$$

**Conclusión:**

El hecho de que no hubiese sido requerido utilizar algún método para convertir a $x_1$ en un valor discreto se puede ir apreciando desde que se plantea el modelo de programación lineal. La restricción $x_1 \leq 12$ condiciona a $x_1$ a tomar el valor de 12.

---

### B. Ejercicio 2 [6, p. 329, ej. 7]

| Ejercicio original | Ejercicio modificado para MILP |
|---|---|
| $\max \; P = 3x + 2y$ | $\max \; P = 3x_1 + 2x_2$ |
| $2x + y \leq 16$ | $2x_1 + x_2 \leq 15$ |
| $2x + 3y \leq 36$ | $2x_1 + 3x_2 \leq 35$ |
| $4x + 5y \geq 28$ | $4x_1 - 5x_2 \geq 20$ |
| $x \geq 0, \; y \geq 0$ | $x_1, x_2 \geq 0$; $x_2$ es entero |

**Modelo reescrito:**

$$\max \; P = 3x_1 + 2x_2 + 0S_1 + 0S_2 + 0S_3 - MR_1$$

$$2x_1 + x_2 + S_1 = 15$$
$$2x_1 + 3x_2 + S_2 = 35$$
$$4x_1 - 5x_2 - S_3 + R_1 = 20$$
$$x_1, x_2 \geq 0 \quad x_2 \text{ es entero}$$

Una vez obtenida una respuesta inicial, se puede apreciar claramente que $x_2$ no es entera como pide el ejercicio, por lo que se procede a realizar el método de Branch and Bound. Se plantea un nuevo modelo para el método simplex para comprobar cuál de ambas opciones es más óptima.

**Solución relajada inicial:**

$$z = 23{,}2142857 \;;\; x_1 = 6{,}78571429 \;;\; x_2 = 1{,}42857143$$

**Rama $x_2 \geq 2$:** Se viola $x_1 \geq 2$. NO es una solución viable.

**Rama $x_2 \leq 1$:**

$$p = 23 \;;\; x_1 = 7 \;;\; x_2 = 1$$

**Respuesta:**

Entre las dos ramas, la opción más óptima es la segunda:

$$p = 23 \;;\; x_1 = 7 \;;\; x_2 = 1$$

**Conclusión:**

En algunas ocasiones, al darle un valor entero a una de las variables, otras también lo harán. En este caso $x_1$ podía tomar un valor continuo, mas al realizar Branch and Bound en $x_2$, $x_1$ también tomó un valor discreto. Como nota adicional, en este ejercicio de maximización el óptimo bajó de 23.21 a 23; este punto se seguirá discutiendo más a lo largo de los demás ejercicios.

---

### C. Ejercicio 3

*"Cada mes Ana va al veterinario para comprar comida para su gato, a su vez que también compra su arena y agenda las citas médicas para este último. Ana quiere minimizar su gasto de dinero teniendo en cuenta que:*

*1) Tiene que agendar como mínimo un único chequeo para su mascota.*

*2) Un empleado de la tienda le ayuda a llevar las compras a su domicilio si ella compra más de 7,25 kg en total.*

*La comida la compra por grano, mientras la arena viene en bolsas que pesan 1,5 kg cada una. Cada cita médica cuesta $63.000 pesos, cada bolsa de arena $18.000, y por cada kilo de comida le cobran $21.000."*

*Autoría: Ana Laura Morcote Chacón.*

**Modelo:**

$$\min z = 63x_1 + 18x_2 + 21x_3$$
$$s.a: \quad x_3 + 1{,}5x_2 \geq 7{,}25$$
$$x_1 \geq 1$$
$$x_1, x_2, x_3 \geq 0 \quad x_1 \; y \; x_2 \text{ son enteros}$$

**Modelo reescrito:**

$$\min z = 63x_1 + 18x_2 + 21x_3 + 0S_1 + 0S_2 + MR_1 + MR_2$$
$$s.a: \quad x_3 + 1{,}5x_2 - S_1 + R_1 = 7{,}25$$
$$x_1 - S_2 + R_2 = 1$$
$$x_1, x_2, x_3 \geq 0 \quad x_1 \; y \; x_2 \text{ son enteros}$$

**Solución relajada inicial:**

$$z = 150 \text{ mil pesos} \;;\; x_1 = 1 \;;\; x_2 = 4{,}83333 \;;\; x_3 = 0$$

A pesar de que $x_1$ cumple la condición de ser entera, $x_2$ todavía queda pendiente, por lo que se ha de realizar Branch and Bound.

**Rama $x_2 \geq 5$:**

$$z = 153 \text{ mil pesos} \;;\; x_1 = 1 \;;\; x_2 = 5 \;;\; x_3 = 0$$

**Rama $x_2 \leq 4$:**

$$z = 161{,}25 \text{ mil pesos} \;;\; x_1 = 1 \;;\; x_2 = 4 \;;\; x_3 = 1{,}25$$

**Respuesta:**

Entre 153.000 COP y 161.250 COP, 153.000 COP es menor, por lo que a Ana le sale más rentable agendar una única cita veterinaria ($x_1$), comprar 5 bolsas de arena ($x_2$), y no comprar comida para gatos ($x_3$) en esa veterinaria.

**Conclusión:**

Ana tiene que ir a comprar la comida de su gato a otro lado donde le salga más rentable; sin embargo, es poco probable que su gato gaste 5 bolsas de arena en un único mes, ha de tener superávit de arena.

En el ejercicio se especifica que $x_1$ debe tener un valor discreto, a su vez que brinda una restricción base que la condiciona a este tipo de variable.

En este ejercicio de minimización, el óptimo presentó un aumento tras realizar Branch and Bound. En los otros ejercicios también es apreciable que, en casos de maximización el óptimo disminuye, mientras que en casos de minimización el óptimo aumenta.

---

### D. Ejercicio 4

*"Daniela es una arquitecta muy prestigiosa a la que le encargaron la planeación de un conjunto de oficinas inteligentes, donde se maximice el diseño funcional.*

*Primero están los cubículos de trabajo que aportan 4 puntos de funcionalidad cada uno, luego están los metros cuadrados de iluminación led personalizable que aportan 3 puntos, en tercera instancia están las zonas de esparcimiento para empleados las cuales aportan 2 puntos, finalmente están los metros cuadrados de vidrio inteligente decorativo que aportan 1 punto de funcionalidad.*

*Entre oficinas y zonas de esparcimiento no se pueden ocupar más de 35 metros cuadrados; ocupando respectivamente 6 y 4 metros cuadrados.*

*El gasto de energía se tiene que mantener por debajo de 125 kW por metro cuadrado; siendo el consumo en kilovatios por metro cuadrado de las oficinas 3, de la iluminación 7, de las zonas de esparcimiento 5 y de los vidrios 2.*

*En términos de presupuesto, Daniela no puede gastar más de 480 dólares entre la iluminación y los vidrios que valen respectivamente $22 y $13 por metro cuadrado."*

*Autoría: Ana Laura Morcote Chacón.*

**Modelo:**

$$\max z = 4x_1 + 3x_2 + 2x_3 + x_4$$
$$s.a: \quad 6x_1 + 4x_3 \leq 35$$
$$3x_1 + 7x_2 + 5x_3 + 2x_4 \leq 125$$
$$22x_2 + 13x_4 \leq 480$$
$$x_1 \; y \; x_3 \text{ son enteros} \quad x_1, x_2, x_3, x_4 \geq 0$$

**Modelo reescrito:**

$$\max z = 4x_1 + 3x_2 + 2x_3 + x_4 + 0S_1 + 0S_2 + 0S_3$$
$$s.a: \quad 6x_1 + 4x_3 + S_1 = 35$$
$$3x_1 + 7x_2 + 5x_3 + 2x_4 + S_2 = 125$$
$$22x_2 + 13x_4 + S_3 = 480$$
$$x_1 \; y \; x_3 \text{ son enteros} \quad x_1, x_2, x_3, x_4 \geq 0$$

**Solución relajada inicial:**

$$z = 72{,}429078 \;;\; x_1 = 5{,}8\overline{3} \;;\; x_2 = 9{,}30851064 \;;\; x_3 = 0 \;;\; x_4 = 21{,}1702128$$

Al violarse la primera restricción si se añadiese $x_1 \geq 6$, solo queda como opción factible irse por la rama $x_1 \leq 5$.

**Rama $x_1 \leq 5$:**

$$z = 70{,}2393617 \;;\; x_1 = 5 \;;\; x_2 = 8{,}2712766 \;;\; x_3 = 1{,}25 \;;\; x_4 = 22{,}9255319$$

De esta rama surgen dos posibilidades:

**Sub-rama $x_3 \leq 1$:**

$$z = 70{,}1914894 \;;\; x_1 = 5 \;;\; x_2 = 8{,}61702128 \;;\; x_3 = 1 \;;\; x_4 = 22{,}3404255$$

**Sub-rama $x_3 \geq 2$:**

$$z = 68{,}9255319 \;;\; x_1 = 4{,}5 \;;\; x_2 = 7{,}64893617 \;;\; x_3 = 2 \;;\; x_4 = 23{,}9787234$$

**Respuesta:**

Daniela lograría un aproximado de 70,2 puntos de funcionalidad si ella construyese 5 cubículos y una zona de esparcimiento para empleados, a su vez que instalase un aproximado de $8{,}62 \; m^2$ de iluminación led junto con $22{,}34 \; m^2$ de vidrio.

**Conclusión:**

Se pueden presentar casos en los que, al tratar de volver una variable continua a discreta, una "normalizada" anteriormente tome un valor continuo. La restricción $x_3 \geq 2$, hizo que $x_1$ abandonara el valor discreto que se había logrado con anterioridad cumpliendo en su totalidad la restricción de $x_1 \leq 5$.

---

### E. Ejercicio 5

*"La mamá de Óscar le pide el favor de que vaya a la tienda y compre huevos, pan, carne y tomates para el almuerzo de mañana. Óscar quiere minimizar el espacio que los productos ocupan en su carrito de mercado teniendo en cuenta que:*

*1) Un huevo cuesta $850, cada pan está a $400, el kilo de carne cuesta $900 y el kilo de tomate cuesta $600, teniendo destinados $8.000 para las proteínas y $5.600 para lo demás.*

*2) Los huevos junto con pan deben ser al menos 10 unidades, mientras que de carne y tomates deben pesar como mínimo 2,5 kilos.*

*3) Tanto la unidad de pan como el kilo de tomate ocupan 2 unidades de espacio. Lo demás solamente ocupa una unidad de espacio por cada unidad o kilo."*

*Autoría: Ana Laura Morcote Chacón.*

**Modelo:**

$$\min z = x_1 + 2x_2 + x_3 + 2x_4$$
$$s.a: \quad 850x_1 + 900x_3 \leq 8000$$
$$400x_2 + 600x_4 \leq 5600$$
$$x_1 + x_2 \geq 10$$
$$x_3 + x_4 \geq 2{,}5$$
$$x_1 \; y \; x_2 \text{ son enteros} \quad x_1, x_2, x_3, x_4 \geq 0$$

**Modelo reescrito:**

$$\min z = x_1 + 2x_2 + x_3 + 2x_4 + 0S_1 + 0S_2 + 0S_3 + 0S_4 + MR_1 + MR_2$$
$$s.a: \quad 850x_1 + 900x_3 + S_1 = 8000$$
$$400x_2 + 600x_4 + S_2 = 5600$$
$$x_1 + x_2 - S_3 + R_1 = 10$$
$$x_3 + x_4 - S_4 + R_2 = 2{,}5$$
$$x_1 \; y \; x_2 \text{ son enteros} \quad x_1, x_2, x_3, x_4 \geq 0$$

**Solución relajada inicial:**

$$z = 15{,}5882353 \;;\; x_1 = 9{,}41176471 \;;\; x_2 = 0{,}58823529 \;;\; x_3 = 0 \;;\; x_4 = 2{,}5$$

De manera similar al ejercicio anterior, si se añadiese la condición de una de las ramas (en este caso $x_1 \geq 10$), se violaría otra condición ya existente.

**Rama $x_1 \leq 9$:**

$$z = 15{,}611 \;;\; x_1 = 9 \;;\; x_2 = 1 \;;\; x_3 = 0{,}38888889 \;;\; x_4 = 2{,}11$$

Al volver $x_1$ discreta, $x_2$ también obtuvo un valor entero. No es necesario hacer otra rama.

**Respuesta:**

Óscar ocuparía aproximadamente 15,61 unidades de espacio si comprara 9 huevos, un único pan, aproximadamente 0,39 kg de carne junto con 2,11 kg de tomate.

**Conclusión:**

A la mamá de Óscar probablemente le toque preparar de almuerzo una receta que requiera una gran cantidad de tomates, como por ejemplo, un gazpacho.

Al convertir una variable a discreta, no es inusual que las demás variables aumenten o disminuyan dependiendo de las restricciones y el objetivo. En el caso de este ejercicio, al $x_1$ pasar a ser un número entero, $x_3$ pasó de ser nula a tener un valor.

---

## Referencias

[1] Ramos, A. (s.f.). *Modelos de Programación Entera Mixta*. Universidad Pontificia Comillas. Revisado Mayo 28 de 2025.

[2] Prada, M. A. (s.f.). *Introducción a la Programación Entera Mixta*. Universidad de Valladolid. https://www.eii.uva.es/~prada/MIP.pdf Revisado Mayo 28 de 2025.

[3] Elsevier. (s.f.). *Mixed Integer Programming*. ScienceDirect. https://www.sciencedirect.com/topics/computer-science/mixed-integer-programming Revisado Mayo 28 de 2025.

[4] Rodríguez, A. S., & Bolaños, W. J. R. (2021). Optimización de rutas de distribución de cilindros de gas licuado de petróleo (GLP) mediante programación lineal entera mixta. *INGE CUC*, 17(1), 139–152. https://doi.org/10.17981/ingecuc.17.1.2021.11. Revisado Mayo 28 de 2025.

[5] Checa Espinosa, D. J. (2021). *Modelación de la planificación de la producción mediante programación lineal entera mixta* [Tesis de pregrado, Escuela Politécnica Nacional]. Repositorio Digital EPN. https://bibdigital.epn.edu.ec/handle/15000/22325 Revisado Mayo 28 de 2025.

[6] T. Tan. *Mathematics for the Managerial, Life, and Social Sciences*. PWS Pub Co, 1999. Revisado Mayo 28 de 2025.