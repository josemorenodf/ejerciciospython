# Para crear una tupla en Python simplemente hay que definir una secuencia de elementos separados por comas.
# La forma de crear una tupla sin paréntesis es conocida como tuple packing (algo así como empaquetado de tuplas).

numeros = 1, 2, 3, 4, 5
print(numeros)
print("************")
elementos = 3, 'a', 8, 7.2, 'hola'
print(elementos)
print("************")
tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'
print(tup)
print("************")
y = (20,30,40,50,60,70)
print(y)
print("************")

# Para crear una tupla vacía: usar paréntesis
x = ()
print(x)

# Para determinar la longitud de una tupla: usar len(tupla)
print("La longitud de la tupla es",len(tup))