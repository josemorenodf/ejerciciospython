#Crear una lista por asignación con 5 enteros. Eliminar el primero, el tercero y el último de la lista.

lista=[10, 20, 30, 40, 50]

print(lista)

"""

lista.pop(0)
print(f"Primer elemento borrado: {lista}")
lista.pop(1)
print(f"Segundo elemento borrado: {lista}")
lista.pop(2)
print(f"Tercer elemento borrado: {lista}")

print("-------------------------------")

"""

lista.pop(4)
print(f"Primer elemento borrado: {lista}")
lista.pop(2)
print(f"Segundo elemento borrado: {lista}")
lista.pop(0)
print(f"Tercer elemento borrado: {lista}")