cadena1 = "Hola soy Eduardo"
cadena2 = "Gracias por arender Python conmigo"
# Metodo 1). dir muestra todos los metodos de una cadena 
"""print(dir(cadena1))"""
# el resultado de dir(cadena1) incluirá: Métodos como upper(), lower(), replace(), 
# split(), etc. Estos son métodos que puedes usar para manipular la cadena. 
# Atributos como __class__, __contains__, etc., que son internos de Python y no 
# se usan comúnmente en el día a día.
# dir(cadena1) te ayuda a ver qué herramientas tienes disponibles para trabajar 
# con la cadena de texto en Python.

# Apliquemos el método upper a la función dir así:
print(cadena1.upper())

# Pasemo a minúsculas con el método lower
print(cadena1.lower())

# Convierte la primera letra en mayúsculas:
print(cadena1.capitalize())

# El siguiente método nos retornará un valor, es decir, el resultado 
# de la ejecución, queremos ver si en cadena1 se encuentra la cadena 
# Hola en este caso me devuelve 0 porque me devuelve la posición de 
# la cadena
print(cadena1.find("Hola"))

# Ahora, veamos la función, index observa que funciona igual que find 
# excepto que en una si no encuentra nada nos devuelve -1 y en esta nos 
# lanza una excepción
print(cadena1.index("a"))

# A pesar de que la línea de código 1 ahora contiene números, sigue siendo 
# una cadena de texto. No obstante, isnumeric() busca números
print(cadena1.isnumeric())

#Corroboremos si es alfa numeríco es decir letras y números con isalpha ( ) 
# Los espacios no son caracteres alfannuméricos sino especiales 
# (los especiales son espacio, #, comas, puntos)
print(cadena1.isalpha())

# Usaremos count, en este caso nos dice que la letra a solo está una vez 
# en la variable cadena1
print(cadena1.count("a"))

# Contemos cuántos caracteres tiene una cadena con el método len
print(len(cadena1))

# Usaremos ENDSWITH verifica si una cadena empieza con algo, 
# por ejemplo el caracter H:
# Lo mismo para ENDSWITH para ver si termina con n:
print("inicia con",cadena1.startswith("H"))
print("termina con",cadena1.endswith("n"))

#slide 302