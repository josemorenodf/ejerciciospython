# Calcular la distancia de 2 puntos en el plano cartesiano. 
# a(1,7)  
# b(4,3)  
# d = sdrt((x2-x1) al cuadrado + (y2-y1) al cuadrado)

import math 

# Datos de a y b 

x1 = -4
y1 = -3
x2 = 2
y2 = 5

#Operaciones

x = x2-x1
y = y2-y1
z = math.pow(x,2) + math.pow(y,2)
d= math.sqrt(z)
print(f"La distancia de 2 puntos a({x1},{y1}) y b({x2},{y2}) en el plano cartesiano es: {d} ")