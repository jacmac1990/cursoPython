"""
for variable in elemento interable (;ista, rango, etc)
    bloque de instruciciones

"""
"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("voy por el: " + str(contador))

    resultado = resultado + contador

print(f"El resultado es: {resultado}")

"""

#ejemplos tablas de multiplicar

print ("\n ############### ejemplo ##########")

numero_usuario = int(input("Ingrese numero: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"###### tabla de multiplicar del numero {numero_usuario}")
    
for numero_tabla in range (0,11):
    if numero_usuario >= 13:
        print("el numero no puede ser mayor a 13")
        break
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario * numero_tabla}")
else:
    print("tabla finalizada")


