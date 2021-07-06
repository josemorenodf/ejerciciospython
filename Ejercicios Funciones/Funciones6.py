# Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.

from typing import List


def carga_lista():
    List=[]
    for x in range(5):
        valor=int(input("Ingrese valor: "))
        List.append(valor)
    return List


def imprimir_mayor10(List):
    print("Elementos de la lista mayores a 10:")
    for x in range(len(List)):
        if List[x]>10:
            print(List[x])


# bloque principal del programa

lista=carga_lista()
imprimir_mayor10(lista)