import numpy as np

# np.ones crea una matriz llena de unos
print("Crear un a matriz de unos - 3  filas y 4 columnas")
unos = np.ones((3,4)) # Matriz de 3  filas y 4 columnas
print(unos)

# np.zeros crea una matriz llena de ceros
print("Crear un a matriz de ceros - 4  filas y 4 columnas")
ceros = np.zeros((4,4)) # Matriz de 4  filas y 4 columnas
print(ceros)

# np.random crea una matriz con valores aleatorios entre 0 y 1 
print("Crear una matriz aleatoria - 2 filas y 3 columnas")
aleatoria = np.random.random((2,3)) # Matriz de 2 filas y 3 columnas
print(aleatoria)