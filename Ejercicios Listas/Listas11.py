#Crear una lista por asignación. La lista tiene que tener cuatro elementos. Cada elemento debe ser una lista de 3 enteros.         Imprimir sus elementos accediendo de diferentes modos.

lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]

# Imprime la lista completa
print(lista)
print("---------")

# Imprime el primer componente de la lista
print(lista[0])
print("---------")

# Imprime el segundo elemento del segundo componente de la lista
print(lista[1][1])
print("---------")

# Imprime con un for la lista contenida en el segundo componente
for x in range(len(lista[0])):
    print(lista[1][x])
print("---------")

# Imprime cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])