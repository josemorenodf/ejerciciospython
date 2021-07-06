"""Comandos de salida"""

# system.exit()

import sys

age = int(input("Ingrese su edad: "))
if age<18:
    sys.exit("Eres menor de edad") # Sale del programa
else:
    print("Eres mayor de edad")