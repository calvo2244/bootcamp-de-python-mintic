diccionario = {
    "nombre" : "Hector",
    "apellido" : "Astudillo",
    "telefono" : 3008880519,
    "cena" : False
    }

# keys() Nos muestra las claves del diccionario
claves = diccionario.keys()
print("=> keys ", claves)

# get() es un método que puede acceder a una propiedad particular de un objeto
claves = diccionario.get("telefono")
print("=> get(telefono) ", claves) #3008880519
claves = diccionario.get("abcdef")
print("=> get(abcdef) ", claves) # nonenos indica que no tiene valor 

# pop te permite eliminar un elemento
diccionario.pop("apellido")
print("=> pop(): ", diccionario)

# elima todo el diccionario 
#dicionario.clear()
#print("=> clear() : ", dicionario)

# Iterar o recorrer un elemento significa pasar por cada uno de sus 
# componentes para realizar una acción. En el contexto de un diccionario, 
# iterar implica recorrer todas las claves y valores del diccionario 
# para acceder a ellos y hacer algo con cada par clave-valor

diccionario_iterable = diccionario.items()
print("=> items(): ", diccionario_iterable) # iterar es recorrer el elemento