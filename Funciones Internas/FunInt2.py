# La función pass le ordena a Python que no tiene que hacer nada

edad = int(input("¿Cuántos años tiene? \n"))
if edad < 90:
    pass
else:
    print("¡No me lo creo!")
    print(f"¡¿Usted dice que tiene {edad} años!?")