print ("estoy intentando hacer esto funcionar")

#paso  1, obtener el numero mayor entre 2
print ("Ingrese dos numeros a encontrar MCD (PD: su orden no importa, se seleccionará el mayor")
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

msj1 = numero1
msj2 = numero2

if (numero2 > numero1):
    change = numero1
    numero1 = numero2
    numero2 = change

#paso 2, modulo

resto = numero1 % numero2
mcd = 0
while mcd == 0:
    if resto != 0:
        numero1 = numero2
        numero2 = resto
    else:
        mcd = numero2
    resto = numero1 % numero2

print (f"El mcd entre {numero1} y {numero2} es {mcd}")