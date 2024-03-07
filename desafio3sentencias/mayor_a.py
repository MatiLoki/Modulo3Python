

diccionario = { "Enero": 15000, "Febrero": 22000, "Marzo": 12000, "Abril": 17000, "Mayo": 81000, "Junio": 13000, "Julio": 21000,
    "Agosto": 41200, "Septiembre": 25000, "Octubre": 21500, "Noviembre": 91000, "Diciembre": 21000}

filtrado = {}

#for key, value in diccionario.items():
#   print(f" {key} - {value}")

for k, v in diccionario.items():
    if v>40000:
        filtrado[k] = v

print(filtrado)