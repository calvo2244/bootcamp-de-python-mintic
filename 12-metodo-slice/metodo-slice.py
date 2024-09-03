a = [1,2,3,4,5]
b = a

print("1: " , a)
print("2: " , b)
del a[0]
print("3: " , a)
print("4: " , b) # el valor de a es el mismo que b porque 
                 # apuntan a el mismo espacio de memoria
                 
print("5: " , id(a)) # id de la lista a
print("6: " , id(b)) # id de la lista b

c = a [:] # slice de la lista a la lista c
print("7: " , id(a))
print("8: " , id(b))
print("9: " , id(c)) # ya estamos accediendo a lugares deferentes en memoria 

a.append(6)
print("10: " , a)
print("11: " , b)
print("12: " , c)