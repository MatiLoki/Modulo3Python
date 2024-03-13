import sys
precios = {'Notebook': 700000, 
    'Teclado': 25000, 
    'Mouse': 12000, 
    'Monitor': 250000, 
    'Escritorio': 135000, 
    'Tarjeta de Video': 1500000}

def filtrar(diccionario, umbral, operacion="mayor"):
    if operacion == "mayor":
        filtro = {k: v for k, v in diccionario.items() if v > umbral}
    elif operacion == "menor":
        filtro = {k: v for k, v in diccionario.items() if v < umbral}
    else:
        return "Lo sentimos, no es una operación válida"
    return filtro

if len(sys.argv) == 2:
    umbral = int(sys.argv[1])
    resultado = filtrar(precios, umbral)
    print(f"Los productos mayores al umbral son: {', '.join(resultado.keys())}")
elif len(sys.argv) == 3:
    umbral = int(sys.argv[1])
    operacion = sys.argv[2].lower()
    resultado = filtrar(precios, umbral, operacion)
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"Los productos {operacion} al umbral son: {', '.join(resultado.keys())}")

