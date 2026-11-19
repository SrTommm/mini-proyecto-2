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
    """
    Debe calcular:
    - Cantidad de residuos por tipo.
    - Peso total de residuos.
    - Costo total de tratamiento.
    - Costo de transporte.
    - Costo total de la jornada.
    - Porcentaje de capacidad utilizada.
    - Porcentaje de aprovechamiento potencial.
    - Cumplimiento de las restricciones de capacidad y presupuesto.

    Retorna un diccionario con las claves indicadas en la plantilla.
    La jornada debe evaluarse incluso si incumple las restricciones.
    """
    raise NotImplementedError("Pendiente implementar evaluar_jornada().")


# ============================================================
# PENDIENTE 2: REGISTRAR UNA JORNADA
# ============================================================

def registrar_jornada(jornada, historial):
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