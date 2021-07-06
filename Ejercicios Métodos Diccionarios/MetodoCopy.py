# Copiar un diccionario

diccionario = {"color": "violeta", "talla": "XS", "precio": 174.25}
camiseta = diccionario.copy() # Asigna los elementos de 'diccionario' a camiseta
print(diccionario)
print(camiseta)
diccionario.clear() # Vacía el diccionario
print(diccionario)
print(camiseta)
musculosa = camiseta # Asigna los elementos de 'camiseta' a 'musculosa'
print(camiseta)
print(musculosa)
camiseta.clear() # Vacía el diccionario 'camiseta' y también 'musculosa' porque no se usó el método .copy
print(camiseta)
print(musculosa)