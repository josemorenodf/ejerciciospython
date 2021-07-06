archivo = open("datos.txt","w",encoding="utf8") # , encoding="utf8"
print(archivo)

cosa = "x\ny"
print(cosa)
print(len(cosa))

man_archivo = open("datos.txt")
contadora = 0
for line in man_archivo:
    contadora += 1
print("Contador de líneas:",contadora)

man_archivo.seek(0)
print("***************")
inp = man_archivo.read()
print(inp)
print("***************")
print(inp[:10])