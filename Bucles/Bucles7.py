# Contador

'''
contador = 0
for valor in [3 , 41 , 12 , 9 , 74 , 15]:
    contador = contador + 1
print(f"El número de elementos es {contador}")
'''

# Acumulador

'''
total = 0
for valor in [3 , 41 , 12 , 9 , 74 , 15]:
    total = total + valor
print(f"Total: {total}")
'''

# Máximo

'''
mayor = None
print(f'Antes {mayor}')
for valor in [3 , 41 , 12 , 9 , 74 , 15]:
    if mayor is None or valor > mayor:
        mayor=valor
    print('Bucle:' , valor , mayor)
print(f"Mayor: {mayor}")

'''

# Mínimo

menor = None
print(f'Antes {menor}')
for valor in [3 , 41 , 12 , 9 , 74 , 15]:
    if menor is None or valor < menor:
        menor=valor
    print('Bucle:' , valor , menor)
print(f"Menor: {menor}")