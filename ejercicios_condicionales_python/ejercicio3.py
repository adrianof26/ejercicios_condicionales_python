#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
numero1 = input("Introduce el primer numero: ")
numero2 = input("Introduce el segundo numero: ")
numero1 = int(numero1)
numero2 = int(numero2)
if numero2 == 0:
    print("error")
else:
    print(numero1/numero2)