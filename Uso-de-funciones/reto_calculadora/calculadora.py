# Funcion para la realizacion de la SUMA
def suma(a,b):
    return print(f"La suma de {a} + {b} es:",a + b)

# Funcion para la realizacion de la RESTA
def resta(a,b):
    return print(f"La resta de {a} - {b} es:", a - b)

# Funcion para la realizacion de la MULTIPLICACION
def multiplicacion(a,b):
    return print(f"La Multiplicacion de {a} * {b} es:", a * b)

# Funcion para la realizacion de la DIVISION
def division(a,b):
    if b == 0 :
        return print(f"La operacion de {a} / {b} no se puede realizar, Numero no se puede divir por 0")
    else:
        return print(f"La division de {a} + {b} es:", a / b)

def calculator():
    while True:
        # se crea el menu de opciones 
        print("Seleccione una Operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        # se toman la opcion del usuario 
        option = input("Ingrese su opcion (1,2,3,4,5): ")

        # validan las opciones 
        if option == "5":
            print("Saliendo de la calculadora")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                suma(num1, num2) # Envia valores para la suma
            elif option == "2":
                resta(num1, num2) # Envia valores para la resta
            elif option == "3":
                multiplicacion(num1, num2)
            elif option == "4":
                division(num1, num2)
        else:
            print("Opcion no Valida, intentar de nuevo")

calculator()