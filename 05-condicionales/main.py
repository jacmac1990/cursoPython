#condicional IF
"""
print("ejemplo 1")\

#color = "rojo"
color = input("ingrese un color: ")

if color == "rojo":
    print("el color es rojo")
else:
    print(f"El color no es {color}")

"""

#operadores de comparacion

"""
== igual
!= diferente
< menor que 
> mayor que
<= menor o igual que
>= mayor o igual que

operadores logicos:
and y 
or O
! negacion 
not NO

"""
"""
print("\n------------EJEMPLO 2----------")

#year = 2022
year = input("en que anio estamos: ")

if int(year) >= 2022:
    print("estamos en el anio 2022")
else:
    print("es un anio anterior al 2022")   


print("\n------------EJEMPLO 3----------")

nombre = "Jonathan"
ciudad = "La Serena"
pais = "Chileno"
edad = 36
mayoria_edad = 18
if edad >= mayoria_edad:
    print(f"{nombre} Es mayor de edad")

    if pais != "Chileno":
        print(f"{nombre} No es Chileno")
    else:
        print(f"{nombre} Es Chileno de la ciudad de {ciudad}")    

else:
    print(f"{nombre} No es mayor de edad")
"""
"""
print("\n------------EJEMPLO 4----------")

dia = int(input("ingrese dia de la semana : "))
"""
"""
if dia == 1:
    print("es lunes")
else:
    if dia == 2:
        print("es Martes")
    else:
        if dia == 3:
            print("es Miercoles")
        else:
            if dia == 4:
                print("es Jueves")
            else:
                if dia == 5:
                    print("es Viernes")
                else:
                    if dia == 6:
                        print("es Sabado")
                    else:
                        if dia == 7:
                            print("es Domingo")
                        else:
                            if dia > 7:
                                print("dia no valido")
"""
"""
if dia == 1:
    print("es lunes")
elif dia == 2:
    print("es Martes")
elif dia == 3:
    print("es Miercoles")    
elif dia == 4:
    print("es Jueves")  
elif dia == 5:
    print("es Viernes") 
elif dia == 6:
    print("es Sabado")
elif dia == 7:
    print("es Domingo")
elif dia > 7:
    print("Dia ingresado no es valido")

"""
"""
print("\n------------EJEMPLO 5----------")  

edad_minima = 18
edad_maxima = 65
edad_oficial = int(input("ingrese edad: "))

if edad_oficial >= 18 and edad_oficial <= 65:
    print("esta en edad de trabajar")
else:
    print("no esta en edad de trabajar")

"""
"""
print("\n------------EJEMPLO 6----------")  

pais = "chile"

if pais == "mexico" or pais == "chile" or pais == "colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")  

"""

"""
print("\n------------EJEMPLO 7----------")  

pais = "chile"

if not pais == "mexico" or pais == "chile" or pais == "colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")  


"""

print("\n------------EJEMPLO 8----------")  

pais = "chile"

if  pais != "mexico" and pais != "chile" and pais != "colombia":
    print(f"{pais} no es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")  