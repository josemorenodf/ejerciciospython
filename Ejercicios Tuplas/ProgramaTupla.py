# Escribir un programa que almacene en una tupla los siguientes precios: 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = (75, 46, 22, 80, 65, 8)

def mayor(precios):
    may=precios[0]
    for price in precios:
        if price>may:
            may=price
    print(f"El elemento mayor de la lista es {may}")

def menor(precios):
    men=precios[0]
    for price in precios:
        if price<men:
            men=price
    print(f"El elemento menor de la lista es {men}")

print(precios)
mayor(precios)
menor(precios)