# Se le llaman variables porque pueden variar, por ejemplo intenta reemplazar 
# el 5 por otro valor y el 8 y vuelve a imprimir código. 
# Con Ctl J puedes ocultar o visualizar la terminal."""

a = 5
b = 8
c = a + b
print("=> Resultados de la operacion a y b:  ",c)


# Intenta imprimir tu nombre y apellido y luego quitar tu apellido 
# de la variable nombre y vuelve a imprimir . """

nombre = "Hector Eduardo "
print("=> Imprime lo que contiene variable nombre:  ",nombre)


# Las variables como su nombre lo dice, pueden variar.
# luego intenta hacer 
numero = 10 # Primero ejecuta esta linea de codigo e imprime 10
# Existe un término en programación llamado concatenar
#Concatenar viene de cadena, es decir unir
numero = numero + 1 # Luego ejecuta esta linea e imprime el 11
numero += 5 # la mejor forma de ralizarlo 
# El valor + adelante del igual siginifica:
# El valor que ya tiene mas lo que este despues del igual 
# Así como podemos sumar también podemos restar
print("=> Resultado variable numero: ",numero)

# Estos son los f strings. Para concatenar de esta forma 
# simplemente ponemos una f adelante.
nombre2 = "Hector Eduardo Astudillo"
bienvenida = f"Hola {nombre2} feliz noche"
print("=> Impresion con f string: ", bienvenida)

# Luego intenta borrar la variable bienvenida
#del bienvenida # Borramos la variable, es decir , que ya no esta mas declarada
#print("=> Impresion variable elimnada: ", bienvenida) # sale error por que no se encuentra 

""" Practiquemos el in y el not int"""
# in sirve para ver si una cadena se encuentra dentro de otra
print("ola" in bienvenida) #True
# not in sirve para ver si una cadena no se encuentra dentro de otra
print("Betty" not in bienvenida) #True
print("Hola" not in bienvenida) # False

#CamelCase
nombreCompletoDeTuProfe = "Hector Eduardo Astudillo"

#SnakeCase es la que debemos utilizar en Python
nombre_completo_de_tu_profe = "Hector Eduardo Astudillo"









