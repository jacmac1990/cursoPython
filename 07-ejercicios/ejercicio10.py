"""
el programa tien que ppedir la notra de 15 alumnos y
sacar por pantalla cuantos ha apriobado y cuantos han suspendido 

"""
import random
contador = 0


for contador in range(1,15+1):
    notas = random.randint(1,7)
    print(f"alumno {contador} promedio {notas}")
    if notas >= 4:
        print("Aprobado")
    else:
        if notas < 4:
            print("Reprobado")    