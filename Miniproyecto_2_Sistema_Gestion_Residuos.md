# MINIPROYECTO 2
# Sistema de gestión y planificación de recolección y aprovechamiento de residuos

---

## 1. Contexto

La gestión de residuos es un desafío presente en instituciones, empresas y diferentes espacios de actividad humana. Una adecuada planificación de su recolección y tratamiento permite reducir el impacto ambiental, aprovechar materiales que pueden reincorporarse a otros procesos y administrar de manera eficiente los recursos disponibles.

En una institución con diferentes espacios de generación de residuos, como cafeterías, bloques académicos, talleres y zonas deportivas, las cantidades y los tipos de residuos producidos pueden variar considerablemente. Por esta razón, organizar las jornadas de recolección requiere analizar diferentes factores: la cantidad de residuos, su clasificación, los costos asociados a su tratamiento, la capacidad del vehículo y el presupuesto disponible.

En este miniproyecto se desarrollará un sistema de gestión y planificación de recolección y aprovechamiento de residuos. La aplicación permitirá consultar información de diferentes puntos de generación, seleccionar los lugares que se desean atender en una jornada, evaluar la viabilidad de la operación y comparar los resultados de distintas alternativas.

El propósito no es únicamente desarrollar un programa que realice cálculos, sino construir una herramienta que permita analizar información y apoyar la toma de decisiones considerando aspectos técnicos, económicos, sociales y ambientales.

## 2. Objetivo general

Desarrollar una aplicación en Python que permita gestionar información de generación de residuos, planificar jornadas de recolección y evaluar diferentes alternativas de operación mediante el uso de estructuras de datos, funciones, estructuras condicionales, ciclos y validaciones.

## 3. Objetivos específicos

- Organizar y consultar información relacionada con los puntos de generación y los tipos de residuos.
- Calcular las cantidades y los costos asociados a una jornada de recolección.
- Evaluar el cumplimiento de las restricciones de capacidad del vehículo y presupuesto disponible.
- Registrar y comparar diferentes jornadas para analizar sus resultados.
- Interpretar los resultados desde perspectivas económicas, sociales y ambientales.
- Justificar las decisiones de diseño e implementación adoptadas durante el desarrollo del programa.

## 4. Condiciones generales del proyecto

| Aspecto | Condición |
|---|---|
| Interfaz gráfica | Se suministrará una plantilla desarrollada con Tkinter. Los estudiantes deberán completar la lógica del programa e integrarla con la interfaz proporcionada. |
| Almacenamiento | Los datos se manejarán en memoria durante la ejecución. No se requiere utilizar bases de datos ni guardar información en archivos. |

### 4.1. Organización del programa

La plantilla suministrada contiene dos archivos principales:

- **`interfaz.py`:** contiene la estructura de la interfaz gráfica y los mecanismos para interactuar con el usuario.
- **`logica.py`:** contiene la estructura inicial de las funciones que deberán implementar los estudiantes.

La lógica del programa debe desarrollarse de manera independiente de la interfaz. Esto significa que los cálculos, validaciones y operaciones sobre los datos deben realizarse mediante funciones en `logica.py`, mientras que `interfaz.py` se encarga de presentar la información y recibir las acciones del usuario.

En particular, se deberán implementar las funciones definidas en la plantilla para:

- Obtener la información de los puntos de generación.
- Evaluar una jornada de recolección.
- Registrar las jornadas en el historial.
- Consultar el historial.
- Comparar las jornadas seleccionadas.

La plantilla incluye algunas funciones auxiliares y estructuras iniciales que deberán revisarse para comprender cómo se integra la lógica con la interfaz.

No es necesario construir una interfaz gráfica desde cero ni modificar la estructura general de la plantilla. El trabajo debe concentrarse en implementar correctamente la lógica y conectar sus resultados con los elementos de la interfaz gráfica.

### 4.2. Uso de herramientas de inteligencia artificial

Se permite el uso de herramientas de inteligencia artificial como apoyo durante el desarrollo del proyecto. Estas pueden utilizarse para consultar conceptos, proponer soluciones, generar fragmentos de código, identificar errores, sugerir pruebas o apoyar la integración entre la lógica y la interfaz gráfica.

Sin embargo, el uso de estas herramientas no reemplaza la responsabilidad de los integrantes sobre el trabajo entregado. Cada estudiante debe revisar, comprender, probar y estar en capacidad de explicar el funcionamiento del código.

En el documento de análisis se deberá indicar brevemente si se utilizaron herramientas de inteligencia artificial, para qué actividades se emplearon y qué modificaciones, verificaciones o ajustes realizaron los integrantes sobre los resultados obtenidos.

