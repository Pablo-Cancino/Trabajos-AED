while True:
    veces = int(input("Ingrese la cantidad de veces a imprimir hola mundo (entre 0 y 5)"))
    if (veces >= 0 or veces <= 5):
        break

for i in range(veces):
    print ("¡Hola Mundo!")

