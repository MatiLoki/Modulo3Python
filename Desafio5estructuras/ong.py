def piratoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

def factorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        resultado = numero * factorial(numero - 1)
        return resultado
    
def calcular(**kwargs):
    for k, v in kwargs.items():
        if 'fact_' in k:
            print(f"El factorial de {v} es {factorial(v)}")
        elif 'prod_' in k:
            print(f"La productoria de {v} es {piratoria(v)}")
        else:
            print(f"Error: '{k}' no es un argumento válido.")

def calcularF(**kwargs):
    fact_args = []
    prod_args = []
    
    for k, v in kwargs.items():
        if 'fact_' in k:
            fact_args.append(v)
        elif 'prod_' in k:
            prod_args.append(v)
    
    if fact_args:
        print("Factoriales:")
        for f in fact_args:
            print(f"El factorial de {f} es {factorial(f)}")
    
    if prod_args:
        print("Productorias:")
        for p in prod_args:
            print(f"La productoria de {p} es {piratoria(p)}")


calcularF(fact_1=5, prod_1=[3, 6, 4, 2, 8], fact_2=6)
