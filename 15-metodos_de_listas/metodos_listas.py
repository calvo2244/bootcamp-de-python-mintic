"""
Así como vimos antes métodos de cadenas, vamos a ver métodos de listas, de decir, métodos que vamos a poder aplicar a listas para operarlas.

LIST - Crea una lista #es una función
LEN - Cuenta la cantidad de elementos de una lista
APPEND - Agrega un elemento a la lista
INSERT - Agrega un elemento a la lista en el índice especificado
EXTEND - Agrega varios elementos a la lista

POP - Elimina un elemento de una lista, pide indice y devuelve valor
REMOVE - Remueve un elemento de una lista, pide valor
CELAR - Elimina todos los elementos de una lista

SORT - Ordena una lista de forma ascendente a descendente
REVERSE - Invierte los elementos de una lista
"""

lista = list(["hola ", "hector astudillo", 1981,14,3,True])
print("==> lista completa  ",lista)
# Nos devuelve la longitud de la lista (antidad de caracteres)
cadena = "Hola" 
# En este caso len nos devuelve la cantidad de caracteres del texto hola
resultado = len(cadena)
print("==> manejo de LEN contando caracteres ",resultado)
# En este caso len nos devuelve la cantidad de elementos de la lista
resultado1 = len(lista)
print("==> manejo de LEN contando campos ",resultado1)

# Agregando un elemento a la lista 
# sEl método append nos permite agregar más elementos a la lista
lista.append("Eduardo")
print("==> lista despues de append ", lista)

# Agregando un elemento a la lista en un a posicion especifica
# El método insert agrega elementos en una posición determinada.
posicion = 2
lista.insert(posicion,"Garces")
print("==> lista despues de insert en la posicion ", posicion, "==", lista)

# Agregando varios elementos a la lista  extend
lista.extend(["MINTIC", "2024"])
print("==> lista despues de EXTEND ", lista)


# Eliminando un elemento a la lista pop
print("==> cuantos elementos tiene la lista ", len(lista))
#El método pop elimina un elemento de la lista en la posición indicada
lista.pop(0)
print("==> cuantos elementos queda la lista ", len(lista))
print("==> lista despues de POP ", lista)
# Con -1 puedes eliminar el último elemento de la lista, -2 el penúltimo, etc.

# Eliminando un elemento a la lista por su valor 
lista.remove("MINTIC")
# lista.remove("cancer") // si no existe el valor genera error 
print("==> lista despues de REMOVE ", lista)

lista1 = list([1981,14,3,True, 2011, 2024, 42])
# ordena los elementos de la lista mientras la lista tenga numeros y booleanos 
# SORT - Ordena una lista de forma ascendente a descendente
print("==> lista 1  Antes de SORT ",lista1)
lista1.sort()
print("==> lista 1  despues de SORT ",lista1)

# Invierte los elementos de una lista con reverse
lista1.sort(reverse=True)
print("==> lista 1  invertida ",lista1)

# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista1.index(14)
print("==> lista 1 Con elemneto encontrado",elemento_encontrado)
