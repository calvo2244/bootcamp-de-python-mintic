#Operadores de comparación 
es_igual_que = 5 == 5
print("=> igual que: ",es_igual_que)

es_diferente = 5 != 6
print("=> Diferente: ",es_diferente)

es_mayor_que = 5 > 6
print("=> Mayor que: ",es_mayor_que)

es_mayor_igual_que = 5 >= 6
print("=> Mayor igual que: ",es_mayor_igual_que)

es_menor_que = 5 < 6
print("=> Menor que: ",es_menor_que)

es_menor_igual_que = 5 <= 6
print("=> Menor igual que: ",es_menor_igual_que)

#Calculos combinados
a = 5
b = 10
c = 20
comparacion = a + b == c
print("=> Comparacion combinadas: ",comparacion)

#Comparar usuarios
contrasena_almacenada = "123456"
contrasena_escrita = "123456"

print(contrasena_almacenada == contrasena_escrita) #True

contrasena_almacenada = "123456"
contrasena_escrita = '123456'
print(contrasena_almacenada == contrasena_escrita) #True

contrasena_almacenada = "123456"
contrasena_escrita = '''123456'''
print(contrasena_almacenada == contrasena_escrita) #True