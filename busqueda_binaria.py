def busqueda_binaria_primera(arr, target):
    lo = 0
    hi = len(arr) - 1
    resultado_index = -1

    while lo <= hi:
        #se calcula el punto medio del arreglo sin hacer que de error
        mid = lo + (hi - lo) // 2
        if arr[lo] == target:
            return lo

        #se revisa que no estémn en las posiciones iniciales de lo/hi
        elif arr[hi] == target:
            return hi

        #se revisa si está en medio del arreglo
        elif arr[mid] == target:
            return mid - 1 #retorna el --> [indice] <--  donde se encuentra target
        
        #se aplica la lógica de "descartar" uno de los lagos del arreglo
        elif arr[mid] < target:
            lo = mid + 1
            
        else:
            hi = mid - 1
            
    return resultado_index

a = [2, 5, 8, 12, 12, 12, 16, 23, 38]
print("Índice esperado para 12: 3. Tu resultado:", busqueda_binaria_primera(a, 12))

b = [5, 5, 5, 5, 5]
print("Índice esperado para 5: 0. Tu resultado:", busqueda_binaria_primera(b, 5))