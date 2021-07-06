import numpy as np

# Convertir listas en arrays

TempC = [10,12,15,23,25,35,26]  # Lista de temperaturas
arrayTemp = np.array(TempC) # Pasa los datos de la lista al arreglo
print("Se muestran los elementos guardados en el arreglo unidimensional")
print(arrayTemp)
b = np.array([[2,5,1],[6,5,3],[9,8,2]]) # Arrays Multidimensionales o Matrices
arrayb =  np.array(b)
print("Se muestran los elementos guardados en el arreglo matriz")
print(b)