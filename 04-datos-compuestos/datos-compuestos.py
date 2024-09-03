# LISTA []
# El primer tipo de dato compuesto que veremos será la lista
lista = ["Hector Astudillo", "mintic 2024 ", True, 1.71]
print("=> lista Completa: ",lista)
#En el mundo de la programacionno contamos del 1 a el 10, contamos del 0 al 9
print("=> Lista en la posicion [0]: "+ lista[0])
lista[3] = "otro dato" #modifica la posicion 3
print("=> Lista [3]: ",lista[3])

# TUPLA ()
# La tupla es una lista que no se puede modificar
tupla = ("Hector Astudillo", "Mintic 2024", True, 1.71)
print("=> Tupla [1]",tupla[1])
# Mientras que la lista se puede modificar, la tupla no
#tupla[1] = "Tips TIC al paso"  #Error 
#print(tupla[1])

# Creando un conjunto o set {}
# Un conjunto no admite elementos duplicados
conjunto = {"Hector Astudillo", "Mintic 2024", True, 1.71, 1.71,"Hector Astudillo"}
# Puedes imprimir un conjunto pero no acceder a uno de sus índices
print ("==> Conjunto:  ",conjunto)

#DICCIONARIO {}
# Creando un diccionario
# La estructura del diccionario es clave:valor o en ingles key:value
diccionario = {
    "nombre": "Hector Eduardo",
    "apellido" : "Astudillo",
    "estatura" : 1.71,
    "esta feliz" : True
}
# Diccionario muestra por el nombre associado, es decir , muestrame lo que tienes
# en el valor nombre 
print("==> diccionario:  ",diccionario["nombre"])
print("==> diccionario:  ",diccionario["esta feliz"])
print("==> diccionario:  ",diccionario["apellido"])
print("==> diccionario:  ",diccionario["estatura"]+2)






