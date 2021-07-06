# Se debe crear y cargar una lista donde se almacenen 5 sueldos. Desplazar el valor mayor de la lista a la última posición

sueldos=[]
for x in range(5):
    valor=int(input(f"Ingrese sueldo {x+1}: "))
    sueldos.append(valor)

print(f"Longitud de la lista: {len(sueldos)}")
print(f"Lista sin ordenar: {sueldos}")

# Prueba de escritorio [50, 35, 15, 78, 45] <---- LISTA ORIGINAL

# x  x+1  aux  n-1  <--(longitud de la cadena 5 - 1 = 4)
# 0   1    50   4   [35, 50, 15, 78, 45]   1 repetición
# 1   2    50   4   [35, 15, 50, 78, 45]  2 repeticiones
# 2   3    50   4   [35. 15, 50, 78, 45]  3 repeticiones
# 3   4    78   4   [35, 15, 50, 45, 78]  4 repeticiones  


for x in range(len(sueldos)-1):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x] # Empleamos una variable auxiliar (aux) para el proceso de intercambio
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux

print(f"Lista con el último elemento ordenado: {sueldos}")