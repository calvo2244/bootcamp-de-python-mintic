# Python es un lenguaje ordenado Ejecuta de arriba a abajo y de izquierda a derecha
name = "Hector"
print("=> tipo dato", type(name)) # Consultar tipo de dato

#Consulta la posición de un caracter
name0 = "Hector"
print("=> posicion 0: ",name0[0])
print("=> posicion 1: ",name0[1])
print("=> posicion 2: ",name0[2])
# Si quieres ir del final hacia la derecha harías esto:
print("=> Ultimo caracter: ",name[-1])

# repetición
name1 = "Hector Eduardo"
last_name1 ="Astudillo Garces"
print("=> Cantidad repeticiones: ",5 * name1)
#Para generar espacio al imprimir la repetición:
print("=> Espacio en repeticion: ",5 * (last_name1 + " "))

# Conteo
name2 = "Hector Eduardo"
last_name2 ="Astudillo Garces"
#len es una función incorporada en Python que se utiliza 
# para obtener la longitud (el número de elementos) de un objeto. 
# Es una función muy común y útil en la programación.
print("=> cantidad elementos: ",len(name2))
print("=> cantidad elementos: ",len(last_name2))

# El método lower (a minúscula)
name3 = "Hector Eduardo"
# lower es un método en Python que se usa para convertir todos 
# los caracteres de una cadena de texto (string) a minúsculas. 
print("=> elementos en minuscula: ",name3.lower())

# El método upper(a mayúscula)
name4 = f"Hector Eduardo"
# El método upper en Python es un método de las cadenas de texto 
# que convierte todos los caracteres de la cadena a mayúsculas. 
# Al igual que lower, es un método que se aplica a objetos de tipo str.
print("=> elementos en Mayuscula: ",name4.upper())

# El método strip (elimina espacios)
name5 = f"            Hector      Astudillo         "
#El método strip en Python es un método de las cadenas de texto 
# que se utiliza para eliminar los espacios en blanco 
# (u otros caracteres especificados) al inicio y al final de una cadena.
print("=> Sin espacio inicio y final: ",name5.strip())