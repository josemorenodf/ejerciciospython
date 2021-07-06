# Acceder a los elementos de una tupla

tupla = ('a', 'b', 'd')
print(tupla)

# Primer elemento de la tupla = Índice 0
print(tupla[0])

# Segundo elemento de la tupla = Índice 1
print(tupla[1])
print("********************************")

# Acceso a los elementos usando un índice negativo
print("Acceso a los elementos usando un índice negativo")
bebidas = ('agua', 'café', 'batido', 'sorbete')
print(bebidas)
print(bebidas[-1])
print(bebidas[-3])

# Acceso a un subconjunto de elementos
print("Acceso a un subconjunto de elementos")
vocales = 'a', 'e', 'i', 'o', 'u'
print("Elementos desde el índice 2 hasta el índice 3-1")
print(vocales[2:3]) # Elementos desde el índice 2 hasta el índice 3-1
print("Elementos desde el 2 hasta el índice 4-1")
print(vocales[2:4]) # Elementos desde el 2 hasta el índice 4-1
print("Todos los elementos")
print(vocales[:]) # Todos los elementos
print("Elementos desde el índice 1")
print(vocales[1:]) # Elementos desde el índice 1
print("Elementos hasta el índice 3-1")
print(vocales[:3]) # Elementos hasta el índice 3 (iniciando en 0)