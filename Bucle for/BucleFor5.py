'''
La variable de control puede ser una variable empleada antes del bucle. 
El valor que tuviera la variable no afecta a la ejecución del bucle, pero cuando termina el bucle, 
la variable de control conserva el último valor asignado
'''

i = 10
print(f'El bucle no ha comenzado. Ahora i vale {i}')
for i in [0, 1, 2, 3, 4]:
    print(f"{i} * {i} = {i ** 2}")
print(f'El bucle ha terminado. Ahora i vale {i}')