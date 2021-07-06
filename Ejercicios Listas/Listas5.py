# Definir una lista vacía y luego solicitar la carga de 5 enteros por teclado y añadirlos a la lista.        Imprimir la lista generada.

lista=[] # Disponemos un ciclo de 5 vueltas 
for x in range(5): # Valor final + 1, la lista comienza en 0 (su primer subíndice) 
    valor=int(input(f"Ingrese el valor entero {x+1}: ")) 
    lista.append(valor) # Se imprime la lista 

print(f"Los elementos de la lista son: {lista}") 