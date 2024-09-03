
# to_do es simplemente un nombre de variable que se asigna a una lista. 
# No tiene nada especial; puedes usar cualquier nombre de variable válido.
to_do = ["Alistar la pelicula",
         "freir la mais pira",
         "preparar pasabocas"
         ]
print("=> Lista to do: ",to_do)

# Creemos otra lista llamada numbers con la siguiente información:
numbers = [1, 2, 3, 4, "cinco"]
print("=> Lista numbers: ",numbers)
print ("=> tipo dato: ",type(numbers))

# mix es una lista que contiene elementos de diferentes tipos: una cadena,
# un entero, un número de punto flotante, un valor booleano y otra lista. 
mix = ["uno", 2, 3.14, True, [1, 2, 3] ]
print("=> Lsta mix: ",mix)
print ("=> Len cuenta elementos: ",len(mix))
print("=> primer elemento: ", mix[0])
print("=> Segundo elemento: ", mix[1])
print("=> Ultimo elemento:", mix[-1])
print("=> ",mix[0:2]) # Imprime los dos primeros elementos de la lista 
print("=> ",mix[:2]) # Imprime los dos primeros elementos de la lista  
#print("=> ",mix) 
print("=> ",mix[2:]) # Imprime desde el elemento 2 hasta el final  
print("=> ",mix[2:-2]) #Imprime  desde el elemento 2 hasta el elemento -2
print("=> ",mix[2:len(mix)])

mix.append(False) # Agrega elemento a la lista 
print("=> Agrega elemento lista: ",mix) 
mix.append("Eduardo")
print("=> Agrega elemento lista: ",mix)

mix.insert(1,["a","b"]) # Insertaremos en la posición 1 la lista:
print("=> Agrega elemento lista [1]: ",mix)

print("=> Posicion de un valor: ",mix.index(3.14)) # posicion de un elemnto

# Consulta los números mayor y menor:
numbers = [1, 2, 100, 90.45, 3, 4, 5]
print("=> Lista numbers:",numbers)
print("=> Mayor:", max(numbers))
print("=> Menor:", min(numbers))
del numbers [-1]
print("=> elimina ultimo en numbers:",numbers)
del numbers [:2] # Elimina una porción de datos, de la posició n 0 a la 2 
print("=> elimina de la posicion 0 al 2:",numbers)
del (numbers) # Elimina toda la lista
#print (numbers) # error no defined