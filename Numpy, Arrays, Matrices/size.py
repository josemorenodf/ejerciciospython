import numpy as np

# .size permite conocer cuantos elementos hay en un array 
a = np.array([2,3,4]) # Arrays Unidimensionales: Vectores
b = np.array([[2,5,1],[6,5,3],[9,8,2]]) #Arrays Multidimensionales o Matrices
print("1D Array")
print(a)
print()
print("2D Array")
print(b)
print("Numero de elementos en a:", a.size)
print("Numero de elementos en b:", b.size)