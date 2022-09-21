"""
#BLUCLE WHITE
ESTRUCTURA DE CONTROL QUE INTERA O REPUTE LA EJECUCION
 DE UNA SERIE DE ISNTRUCCIONES TANTAS VECES COMO SEA NECESARIO, 
 HASTA QUYE DEJE DE CUMPLIRSE LA CONDICION

while condicion:
    bloque de instrucciones
    actualizacion de contador
"""
"""
contador = 1

while contador <= 100:
    print(f"estoy en el numero: {contador}")
    contador += 1
"""
"""
contador = 1
muestrame = str(0)

while contador <= 10:
    muestrame = muestrame + ", " + str(contador)
    contador = contador + 1
    
print(muestrame)

"""

numero_usuario = int(input("Ingrese numero para multiplicar: "))

if numero_usuario < 1:
    numero_usuario = 1

print(f"Tabla del {numero_usuario}")

contador = 1
while contador <= 10:
    print(f"{numero_usuario} x {contador} = {numero_usuario*contador} ")
    contador += 1
else:    
    print("proceso terminado")
