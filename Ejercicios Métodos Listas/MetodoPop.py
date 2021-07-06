# Eliminando elementos
# Se puede obtener el dato que fue eliminado

nombre = ["Juan","Ivan","Pedro","Luis","Hector","Esteban","Juan","Marcos","Juan"]
print(nombre)
x = nombre.pop(2)
print("Lista después de aplicar el método .pop:")
print(nombre)
print(f"El elemento eliminado fue {x}")