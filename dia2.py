#hola esto es un comentario
#los comentarios son ignorados
print("hola mundo")
""" este es un comentario de mas de una linea
son ignorados completamente
"""
numero = 2
print(numero)
print(2+2)
print(3.5+10)
print("la cantidad de letras 'a' que tiene santana es:")
print("santana" .count("a")) #este print cuenta la cantidad de letras A
print("santana" .upper()) #este print transforma en negritas

frase = "holA mundo COMo Estan"
frase_mayuscula = (frase.upper())
print(frase.upper()) #metodo upper case mayusculas
print(frase.lower()) #metodo lower case minusculas

print(frase_mayuscula.count("O")) #metodo para contar letras no diferencia si son mayusculas o minusculas debes transformar todas

lista = ["pera", "manzana", "pan", "queso"]
print("-".join(lista))
 
nombre = "Matias"
apellido = "Fernandez"
apellido_2 = "SanMartin"

print("Mi nombre es {} {} {}".format(nombre, apellido, apellido_2))
 
print(f"Mi nombre es {nombre} {apellido} {apellido_2}") #f-string segundo metodo concatenado
print(f"{10/3:.4f}")



