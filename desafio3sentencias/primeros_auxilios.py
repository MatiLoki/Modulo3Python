print("Que hacer en caso de emergencia \n")

resp=str(input("¿La persona responde a estimulos?")).lower()

if resp == "si":
    print("Valorar la necesidad de llevarlo al hospital mas cercano")

else :
    print("Abrir la via respiratoria")
    resp_1=input("¿Respira?").lower
    if resp_1=="si":
        print("Permitirle posicion de suficiente respiracion")
    else :
        print("Administrar 5 ventilaciones y llamar a ambulancia")    
       
resp_2=str(input("¿Signos de vida?")).lower()       
if resp_2 == "si":
    print("Reevaluar a la espera de la ambulancia")
    resp_3=input("¿Llego la ambulancia?").lower()
    if resp_3== "si" :
        StopIteration
else : 
    print("Administrar compresiones torácicas hasta que llegue ambulancia")
    resp_3=input("¿Llego la ambulancia?").lower()
    if resp_3=="si":
        StopIteration


