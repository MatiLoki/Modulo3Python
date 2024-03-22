from personaje import personaje
import random

print("Bienvenido a Gran Fantasia")

nombre= input("Porfavor indique el nombre de su personaje: \n")

p = personaje(nombre)

print("Oh no, Ha aparecido un Orco!")

o = personaje("orco")
posibilidad_ganar = p.get_probabilidad_ganar(o)

opcion_orco = personaje.mostrar_dialogo_opcion(posibilidad_ganar)

while opcion_orco == 1:
    numero = random.uniform(0,1)
    #resultado = ''
    resultado = 'G' if numero < posibilidad_ganar else 'P'
    #if numero< probabilidad_ganar:
    #    resultado = 'G'
    #else:
    #    resultado = 'P'
    if resultado == 'G':
        print(f"""Le has ganado al Orco, Felicidades!
              Recibiras 50 puntos de experiencia!    """)
        p.estado = 50
        o.estado = -30
    elif resultado == 'P':
        print(f"""Oh No! El Orco te ha ganado!
              Has perdido 30 puntos de experiencia! """)
        p.estado = -30
        o.estado = 50
    
    print(p.estado)
    print(o.estado)
    probabilidad_ganar = p.get_probabilidad_ganar(o)
    opcion_orco = personaje.mostrar_dialogo_opcion(probabilidad_ganar)

print('¡Has huido! El orco ha quedado atras.')