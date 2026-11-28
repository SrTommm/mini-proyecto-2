"""
MINIPROYECTO 2 - ARCHIVO DE LÓGICA

En este archivo se encuentra la información del escenario y las
funciones necesarias para el funcionamiento del programa.

FUNCIONES QUE DEBE COMPLETAR EL ESTUDIANTE:

1. evaluar_jornada()
   Calcula los indicadores de una jornada y determina si cumple
   las restricciones de capacidad y presupuesto.

2. registrar_jornada()
   Asigna un identificador y almacena la jornada en el historial.

3. comparar_jornadas()
   Organiza la información de las jornadas seleccionadas para
   facilitar su comparación.

Las funciones obtener_puntos() y obtener_historial() ya están
implementadas. No es necesario modificarlas.

IMPORTANTE:
- No modificar los parámetros del escenario.
- No programar elementos de Tkinter en este archivo.
- Respetar los nombres de las funciones y los parámetros definidos.
- Respetar la estructura de los diccionarios de retorno indicados
  en cada función.
"""

CAPACIDAD_MAXIMA = 160
PRESUPUESTO_MAXIMO = 305000
COSTO_TRANSPORTE_POR_PUNTO = 45000

COSTOS_TRATAMIENTO = {
    "papel_carton": 500,
    "plastico": 800,
    "vidrio": 350,
    "organicos": 600,
    "no_aprovechables": 3500
}

PUNTOS = {
    "Cafetería": {
        "papel_carton": 8, "plastico": 12, "vidrio": 2,
        "organicos": 70, "no_aprovechables": 8
    },
    "Bloques académicos": {
        "papel_carton": 15, "plastico": 8, "vidrio": 1,
        "organicos": 5, "no_aprovechables": 6
    },
    "Talleres de mantenimiento": {
        "papel_carton": 0, "plastico": 0, "vidrio": 0,
        "organicos": 0, "no_aprovechables": 75
    },
    "Zonas deportivas": {
        "papel_carton": 5, "plastico": 10, "vidrio": 1,
        "organicos": 12, "no_aprovechables": 7
    }
}

# ============================================================
# PENDIENTE 1: EVALUAR UNA JORNADA
# ============================================================

def evaluar_jornada(puntos_seleccionados, puntos):

    #Cantidad de residuo por tipo
    # cant_elemento = sum([ PUNTOS[puntos_seleccionados[i]]["elemento"] for i in range(len(puntos_seleccionados))])
    #
   
    peso_por_tipo = {"papel_carton": sum([ PUNTOS[puntos_seleccionados[i]]["papel_carton"] for i in range(len(puntos_seleccionados))]),
                      "plastico" :sum([ PUNTOS[puntos_seleccionados[i]]["plastico"] for i in range(len(puntos_seleccionados))]),
                      "vidrio": sum([ PUNTOS[puntos_seleccionados[i]]["vidrio"] for i in range(len(puntos_seleccionados))]),
                      "organicos":sum([ PUNTOS[puntos_seleccionados[i]]["organicos"] for i in range(len(puntos_seleccionados))]),
                        "no_aprovechables" :sum([ PUNTOS[puntos_seleccionados[i]]["no_aprovechables"] for i in range(len(puntos_seleccionados))])}
    
    #Peso total -> sumamos cada peso registrado en el diccionario que guarda los pesos

    peso_total = sum([peso_por_tipo[i] for i in range(len(peso_por_tipo))])

    #costos -> 
    costo_transporte = len(puntos_seleccionados) * COSTO_TRANSPORTE_POR_PUNTO #la cantidad de puntos que visitamos lo multiplicamos por el costo de viaje por punto

    costo_tramiento = sum([peso_por_tipo[i] * COSTOS_TRATAMIENTO[i] for i in peso_por_tipo]) # sumatoria de: el peso * el costo de tratamiento por kg

    costo_jornada = costo_tramiento + costo_transporte # La suma de todos los costos

    #porcentaje - parte / total) * 100
    porcentaje_capacidad_usada = (peso_total / CAPACIDAD_MAXIMA) *100

    #porcentaje aprovechamiento 
    cant_residuos_aprovechables = sum(peso_por_tipo[i] for i in peso_por_tipo if i != "no_aprovechables")
    porcentaje_aprovechamiento = (cant_residuos_aprovechables/160) * 100

    #validacion restricciones
    viabilidad = True #Por defecto es viable, y luego podria cambiar
    restriccion_incumplidas = None
    if peso_total > 160:
        viabilidad = False
        restriccion_incumplidas["peso_total"] = peso_total
    if costo_jornada > 305000: 
        viabilidad = False
        restriccion_incumplidas["costo_total"] = costo_jornada


     #Puntos -> Agrega a una lista los puntos seleccionados

     
    puntos = [i for i in puntos_seleccionados]
        # Revisa por separado cada codicion para agregar la que no se cumple a un diccionario
    jornada = {
            "id" : None,
            "cantidades_por_tipo": peso_por_tipo, 
            "peso_total": peso_total,
            "costo_tratamiento":costo_tramiento ,
            "costo_transporte": costo_transporte,
            "costo_total": costo_jornada,
            "porcentaje_capacidad": porcentaje_capacidad_usada,
            "porcentaje_aprovechamiento": porcentaje_aprovechamiento,
            "viable": viabilidad,
            "restricciones_incumplidas": restriccion_incumplidas ,

               }
    return jornada
    """
    Debe calcular:
    - Cantidad de residuos por tipo. (X)
    - Peso total de residuos. (X)
    - Costo total de tratamiento.  (X)
    - Costo de transporte. (X)
    - Costo total de la jornada. (x)
    - Porcentaje de capacidad utilizada. (X)
    - Porcentaje de aprovechamiento potencial. (X)
    - Cumplimiento de las restricciones de capacidad y presupuesto. (x)

    Retorna un diccionario con las claves indicadas en la plantilla. (X)
    La jornada debe evaluarse incluso si incumple las restricciones.
    """
    raise NotImplementedError("Pendiente implementar evaluar_jornada().")


# ============================================================
# PENDIENTE 2: REGISTRAR UNA JORNADA
# ============================================================

def registrar_jornada(jornada, historial):

    #Contar cuantos elementos historial y asignarle el el proximo numero en el id de la jornada
    id = len(historial) + 1
    jornada["id"] = id


    return jornada

    """
    Debe asignar un identificador único a la jornada y agregarla
    al historial.

    Se deben registrar tanto las jornadas viables como las no viables.
    """
    raise NotImplementedError("Pendiente implementar registrar_jornada().")


# ============================================================
# PENDIENTE 3: COMPARAR JORNADAS
# ============================================================

def comparar_jornadas(jornadas_seleccionadas):
    """
    Recibe dos o más jornadas y organiza sus indicadores para
    facilitar la comparación.

    Debe retornar un diccionario con las claves "indicadores"
    y "valores", siguiendo la estructura indicada en la plantilla.
    """
    raise NotImplementedError("Pendiente implementar comparar_jornadas().")

def obtener_puntos():
    """Retorna los puntos de generación disponibles."""
    return PUNTOS

def registrar_jornada(jornada, historial):
    """
    Asigna un identificador único, agrega la jornada al historial y la retorna.
    Deben registrarse tanto las jornadas viables como las no viables.
    """
    raise NotImplementedError(
        "Pendiente: implementar el registro de jornadas en el historial."
    )


def obtener_historial(historial):
    """Retorna la lista de jornadas registradas."""
    return historial