## 5. Descripción del escenario

Una institución desea organizar la recolección y el aprovechamiento de los residuos generados en cuatro puntos:

1. Cafetería.
2. Bloques académicos.
3. Talleres de mantenimiento.
4. Zonas deportivas.

Para cada punto se dispone de una cantidad estimada de residuos clasificados en cinco categorías:

- Papel y cartón.
- Plástico.
- Vidrio.
- Residuos orgánicos.
- Residuos no aprovechables.

Para efectos del proyecto, se considera que el papel y cartón, el plástico y el vidrio pueden ser aprovechados mediante procesos de reciclaje. Los residuos orgánicos pueden destinarse a procesos de compostaje y los no aprovechables requieren disposición final.

### 5.1. Cantidades de residuos por punto de generación

Los siguientes valores corresponden a un escenario académico ficticio:

| Tipo de residuo | Cafetería | Bloques académicos | Talleres de mantenimiento | Zonas deportivas |
|---|---:|---:|---:|---:|
| Papel y cartón | 8 kg | 15 kg | 0 kg | 5 kg |
| Plástico | 12 kg | 8 kg | 0 kg | 10 kg |
| Vidrio | 2 kg | 1 kg | 0 kg | 1 kg |
| Orgánicos | 70 kg | 5 kg | 0 kg | 12 kg |
| No aprovechables | 8 kg | 6 kg | 75 kg | 7 kg |
| **Total** | **100 kg** | **35 kg** | **75 kg** | **35 kg** |

El punto de talleres de mantenimiento representa una jornada de adecuación y limpieza de estos espacios, durante la cual se genera una cantidad considerable de residuos no aprovechables.

### 5.2. Costos de tratamiento

Para calcular el costo de tratamiento se utilizarán los siguientes valores ficticios:

| Tipo de residuo | Costo de tratamiento por kg |
|---|---:|
| Papel y cartón | $500 COP |
| Plástico | $800 COP |
| Vidrio | $350 COP |
| Orgánicos | $600 COP |
| No aprovechables | $3.500 COP |

El costo de tratamiento de cada categoría se obtiene multiplicando la cantidad de residuos por su respectivo costo por kilogramo.

### 5.3. Restricciones operativas

Cada jornada de recolección tiene las siguientes condiciones:

- **Capacidad máxima del vehículo:** 160 kg.
- **Presupuesto máximo por jornada:** $305.000 COP.
- **Costo de transporte:** $45.000 COP por cada punto de generación seleccionado.

Para efectos del ejercicio, cada punto seleccionado debe atenderse completamente. No se permite recolectar únicamente una parte de los residuos de un punto.

Una jornada se considera viable cuando cumple simultáneamente las dos restricciones:

1. El peso total de los residuos no supera la capacidad máxima del vehículo.
2. El costo total de la operación no supera el presupuesto disponible.

El costo total de una jornada corresponde a la suma del costo de tratamiento de los residuos y el costo de transporte de los puntos seleccionados.

## 6. Requerimientos funcionales

La aplicación deberá contar con tres módulos principales, disponibles desde la interfaz gráfica suministrada.

### Módulo 1. Consulta de puntos de generación

Este módulo permitirá consultar la información de los cuatro puntos de generación de residuos.

La aplicación deberá:

- Mostrar los puntos de generación disponibles.
- Presentar las cantidades de residuos de cada categoría para cada punto.
- Calcular y mostrar el peso total de residuos generado en cada punto.

La información de los puntos será precargada en el programa. No se requiere que el usuario registre nuevos puntos ni modifique las cantidades iniciales.

### Módulo 2. Planificación de jornadas de recolección

Este módulo permitirá seleccionar uno o varios puntos de generación para conformar una jornada de recolección.

A partir de la selección realizada, el programa deberá:

1. Identificar las cantidades de residuos correspondientes a los puntos seleccionados.
2. Calcular la cantidad total de residuos por categoría.
3. Calcular el peso total de residuos de la jornada.
4. Calcular el costo total de tratamiento de los residuos.
5. Calcular el costo de transporte, considerando el número de puntos seleccionados.
6. Calcular el costo total de la jornada.
7. Calcular el porcentaje de utilización de la capacidad del vehículo.
8. Calcular el porcentaje potencial de aprovechamiento de los residuos.

Una vez realizados los cálculos, el programa deberá evaluar las restricciones de capacidad y presupuesto.

El resultado deberá indicar si la jornada es viable o no viable. En caso de incumplimiento, deberá identificar claramente cuál o cuáles restricciones fueron superadas y mostrar la diferencia frente al límite establecido.

