lista = list(["hola ", "hector astudillo", 1981,14,3,True])
print("impresion lista completa ==> ",lista)
# Nos devuelve la longitud de la lista (antidad de caracteres)
cadena = "Hola" 
resultado = len(cadena)
resultado1 = len(lista)
print("manejo de LEN contando caracteres ==> ",resultado)
print("manejo de LEN contando campos ==> ",resultado1)

# Agregando un elemento a la lista 
lista.append("Eduardo")
print("imprimimos la lista despues de append==>", lista)

# Agregando un elemento a la lista en un a posicion especifica
posicion = 2
lista.insert(posicion,"Garces")
print("imprimimos la lista despues de insert en la posicion ", posicion, "==>", lista)

# Agregando varios elementos a la lista 
lista.extend(["MINTIC", "2024"])
print("imprimimos la lista despues de EXTEND==>", lista)


# Eliminando un elemento a la lista
print("cuantos elementos tiene la lista ", len(lista))
lista.pop(0)
print("cuantos elementos queda la lista ", len(lista))
print("imprimimos la lista despues de POP ", lista)

# Eliminando un elemento a la lista por su valor 
lista.remove("MINTIC")
# lista.remove("cancer") // si no existe el valor genera error 
print("imprimimos la lista despues de REMOVE ", lista)

lista1 = list([1981,14,3,True, 2011, 2024, 42])
# ordena los elementos de la lista mientras la lista tenga numeros y booleanos 
print("imprimimos la lista 1  Antes de SORT ",lista1)
lista1.sort()
print("imprimimos la lista 1  despues de SORT ",lista1)

lista1.sort(reverse=True)
print("imprimimos la lista 1  invertida ",lista1)

# Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista1.index(14)
print("imprimimos la lista 1 Con elemneto encontrado",elemento_encontrado)
