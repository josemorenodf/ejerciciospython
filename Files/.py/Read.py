import os
os.system('cls')

# Método open para abrir el archivo. Para evitar errores de escape se coloca la letra r al inicio de la ruta.

archivo = open(r"C:\Users\user\Dropbox\Mi PC (DESKTOP-MHI3HB6)\Documents\Python\Files\.txt\datos.txt")

print("****************")
print()
# Leer los datos del archivo.
print("metodo.read()")
print()
print(archivo.read()) 



