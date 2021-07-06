import os
os.system('cls')

archivo = open(r"C:\Users\user\Dropbox\Mi PC (DESKTOP-MHI3HB6)\Documents\Python\Files\.txt\datos.txt","w",encoding="utf8") 

# "r" : solo lectura
# "w" : sobreescribir
# "a" : Permite escribir, conservar los datos
# "a+" : Permite escribir y leer, conservar los datos

# encoding="utf8" (caracteres especiales del español)

print("modo del archivo (r: solo lectura w: escritura a+:lectura y escritura)")
print("archivo.mode")
print("****************")
archivo.write("melon\n")  # salto de linea

"""
archivo.seek(0)  # leer el cursor al principio
print("Recorrido con ciclo for loops")
for i in archivo.readlines():
    print(i,end="")
print("****************")
encoding = archivo.encoding
print(encoding)
"""