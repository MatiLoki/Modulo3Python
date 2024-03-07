from string import ascii_lowercase

print(ascii_lowercase)

password = "gato"
contador = 0

for letra in password:
    for elemento in ascii_lowercase:
        contador = contador+1
        
        if letra == elemento:
            break
print(contador)