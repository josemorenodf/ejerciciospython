# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista=[10, 7, 3, 7, 2] # Asignación de valores a la lista, el subíndice inicial de la lista es 0.
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x] # En esta parte se recorre la lista elemento por elemento [x]
    x=x+1

print(f"Los elementos de la lista son {lista}")
print(f"La suma de todos los elementos es {suma}")