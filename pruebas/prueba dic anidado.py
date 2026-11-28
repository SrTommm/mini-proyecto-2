
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
puntos_seleccionados = PUNTOS
lista = []
def evaluar_jornada(puntos_seleccionados):
    
    for i in range(len(puntos_seleccionados)):
        c = PUNTOS[puntos_seleccionados[i]]["papel_carton"]
        lista.append(c)
        print("El peso del carton es", c, "kg")

x = ["Cafetería","Talleres de mantenimiento","Zonas deportivas"]

evaluar_jornada(puntos_seleccionados=x)

cant_carton = sum([ PUNTOS[x[i]]["papel_carton"] for i in range(len(x))])

print(cant_carton)

"""
cant_carton = sum([ PUNTOS[puntos_seleccionados[i]]["papel_carton"] for i in range(len(puntos_seleccionados))])
cant_plasticos = sum([ PUNTOS[puntos_seleccionados[i]]["plastico"] for i in range(len(puntos_seleccionados))])
cant_vidrio = sum([ PUNTOS[puntos_seleccionados[i]]["vidrio"] for i in range(len(puntos_seleccionados))])
cant_organico = sum([ PUNTOS[puntos_seleccionados[i]]["organicos"] for i in range(len(puntos_seleccionados))])
cant_NoAprovechable = sum([ PUNTOS[puntos_seleccionados[i]]["no_aprovechables"] for i in range(len(puntos_seleccionados))])
"""