# Crear un nuevo diccionario desde las claves de una secuencia

secuencia = ["color", "talla", "marca"]
diccionario1 = dict.fromkeys(secuencia)
print(diccionario1) # Determina que las claves no tienen valor, por lo que su valor es 'None'
diccionario2 = dict.fromkeys(secuencia, 'valor x defecto')
print(diccionario2) # Indica un valor a la clave