**Importante:** una jornada puede incumplir una o las dos restricciones. El programa debe evaluar ambas de manera independiente, sin asumir que el incumplimiento de una implica necesariamente el incumplimiento de la otra.

### Módulo 3. Consulta y comparación de resultados

Cada vez que el usuario evalúe una jornada, esta deberá quedar registrada en el historial de la aplicación, independientemente de que sea viable o no.

Este historial permitirá consultar las jornadas evaluadas durante la ejecución del programa.

La aplicación deberá permitir seleccionar dos o más jornadas del historial para compararlas mediante indicadores como:

- Puntos de generación atendidos.
- Peso total de residuos recolectados.
- Cantidades por categoría de residuos.
- Costo de tratamiento.
- Costo de transporte.
- Costo total de la jornada.
- Porcentaje de utilización de la capacidad del vehículo.
- Porcentaje potencial de aprovechamiento.
- Estado de viabilidad.

La comparación deberá presentar los resultados de manera organizada para facilitar la identificación de diferencias entre las alternativas evaluadas.

No se requiere implementar un algoritmo que seleccione automáticamente la mejor jornada. La comparación debe proporcionar información suficiente para que el usuario pueda analizar y justificar cuál alternativa considera más conveniente según los criterios que establezca.

## 7. Indicadores de análisis

Para apoyar la interpretación de los resultados, el programa deberá calcular los siguientes indicadores:

### 7.1. Porcentaje de utilización de la capacidad

Representa qué proporción de la capacidad máxima del vehículo se utiliza durante la jornada.

**Fórmula:**

`(Peso total recolectado / Capacidad del vehículo) * 100`

### 7.2. Porcentaje potencial de aprovechamiento

Para este ejercicio se considera que el papel y cartón, el plástico, el vidrio y los residuos orgánicos tienen potencial de aprovechamiento.

**Fórmula:**

`(Peso de residuos aprovechables / Peso total de residuos) * 100`

Este indicador representa el potencial de aprovechamiento según la clasificación establecida en el escenario. No significa que todo el material vaya a ser efectivamente recuperado.

Los indicadores deberán calcularse a partir de los datos de cada jornada, evitando utilizar valores fijos que no correspondan a la selección realizada.

## 8. Validaciones y manejo de errores

El programa deberá contemplar validaciones que eviten operaciones incorrectas y permitan una interacción adecuada con el usuario.

Como mínimo, se deberán considerar las siguientes situaciones:

- No permitir evaluar una jornada si no se ha seleccionado ningún punto de generación.
- Verificar que los puntos seleccionados correspondan a opciones disponibles.
- Evitar que una selección vacía genere cálculos o registros incorrectos.
- Evitar errores cuando se consulten o comparen jornadas sin información disponible.
- Verificar que se seleccionen al menos dos jornadas para realizar una comparación.
- Controlar situaciones que puedan producir errores durante la ejecución del programa.

Las validaciones deberán estar implementadas en la lógica del programa. No basta con mostrar mensajes en la interfaz si la operación correspondiente no está correctamente controlada.

## 9. Análisis de impacto y toma de decisiones

Además del desarrollo de la aplicación, los integrantes deberán analizar los resultados obtenidos y reconocer que la planificación de la recolección de residuos involucra diferentes dimensiones.

### 9.1. Dimensión económica

- ¿Qué factores tienen mayor influencia en el costo total de una jornada?
- ¿Cómo cambia el costo cuando se seleccionan diferentes puntos de generación?
- ¿Qué alternativas permiten atender una mayor cantidad de residuos sin superar el presupuesto?
- ¿Qué decisiones podrían tomarse para utilizar de manera más eficiente los recursos disponibles?

### 9.2. Dimensión ambiental

- ¿Qué tipos de residuos representan el mayor potencial de aprovechamiento?
- ¿Cómo cambia el porcentaje potencial de aprovechamiento entre las jornadas evaluadas?
- ¿Qué consecuencias ambientales podrían tener una adecuada separación y gestión de los residuos?
- ¿Qué limitaciones tiene utilizar únicamente el porcentaje potencial de aprovechamiento como indicador ambiental?

### 9.3. Dimensión social

- ¿Qué beneficios puede generar una adecuada gestión de residuos para las personas que utilizan los diferentes espacios de la institución?
- ¿Qué acciones podrían promover una mayor separación de residuos en los puntos de generación?
- ¿Cómo podrían participar estudiantes, docentes, personal administrativo y personal de servicios generales en el mejoramiento del proceso?

### 9.4. Toma de decisiones

