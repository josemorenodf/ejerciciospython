import os
os.system('cls')

archivo = open(r"C:\Users\user\Dropbox\Mi PC (DESKTOP-MHI3HB6)\Documents\Python\Files\.txt\datos.txt")

print("****************")

print("Lista de datos del archivo (validar si tienen salto de lineas los datos)")
print(archivo.readlines())
archivo.seek(0) # mover el puntero hacia la primera linea del archivo del ejemplo (0)
print("Recorrido con ciclo for loops")
for i in archivo.readlines():
    print(i,end="")