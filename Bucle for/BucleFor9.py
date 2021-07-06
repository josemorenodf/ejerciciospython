# Testigo
'''
Variable que indica simplemente si una condición se ha cumplido o no. Es un caso particular de contador, 
pero se suele hacer con variables lógicas en vez de numéricas.
'''

print("Comienzo")
encontrado = False
for i in range (1,6):
    if i%2 == 0:
        encontrado = True
if encontrado:
    print(f"Entre 1 y 5 hay al menos un múltiplo de 2.")
else:
    print(f"Entre 1 y 5 no hay ningún múltiplo de 2.")