# Concatenar diccionarios

diccionario1 = {"color": "verde", "precio": 45}
diccionario2 = {"talla": "M", "marca": "Lacoste"}
diccionario1.update(diccionario2) # El diccionario 1 toma los elementos del diccionario 2 y los integra para construir sólo un diccionario
print(diccionario1)