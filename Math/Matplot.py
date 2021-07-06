import math 
import matplotlib.pyplot as plt

# Función seno

x1 = []
y1 = []
for i in range(0,360,1):
    angulo = math.radians(i)
    x1.append(angulo)
    y1.append(math.sin(angulo))
plt.plot(x1,y1)
plt.ylabel('Funcion seno')
plt.show()

# Función coseno

x = []
y = []
for i in range(0,360,1):
    angulo = math.radians(i)
    x.append(angulo)
    y.append(math.cos(angulo))
#print(x)
#print(y)
plt.plot(x,y)
plt.ylabel('Funcion coseno')
plt.show()