#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
#Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
#Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
vegetariana = input("¿Quiere una pizza vegetariana? (si/no): ")
vegetariana = vegetariana.lower()
while vegetariana != "si" and vegetariana != "no":
    print("No ha selecionado una pizza valida")
    vegetariana = input("¿Quiere una pizza vegetariana? (si/no): ")
    vegetariana = vegetariana.lower()
if vegetariana == "si":
    print("Ingredientes disponibles: Pimiento y Tofu")
    ingrediente = input("¿Que ingrediente desea añadir? (Pimiento/Tofu): ")
    ingrediente = ingrediente.lower()
    while ingrediente != "pimiento" and ingrediente != "tofu":
        print("No ha introducido un ingrediente valido")
        ingrediente = input("¿Que ingrediente desea añadir? (Pimiento/Tofu): ")
        ingrediente = ingrediente.lower()
    print("Su pizza vegetariana con mozzarella, tomate y "+ingrediente+ " está en el horno")
else:
    print("Ingredientes disponibles: Peperoni, Jamon y Salmon")
    ingrediente = input("¿Que ingrediente desea añadir? (Peperoni/Jamon/Salmon): ")
    ingrediente = ingrediente.lower()
    while ingrediente != "peperoni" and ingrediente != "jamon" and ingrediente != "salmon":
        print("No ha introducido una respuesta valida")
        ingrediente = input("¿Que ingrediente desea añadir? (Peperoni/Jamon/Salmon): ")
        ingrediente = ingrediente.lower()
    print("Su pizza no vegetariana con mozzarella, tomate y "+ingrediente+ " está lista")