from string import ascii_lowercase

password = "maria"
contador = 0




for letra in password:
    for elemento in ascii_lowercase:
        contador = contador+1
        
        if letra == elemento:
            break
print(contador)