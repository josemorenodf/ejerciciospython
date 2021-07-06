# También se puede usar el constructor de la clase dict() de varias maneras, para crear diccionarios: 

# 1. Argumentos con nombre
print("1. Argumentos con nombre")
d2 = dict(uno=1, dos=2, tres=3)
print(d2)
print()
# 2. Pares clave: valor encerrados entre llaves
print("2. Pares clave: valor encerrados entre llaves")
d3 = dict({'uno': 1, 'dos': 2, 'tres': 3})
print(d3)
print()
# 3. Iterable que contiene iterables con dos elementos
print("3. Iterable que contiene iterables con dos elementos")
d4 = dict([('uno', 1), ('dos', 2), ('tres', 3)])
print(d4)
print()
# 4. Diccionario vacío usando el constructor
print("4. Diccionario vacío usando el constructor")
d6 = dict()
print(d6)
print()