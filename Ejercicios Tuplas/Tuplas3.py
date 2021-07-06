# Definir una tupla con tres valores enteros. Convertir el contenido de la tupla a tipo lista. 
# Modificar la lista y luego convertir la lista en tupla.

fechatupla1 = (25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista = list(fechatupla1) # Función list(tupla) convierte la información de la tupla a una lista
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0] = 31
print("Imprimimos la lista ya modificada")
print(fechalista)
fechatupla2 =tuple (fechalista) # Función tuple(lista) convierte la información de la lista a una tupla
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)