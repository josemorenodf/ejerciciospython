# Eliminando elementos

t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x = t.pop(3) # Modifica la lista y regresa el elemento que fue removido
print(x) 
print("Aplicando el método .pop:")   
print(t)  

# Si no se necesita el valor removido, se puede usar el operador del:

del t[1]
print("Aplicando el operador del:")   
print(t)

# Si se sabe cual elemento se quiere remover (pero no conoce el índice), se puede usar remove: 

t1 = ["a","b","c","d","e","f","g","h"]
t1.remove("b")
print("Aplicando el método .remove")
print(t1)

# Para remover más de un elemento, se puede usar 'del' con un índice de rebanado:

print("Lista antes de aplicar del t[2:4]:",t)
del t[2:4]
print("Aplicando el operador del para remover más de un elemento:")   
print(t)