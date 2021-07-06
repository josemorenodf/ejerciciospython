''' Cuando se escriben dos o más bucles seguidos, la costumbre es utilizar el mismo nombre de variable, 
puesto que cada bucle establece los valores de la variable sin importar los valores anteriores.
'''

for i in [0, 1, 2]:
    print(f"{i} * {i} = {i ** 2}")
print()
for i in [0, 1, 2, 3]:
    print(f"{i} * {i} * {i} = {i**3}")