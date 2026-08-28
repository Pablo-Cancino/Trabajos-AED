#Func modificada desde 3sum_problem
"""
def two_sum(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] + numbers[j] == 0):
                print (f"[{numbers[i]},{numbers[j]}]")
"""               
    
#En base al lab 
import time
import matplotlib.pyplot as plt

def two_sum_brute(arr):
    count = 0
    #se usa la función modificada de arriba
    for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (arr[i] + arr[j] == 0):
                    print (f"[{arr[i]},{arr[j]}]")
                    count+=1
    pass
    
    return count

# Pruebas y Tiempos de Ejecución empíricos
sizes = [100, 200, 400, 800, 1600]
times = []

for size in sizes:
    arr = list(range(-size//2, size//2))
    
    # Toma el tiempo antes de comenzar
    start_time = 0 # TODO: Reemplazar por método real
    
    two_sum_brute(arr)
    
    # Toma el tiempo al terminar
    end_time = 0 # TODO: Reemplazar por método real
    
    times.append(end_time - start_time)

# TODO: Escribe el código para mostrar el gráfico Lineal
