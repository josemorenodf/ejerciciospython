# Rebanado de listas 

t = ["a","b","c","d","e","f"]
print(t)
print("Aplicando t[1:4]: ",t[1:4])   
print("Aplicando t[2:100] (no genera error):",t[2:100])   

print("Imprime la lista completa:",t[:]) 

# Un operador de rebanado al lado izquierdo de una asignación puede actualizar múltiples elementos: 

print("Lista completa antes de la asignacion:",t)
t[1:3] = ["x","y"]
print("Lista modificada:",t)
t[5:7] = ["x","y","x","k","m","r"]
print("Lista modificada t[5:7]:",t)