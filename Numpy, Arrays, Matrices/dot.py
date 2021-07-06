import numpy as np

# .dot ejecuta una multiplicación de matrices

a = np.array([[-2,-6],[-4,-3],[5,0],[4,-6]])
b = np.array([[2,-2,2],[-2,0,-3]])
print("Matriz A")
print(a)
print()
print("Matriz B")
print(b)
print()
print("La multiplicacion es A * B:")
print(a.dot(b))