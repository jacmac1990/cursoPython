"""
ejercicio 6, mostrar todas las tablas de multiplicar del 1 al 10 
Mostrando el titulo de la tabla y ;luego las multiplicaciones.

"""

contador = 0
resultado = 0

for contador in range(1,11):
    print(f"Tabla del {contador}")
    for resultado in range(1,11):
        print(f"{contador} x {resultado} = {contador * resultado}")           
    
