import math

r = float (input("ingrese el radio en kilometros: \n"))
g = float (input("ingrese la constante g: \n"))

v = math.sqrt((r*1000*g)*2)
print (f"velocidad de escape : {v} [m/s]")
