#se tiene una lista de numeros enteros, en donde el sistema devuelve todos los grupos de 2 que suman 0.
#input arreglo de Z
#entrega combinaciones que dan 0

def two_sum(numbers: list[int]):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i] + numbers[j] == 0):
                print (f"[{numbers[i]},{numbers[j]}]")
                
        
#numbers_input = [0, -2, 4, 2, -6, -1] --> desordenado
numbers_input = [-6, -2, -1, 0, 2, 4]
two_sum(numbers_input)