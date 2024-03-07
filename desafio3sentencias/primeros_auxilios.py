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
       