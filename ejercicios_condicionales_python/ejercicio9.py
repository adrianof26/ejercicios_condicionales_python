#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
edad = int(input("Introduce tu edad: "))
while edad < 0:
    print("No puedes tener una edad negativa")
    edad = int(input("Introduce tu edad: "))
if edad < 4:
    print("La entrada para los menores de edad es gratuita")
elif edad >= 4 and edad <= 18:
    print("La entrada te costara 5€")
elif edad > 18:
    print("La entrada te costara 10€")