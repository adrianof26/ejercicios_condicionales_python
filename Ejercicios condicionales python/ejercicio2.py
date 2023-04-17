#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = input("Introduzca la contraseña: ")
contraseña2 = input("Introduzca de nuevo su contrasñea para verificarla: ")
contraseña = contraseña.lower()
contraseña2 = contraseña2.lower()
if contraseña == contraseña2:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
