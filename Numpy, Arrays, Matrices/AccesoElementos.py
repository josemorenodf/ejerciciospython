import numpy as np

# 1. Acceso a vectores y sus elementos

A = np.array([2,4,6,8,10])

print("A[0]=", A[0])
print("A[2]=", A[2])
print("A[-1]=", A[-1])

# 2. Acceso a matrices, filas y elementos

A = np.array([[2,4,6,8,10],
              [-5,8,9,0],
              [-6,7,11,19]])

# Primer elemento de la primera fila
print("A[0][0]=", A[0][0])

# Tercer elemento de la segunda fila
print("A[1][2]=", A[1][2])

# Último elemento de la tercera fila
print("A[-1][-1]=", A[-1][-1])

# 3. Acceso a matrices y columnas

A = np.array([[1,4,5,12,],
              [-5,8,9,0],
              [-6,7,11,19]])

# Primera columna
print("A[:,0]=", A[:,0])

# Cuarta columna
print("A[:,3]=", A[:,3])

# Última columna
print("A[:,-1]=", A[:,-1])