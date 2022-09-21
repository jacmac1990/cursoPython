"""
Una duncion es un conjunto de instrucciones agrupadas 
bajo un nombre concreto que pueden reautilizarse invocando
 a la fuincion tantas veces como sea necesario

def nombreDeMiFuncion(parametro):
    #bloque / conjun to de instrucciones

como llamar a la funcion
nombreDeMiFuncion(mi_parametro)    
"""
#ejemlo 1
"""
def muestraNombres():
    print("Jonathan Ahumada")
    print("Jimmy Ahumada")
    print("Jhonny Ahumada")
    print("Yessenia Ahumada")
    print("\n")
"""
"""
muestraNombres()


#ejemlo 2

def mostrarTuNombre(nombre, edad):
    print(f"tu nombre es: {nombre}")

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        if edad < 18:
            print("eres nmenos de edad")    

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
mostrarTuNombre(nombre, edad)

"""
"""
#ejemlo 3

def tabla(numero):
    print(f"tabla de multiplical del numero: {numero}")
    
    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")
        
    print("\n")
    
tabla(115)

"""
"""
#ejemlo 4

def getEmpleado(nombre, rut = None):
    print(f"Nombre: {nombre}")

    if rut != None:
       print(f"rut: {rut}")
    
getEmpleado("jonathan")

"""
"""
#parametros opcionales y return o devolver datos 

def saludame(nombre):
    saludo = f"hola, saludos {nombre}"
    
    return saludo

print(saludame("jonathan"))

"""    
"""    
def calculadora(numero1,numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicar = numero1 * numero2
    dividir = numero1 / numero2
    
    cadena = ""
    
    cadena += "suma: " + str(suma)
    cadena += "\n"
    cadena += "Resta: "+ str(resta)
    cadena += "\n"
    cadena += "Multiplicar: "+ str(multiplicar)
    cadena += "\n" 
    cadena += "Dividir: "+ str(dividir)
    
    return cadena

print(calculadora(2,5))
 
"""  

