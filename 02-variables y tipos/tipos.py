nada = None
cadena = "Hola soy Jonathan"
entero = 99
decimal =  9.1
booleano = True
lista = [10, 20, 30, 40]
listastring = [44, "treinta", "cuarenta", 50]
tuplaNoCambia = ("no", "cambia", "contenido")
diccionario = {
    "nombre": "Jonathan",
    "apellido": "Ahumada"
}
rango = range(9)
dato_byte = b"probando"

#mostrar tipo de datos
print (nada, type(nada))
print (cadena, type(cadena))
print (entero, type(entero))
print (decimal, type(decimal))
print (booleano, type(booleano))
print (lista, type(lista))
print (listastring, type(listastring))
print (tuplaNoCambia, type(tuplaNoCambia))
print (diccionario, type(diccionario))
print (rango, type(rango))
print (dato_byte, type(dato_byte))

#convertir tipos de datos

texto = "hola soy un texto"
numerico = str(100)
print(texto + numerico)
numerico = int(100)
print (numerico, type(numerico))
numerico = float(100)
print (numerico, type(numerico))

