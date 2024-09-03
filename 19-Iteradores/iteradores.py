""""
Lista: my_list es simplemente una lista con los números [1, 2, 3, 4].
Iterador: Cuando usas iter(my_list), estás creando un "iterador" para esa 
    lista. Este iterador te permite pasar por los elementos de la lista uno 
    a la vez, sin necesidad de un bucle tradicional.
next(): La función next() se utiliza para obtener el siguiente elemento de 
    la lista usando el iterador. Cada vez que llamas a next(my_iter), obtendrás
    el siguiente número en la lista.
En el ejemplo, al ejecutar print(next(my_iter)), se imprime el primer 
elemento de la lista, que es 1. Si llamas a next() de nuevo, te dará 
el siguiente número, que es 2, y así sucesivamente hasta que no haya 
más elementos.
"""

# Ejemplo de como funcionan los iteradores 
#Crear una lista con algunos numeros 

my_list = [1,2,3,4]

#obtener el iterador de la lista 
# un iterador es un objeto que nos permite recorrer una coleccion (como lista ) uno por uno
my_iter = iter(my_list)

# usar el iterador para accesder a los elementos de la lista 
# la funcion next() nos da el siguiente elemento en la coleccion cada vez que se llamae 

#print(my_iter) # <list_iterator object at 0x0000019B9B9668C0>
#print(next(my_list)) # TypeError: 'list' object is not an iterator
print(my_list[0]) #1
print(next(my_iter)) #1 
print(next(my_iter)) #2
print(next(my_iter)) #3
print(next(my_iter)) #4
# print(next(my_iter)) #genera error por que no tiene mas datos la lista

# iterar cadenas de texto usando un iterador 
#crear camdena de texto
text = "hola mundo"
# crear un iterador para la cadena 
# Un iterador nos permite recorrer cada caracter de la cadena uno por uno 
iter_text = iter(text)
# iterar sobre cada caracter de la cadena usando un bucle for 
print(next(iter_text)) #h
print(next(iter_text)) #o
#for char in iter_text:
#    print(char)

#Crear un Iterador que genere numeros impares desde 1 hasta el limite
# range (1,limit+1, 2 ) genera numeros comenzando 1, con saltos de 2 ,  hasta llegar a 9
# (el limite no se incluye)
odd_iter = iter(range(1,10,2))
#usar el iterador para recorrer y mostrar cada numero impar generado
print(next(odd_iter)) #1
print(next(odd_iter)) #3
#for num in odd_iter:
#    print(num) #imprime cada nmero impar en una nueva linea

# Definir una funcion generadora 
def my_generator():
    #la palabra clave yield nos permite devolver un valor y pausar la funcion en ese punto 
    yield 1 # primer valor que se devuelve cuando se llama la funcion 
    yield 2 # primer valor que se devuelve cuando se llama la funcion 
    yield 3 # primer valor que se devuelve cuando se llama la funcion 
# usar un bucle for para iterar sobre los valores generados
for value in my_generator():
    print("funcion generadora",value)
    
#FIBONACCI
# la serie fibonacci hace referencia a que vamos a obtener un valor sumado 
# los dos anteriores [0 1 1 2 3 5 8 13 ......]

def fibonacci(limit):
    #inicializar los dos primero dos numeros de la secuencia de fibonacci
    a,b = 0,1
    # continuar generando numeros mientras "a" sea menor que el limite 
    while a < limit :
        yield a # Devolver el valor actual de "a" y pausar la ejecucion de la funcion 
        a,b = b, a + b
for num in fibonacci(10):
    print("fibonacci: ",num)
