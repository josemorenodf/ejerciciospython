# Crear una lista y almacenar 10 enteros pedidos por teclado. Eliminar todos los elementos que sean iguales al número entero 5.

lista=[]

for x in range(10): 
    valor=int(input("Ingrese valor: ")) 
    lista.append(valor) 
print(f"Lista actual: {lista}") 

posicion=0 
while posicion<len(lista): 
    if lista[posicion]==5: 
        lista.pop(posicion) 
    else: 
        posicion=posicion+1 
print(f"Se eliminan de la lista los valores iguales a 5: {lista}") 