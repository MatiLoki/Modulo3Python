import math

print("Debe ingresar unicamente valores numericos incluidos numeros decimales")

P = float(input("ingrese el precio de suscripción: \n"))
UN = float(input("ingrese el numero de usuarios normales: \n"))
UP = float(input("ingrese el numero de usuarios premium: \n"))
GT = float(input("ingrese el gasto total: \n"))

utilidades = (P*UN*GT*(UP*1.5))

print(f"las utilidades del proyecto son: {utilidades:.1f}")