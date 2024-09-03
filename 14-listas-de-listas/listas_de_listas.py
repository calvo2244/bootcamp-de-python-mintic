matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print("=> matrix: ", matrix) #imprime la lista completa
print("=> matrix[0]: ", matrix[0]) #imprime la lista posicion[0]

# Crearemos ahora una tupla:
numbers = (1,2,3,4,5)
print("=> Tupla: ", numbers) #=> Tupla:  (1, 2, 3, 4, 5)
print("=> Tipo Dato: ", type(numbers)) # Python conoce a este tipo de dato como la clase tuple
# Las tuplas son inmutables, es decir, no podemos realizar ninguna modificación
# con ellas:
print("=> numbers[0]: ", numbers[0]) #1
#numbers[0] = 10 #error 'tuple' object does not support item assignment
