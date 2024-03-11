text=open("lorem_ipsum.txt", "r") 
texto=text.read()

def contar_caracteres_distintos(texto):
    caracteres_distintos = set(texto)
    return len(caracteres_distintos)

def contar_palabras_distintas(texto):
    palabras = texto.split()
    palabras_distintas = set(palabras)
    return len(palabras_distintas)

num_caracteres_distintos = contar_caracteres_distintos(texto)
num_palabras_distintas = contar_palabras_distintas(texto)
print(f"El número de caracteres distintos: {num_caracteres_distintos}")
print(f"El número de palabras distintas: {num_palabras_distintas}")
