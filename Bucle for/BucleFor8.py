# Usando la función range()

'''
print("Comienzo")
for i in range(3):
    print("Hola " , end="")
print()
print("Final")
'''

# El usuario decide cuántas veces se ejecuta el bucle

veces = int(input("¿Cuántas veces quieres que te salude?\n"))
for i in range(veces):
    print("Hola " , end="")
print()
print("Adiós")