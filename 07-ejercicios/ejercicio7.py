"""
hacer un programa que muestre todos los numero impares
entre dos numero que decida el usuario

"""

numero1 = int(input("Ingrese numero 1: "))
numero2 = int(input("Ingrese numero 2: " ))


for contador in range(numero1,numero2):
    resultado = contador % 2 
    if  resultado == 0:
        pass #no hace nada
    else:
        if resultado > 0:
            print(contador)
