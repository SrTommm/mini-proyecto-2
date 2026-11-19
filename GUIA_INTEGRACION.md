# Guía de integración - Miniproyecto 2 

## 1. Parámetros del escenario

Los datos son ficticios y se utilizan exclusivamente para la simulación académica.

- Capacidad máxima del vehículo: 160 kg.
- Presupuesto máximo por jornada: $305.000 COP.
- Costo fijo de transporte: $45.000 COP por punto seleccionado.
- Costos de tratamiento por kilogramo: papel/cartón $500; plástico $800; vidrio $350; orgánicos $600; no aprovechables $3.500.
- Cada punto seleccionado debe atenderse en su totalidad.
- Una jornada solo es viable si cumple simultáneamente la capacidad y el presupuesto.

Puntos de generación: cafetería, bloques académicos, talleres de mantenimiento y zonas deportivas. Los talleres de mantenimiento representan una jornada de adecuación y limpieza en la que se genera una cantidad elevada de residuos no aprovechables.

## 2. Archivos del proyecto

- `interfaz.py`: contiene la ventana, las pestañas, las tablas, los botones y los campos de selección.
- `logica.py`: contiene los datos del escenario y las funciones que debe completar el grupo.

Los dos archivos deben permanecer en la misma carpeta.

## 3. Ejecutar la aplicación

Desde una terminal ubicada en la carpeta del proyecto, ejecute:

`python interfaz.py`

La interfaz puede abrirse desde el comienzo. Las acciones que dependen de funciones pendientes mostrarán un mensaje hasta que estas se implementen.

## 4. Funciones que debe completar el grupo

### `evaluar_jornada(puntos_seleccionados, puntos)`

Debe retornar un diccionario con:
- `id`: puede inicializarse temporalmente como `None`; se asignará al registrar.
- `puntos`: lista de nombres de puntos seleccionados.
- `cantidades_por_tipo`: diccionario con las cantidades por categoría.
- `peso_total`: suma de todos los kilogramos.
- `costo_tratamiento`: suma de los costos por categoría.
- `costo_transporte`: cantidad de puntos seleccionados multiplicada por el costo fijo.
- `costo_total`: tratamiento más transporte.
- `porcentaje_capacidad`: peso total dividido por la capacidad máxima y multiplicado por 100.
- `porcentaje_aprovechamiento`: proporción de residuos reciclables y orgánicos sobre el peso total.
- `viable`: `True` si cumple simultáneamente capacidad y presupuesto; `False` en caso contrario.
- `restricciones_incumplidas`: lista que indique si se excedió la capacidad, el presupuesto o ambos.

La jornada debe poder evaluarse aunque no sea viable.

### `registrar_jornada(jornada, historial)`

Debe asignar un identificador único y agregar la jornada a la lista `historial`. Retorna la jornada registrada. No debe descartar las jornadas no viables.

### `obtener_historial(historial)`

Ya está implementada. Retorna el historial.

### `comparar_jornadas(jornadas_seleccionadas)`

Recibe dos o más jornadas y retorna un diccionario con dos claves:
- `indicadores`: lista de nombres de los indicadores que se mostrarán como filas.
- `valores`: diccionario cuyas claves son los identificadores de las jornadas y cuyos valores son listas con los resultados en el mismo orden de `indicadores`.

Ejemplo de estructura de retorno (valores ilustrativos):

    {
        "indicadores": ["Peso total (kg)", "Costo total ($)", "Viabilidad"],
        "valores": {
            1: [115, 165550, "Viable"],
            2: [190, 308550, "No viable"]
        }
    }

## 5. Comportamiento de la aplicación

- Una jornada se registra cada vez que el usuario pulsa “Evaluar y registrar jornada” con una selección válida.
- Las jornadas no viables también se conservan.
- El historial existe únicamente mientras la aplicación permanece abierta.
- Para comparar, seleccione dos o más filas del historial. Use Ctrl o Shift para seleccionar varias filas.
- El botón “Limpiar selección” desmarca todos los puntos del módulo de planificación.
- El porcentaje de aprovechamiento considera papel/cartón, plástico, vidrio y residuos orgánicos.

## 6. Recomendaciones

- Puede crear funciones auxiliares dentro de `logica.py`.
- Mantenga los nombres de las funciones y las claves de los diccionarios indicadas, para que la interfaz pueda utilizar sus resultados.
- No incluya código de Tkinter en `logica.py`.
- Pruebe selecciones que cumplan las restricciones y otras que excedan la capacidad o el presupuesto. Por ejemplo, cafetería + bloques académicos + zonas deportivas supera la capacidad, pero no el presupuesto; talleres de mantenimiento supera el presupuesto, pero no la capacidad.
