COSTOS_TRATAMIENTO = {
    "papel_carton": 500,
    "plastico": 800,
    "vidrio": 350,
    "organicos": 600,
    "no_aprovechables": 3500}


peso_por_tipo = {"papel_carton": 1,
                      "plastico" :1,
                      "vidrio": 1,
                      "organicos":1,
                        "no_aprovechables" : 1}


costo_tramiento = [peso_por_tipo[i] * COSTOS_TRATAMIENTO[i] for i in peso_por_tipo]

print(costo_tramiento)