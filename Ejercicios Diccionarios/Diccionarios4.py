# El diccionario define una relación uno a uno entre {claves y valores}.

productos={"manzanas":39, "peras":32, "lechuga":17} 
print("Diccionario completo")
print(productos) 
print("Accediendo a los valores de un diccionario")
y = productos["peras"]
print(y) 
print("Recorriendo cada elemento del diccionario")
for clave in productos: # clave puede ser cualquier variable ej. i, j, k 
    print(f"La clave: {clave} , su referencia es: {productos[clave]}")

print("Diccionario vacío:")
d5 = {} #Diccionario vacío
print(d5)

print("Añadir elementos a un diccionario en Python:")
d = {'uno': 1, 'dos': 2}
print(d)
d['tres'] = 3 #Añadir elementos a un diccionario en Python
print(d)

print("La longitud del diccionario productos es:",len(productos))