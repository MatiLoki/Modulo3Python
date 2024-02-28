import math

print("Debe ingresar unicamente valores numericos incluidos numeros decimales")

P = float(input("ingrese el precio de suscripción: \n"))
U = float(input("ingrese el numero de usuarios: \n"))
GT = float(input("ingrese el gasto total: \n"))
UA = float(input("ingrese las utilidades del año anterior: \n"))

utilidades = (P*U*GT)

print(f"las utilidades del proyecto actual son: {utilidades:.1f}", f"y la razon entre los dos años es {utilidades/UA}")
