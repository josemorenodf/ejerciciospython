# Listas y funciones
# La función sum() solamente funciona cuando los elementos de la lista son números. Las otras funciones (max(), len(), etc.) funcionan con listas de cadenas y otros tipos que pueden ser comparados entre sí.

t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

print("Longitud de la lista:",len(t))
print("La suma es:",sum(t)) 
print("El máximo número es:",max(t)) 
print("El mínimo número es:",min(t)) 
print("El promedio es:",sum(t)//len(t))