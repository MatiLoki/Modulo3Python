import random

print("Bienvenido al juego Piedra, Papel o Tijera \n")

pc=random.choice(("piedra","papel","tijera"))

v=input("ingrese piedra, papel o tijera: \n")
v=v.lower()

if (v!="piedra" and v!="papel" and v!="tijera") :
    v=input("Argumento inválido: debe ser piedra , papel o tijera")

if v!=pc :
    if v==("papel") and pc==("tijera") :
        print(f" Tu jugaste papel \n", "Computador jugo tijera \n" , "Perdiste!! \n")
    if v==("papel") and pc==("piedra") :
        print(f" Tu jugaste papel \n", "Computador jugo piedra \n" , "Ganaste!! \n")
    if v==("papel") and pc==("papel") :
        print(f" Tu jugaste papel \n", "Computador jugo papel \n" , "Empate!! \n")
    if v==("piedra") and pc==("papel") :
        print(f" Tu jugaste piedra \n", "Computador jugo papel \n" , "Perdiste!! \n")
    if v==("piedra") and pc==("tijera") :
        print(f" Tu jugaste piedra \n", "Computador jugo tijera \n" , "Ganaste!! \n")
    if v==("piedra") and pc==("piedra") :
        print(f" Tu jugaste piedra \n", "Computador jugo piedra \n" , "Empate!! \n")
    if v==("tijera") and pc==("piedra") :
        print(f" Tu jugaste papel \n", "Computador jugo piedra \n" , "Perdiste!! \n")
    if v==("tijera") and pc==("papel") :
        print(f" Tu jugaste papel \n", "Computador jugo papel \n" , "Ganaste!! \n")
    if v==("tijera") and pc==("tijera") :
        print(f" Tu jugaste tijera \n", "Computador jugo tijera \n" , "Empate!! \n")
    