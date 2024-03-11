import sys

if len(sys.argv) != 1:
    print("python script.py")
else:
    try:
        # Ingresar las tasas de conversión como strings y luego convertirlas a float
        sol = float(input("Ingrese la tasa de conversión de CLP a Sol peruano: "))
        arg = float(input("Ingrese la tasa de conversión de CLP a Peso Argentino: "))
        dolar = float(input("Ingrese la tasa de conversión de CLP a Dólar Americano: "))

        # Ingresar el valor en CLP como string y luego convertirlo a float
        clp = float(input("Ingrese el valor en pesos chilenos a convertir: "))

        # Realizar conversiones
        valorsol = clp * sol
        valorarg = clp * arg
        valordolar = clp * dolar

        print(f"Los {clp:.0f} equivalen a:")
        print(f"{valorsol:.1f} Soles")
        print(f"{valorarg:.1f} Pesos Argentinos")
        print(f"{valordolar:.1f} Dolares")

    except ValueError:
        print("Por favor, asegúrate de ingresar valores válidos como tasas de conversión y valor en pesos chilenos.")
