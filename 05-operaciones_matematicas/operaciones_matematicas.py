#Operaciones matemáticas
a = 10
b = 3

print("=> suma", a + b)
print("=> resta", a - b)
print("=> multiplicacion", a * b)
print("=> division", a / b)

#En Python, el operador (%) obtiene el residuo de una división
print("=> modulo", a % b)

#El siguiente signo es el doble división y el resultaod sería la parte entera
print("=> division entera", a // b)

#Potencia
print("=> potencia", a ** b)

# se le llama hacer un artificio.
a += 2
print("=> a += 2: ",a)
a *= 2
print("=> a *= 2: ",a)
a /= 2
print("=> a /= 2: ",a)
a -= 2
print("=> a -= 2: ",a)

operacion_1 = 2 + 3 * 4
print("=> Operacion 1: ",operacion_1)
operacion_2 = 2 + (3 * 4)
print("=> Operacion 2: ",operacion_2)
operacion_3 = (2 + 3) * 4
print("=> Operacion 3: ",operacion_3)
operacion_4 = (2 + 3) * (4 ** 2 ) / 8 - 1
print("=> Operacion 4: ",operacion_4)

print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)
