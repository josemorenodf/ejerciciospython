# Eliminar un elemento de un diccionario

d = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}
# Elimina un elemento con pop()
d.pop('uno')
print(d)

# Elimina un elemento con popitem()
d.popitem()
('cinco', 5)
print(d)

# Elimina un elemento con del
del d['tres']
print(d)

# Borra todos los elementos del diccionario
d.clear()
print(d)