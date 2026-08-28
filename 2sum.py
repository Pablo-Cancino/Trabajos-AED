import time
import matplotlib.pyplot as plt

#Func modificada desde 2sum
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
                    count+=1
    
    return count

# Pruebas y Tiempos de Ejecución empíricos
sizes = [100, 200, 400, 800, 1600]
times = []

for size in sizes:
    arr = list(range(-size//2, size//2))
    
    # Toma el tiempo antes de comenzar, se usa time.perf_counter porque es más preciso
    start_time = time.perf_counter()
    
    two_sum_brute(arr)
    
    # Toma el tiempo al terminar, se usa time.perf_counter porque es más preciso
    end_time = time.perf_counter()
    
    times.append(end_time - start_time)

#generar grafico ??????
plt.plot(sizes, times, color='blue', linestyle='-', marker='o')
plt.title("Two Sum fuerza bruta")
plt.xlabel("Tamaño del input (N)")
plt.ylabel("Tiempo (Segundos)")
plt.grid(True)
plt.show()
