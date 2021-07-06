import numpy as np

# Operaciones con arrays
 
r = [10,12,15,23,25,35,26,44,55,88,100,56,89]  # Lista de temperaturas
arreglor = np.array(r) # Le aplica la operacion acada elemento al momento de mostrar en pantalla
print("Multiplicando cada dato por 10:",arreglor*10)
print("*******************")
for i in range(0,len(arreglor)-1):
    print("Valor anterior:",arreglor[i+1])
    arreglor[i+1] = arreglor[i+1]*2
    print("Valor actual:",arreglor[i+1])