A partir de los resultados de la aplicación, deberán comparar diferentes jornadas y seleccionar una alternativa que consideren conveniente.

La decisión deberá justificarse considerando, como mínimo, el cumplimiento de las restricciones, los costos, la cantidad de residuos atendidos y el potencial de aprovechamiento.

No necesariamente existe una única alternativa óptima. Lo importante es que la decisión esté respaldada por los resultados obtenidos y por argumentos claros.

## 10. Entregables

Cada equipo deberá entregar los siguientes elementos:

### 10.1. Código fuente

Se deberá entregar el código completo del proyecto, incluyendo:

- `interfaz.py`
- `logica.py`

El programa deberá ejecutarse correctamente utilizando la plantilla suministrada y permitir el acceso a los tres módulos funcionales.

### 10.2. Diagrama de flujo

Se deberá elaborar un diagrama de flujo que represente la lógica general del sistema.

El diagrama deberá permitir comprender cómo se realiza la consulta de información, la planificación de jornadas, la evaluación de restricciones y el registro y comparación de resultados.

No es necesario representar cada detalle de la interfaz gráfica. El énfasis debe estar en los procesos, decisiones y operaciones principales del programa.

### 10.3. Documento de análisis y justificación

Se deberá entregar un documento breve que contenga:

1. **Descripción de la solución:** explicación general del funcionamiento de la aplicación y de los módulos desarrollados.
2. **Decisiones de implementación:** justificación de las estructuras de datos, funciones y procedimientos utilizados para organizar y procesar la información.
3. **Pruebas realizadas:** descripción de los casos utilizados para verificar el funcionamiento del programa, incluyendo jornadas viables y no viables.
4. **Análisis de resultados e impacto:** reflexión sobre las dimensiones económica, ambiental y social planteadas en el proyecto.
5. **Uso de inteligencia artificial:** herramientas utilizadas, actividades en las que se emplearon y verificaciones o modificaciones realizadas por los integrantes.

El documento debe evidenciar el análisis realizado por el equipo y la comprensión de las decisiones tomadas durante el desarrollo. No se busca una explicación extensa de cada línea de código.

## 11. Sustentación

Cada equipo deberá realizar una sustentación del proyecto. Durante esta actividad se revisará el funcionamiento de la aplicación y se formularán preguntas relacionadas con la solución implementada.

Todos los integrantes deben estar en capacidad de:

- Explicar la lógica general del programa.
- Justificar las estructuras de datos y funciones utilizadas.
- Explicar los cálculos y las validaciones implementadas.
- Interpretar los resultados obtenidos.
- Reconocer y explicar las decisiones de implementación realizadas.

Las preguntas podrán abordar cualquier parte del código, independientemente de quién haya desarrollado inicialmente cada componente.

El uso de herramientas de inteligencia artificial está permitido, pero no exime a los integrantes de comprender y demostrar dominio sobre la solución entregada.

## 12. Criterios generales de evaluación

La evaluación tendrá en cuenta los siguientes aspectos, organizados de acuerdo con los objetivos de aprendizaje del curso:

### OA1. Análisis y comprensión del problema

- Comprensión del escenario y sus restricciones.
- Identificación de datos, procesos y resultados esperados.
- Análisis de las alternativas y justificación de las decisiones tomadas.

### OA2. Diseño e implementación de la solución

- Organización de la información mediante estructuras de datos adecuadas.
- Uso correcto de funciones y modularización del programa.
- Aplicación de estructuras condicionales e iterativas.
- Implementación de cálculos, validaciones y manejo de errores.
- Integración adecuada entre la lógica del programa y la interfaz gráfica.
- Funcionamiento y coherencia de los resultados obtenidos.

### OA3. Comunicación, documentación e impacto

- Claridad y organización del diagrama de flujo.
- Calidad del documento de análisis y justificación.
- Capacidad para interpretar los resultados desde las dimensiones económica, ambiental y social.
- Claridad en la sustentación y capacidad para explicar las decisiones de implementación.

La evaluación considerará tanto el resultado obtenido como el razonamiento, la lógica y el análisis evidenciados durante el desarrollo y la sustentación.

---

## Consideraciones finales

- La información y los costos suministrados corresponden a un escenario académico ficticio.
- No se requiere utilizar bases de datos, archivos externos ni librerías adicionales para desarrollar la lógica principal del proyecto.
- La interfaz gráfica será suministrada por el docente.
- Se permite el uso de inteligencia artificial como herramienta de apoyo, siempre que los integrantes comprendan, verifiquen y puedan explicar el trabajo entregado.
- El proyecto debe desarrollarse dentro del alcance de los contenidos trabajados en el curso.