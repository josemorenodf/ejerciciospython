# Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos RETORNE su superficie.

def retornar_superficie(lado):
    sup=lado*lado
    return sup

# Bloque principal del programa

valor=int(input("Ingrese el valor del lado del cuafrado: "))
superficie=retornar_superficie(valor)
print("La superficie del cuadrado es",superficie)