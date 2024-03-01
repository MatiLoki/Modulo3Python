#solicitud de datos por pantalla
p = float (input("Ingrese el peso en kilogramos: \n"))
a = float (input("Ingrese la altura en cm: \n"))
#calculo de im
imc = float(p/(a*a))
#Si condicional de clasificacion de la OMS
if (imc < 18.5) :
    clasificacion = "Bajo peso"
elif (18.5 <= imc <=24.9) :
    clasificacion = "Adecuado"
elif (25.0 <= imc <=29.9) :
    clasificacion = "Sobre Peso"
elif (30 <= imc <=34.9) :
    clasificacion = "Obesidad grado 1"
elif (35 <= imc <=39.9) :
    clasificacion = "Obesidad grado 2"
else :
    clasificacion = "Obesidad grado 3"

#Concatenado de print para mostrar datos
print (f"Su Imc es: {imc:.2f} , La clasificacion OMS es {clasificacion}")