# La forma más común de recorrer los elementos de una lista es con un bucle for. 
# Esto funciona bien si solamente necesitas leer los elementos de la lista. Pero si se quiere escribir o actualizar los elementos, se necesitan los índices. Una forma común de hacer eso es combinando las funciones range y len: 

listas = [15,26,"JUAN",["LUIS","PEDRO","LAURA"],(2,5,8)]

for lista in listas:
    print(lista)