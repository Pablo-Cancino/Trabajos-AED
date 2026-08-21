import math

# Ingreso de datos (multiples, que se resuelvan en una sola ejecucion):
# num_legionarios = input(int()).split() --> ingreso multiple no aplicado de momento

# Calculo de escudos
# pasos:
# se obtiene el numero (ahora mismo individual)
num = int(input("Ingrese el numero de legionarios a ordenar: "))

# se simula un ciclo do-while
total_escudos = 0
while True:
    # se obtiene su raiz, se obtiene la raiz perfecta más cercana (floor) 
    cerca = math.floor(math.sqrt(num))

    # se obtiene el numero al cuadrado y luego se resta al anterior
    pcerca = cerca * cerca
    num -= pcerca

    #se calcula el perimetro del grupo actual (en base a cerca) y se le suma su potencia, ya que es el area superior
    total_escudos += cerca * 4
    total_escudos += pcerca

    # al terminar de calcular, si el resto de la operacion constante es 1, se le suma 5, que es constante para que se defienda
    if (num == 1):
        total_escudos += 5
        break

    #si no, un break
    if (num == 0):
        break

#se imprime el numero de escudos necesarios
print(f"se necesita un total de {total_escudos} escudos")

