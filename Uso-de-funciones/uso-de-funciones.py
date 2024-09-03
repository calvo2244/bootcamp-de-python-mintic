# Uso de Funciones en Python

# definimos una funcion llamada greet
def greet():
    #dentro de la funcion, usamos print para mostrar "Hola mundo en la consola"
    print("funcion 1 => Hola Mundo") 

greet()

# enviando parametros
def greet2(name, last_Name):
    #dentro de la funcion, usamos print para mostrar "Hola mundo en la consola"
    print("funcion 2 => Hola",name, last_Name) 

greet2("Hector","astudillo")
greet2("Eduardo","garces")

# si no tiene un parametro
def greet3(name, last_Name="NO tiene apellido"):
    #dentro de la funcion, usamos print para mostrar "Hola mundo en la consola"
    print("funcion 3 => Hola",name, last_Name) 

greet3("Hector","astudillo")
greet3("Eduardo")