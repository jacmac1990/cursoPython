"""
pedir 2 numero al usuario y hacer operaciones basicas.

"""

numero1 = int(input("ingrese numero 1: "))
numero2 = int(input("ingrese numero 2: "))

if numero2 == 0:
    print("no se puede dividir por 0")
else: 
    print(f"la suma de {numero1} + {numero2} = {numero1+numero2}")
    print(f"la resta de {numero1} - {numero2} = {numero1-numero2}")
    print(f"la multiplicacion de {numero1} * {numero2} = {numero1*numero2}")
    print(f"la division de {numero1} / {numero2} = {numero1/numero2}")