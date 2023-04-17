#Un programa que me diga si el numero es primo o no
#La i es el numero que probara el for durante todo el rango
numero = int(input("Introduce un numero: "))
for i in range(2,numero):
    if numero % i == 0:
        print("No es primo")
        break
else:
    print("Es primo")
    