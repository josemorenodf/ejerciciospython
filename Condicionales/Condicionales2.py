# Programa para convertir una temperatura desde grados Fahrenheit a grados Celsius

# De forma normal:

"""fahrenheit = float(input("Introduzca la temperatura en grados Fahrenheit: "))
celsius = (fahrenheit-32) * 5 / 9
print(round(celsius))"""

# Para que no genere errores:

entrada = input("Introduzca la temperatura en grados Fahrenheit: ")
try:
    fahrenheit = float (entrada)
    celsius = (fahrenheit-32) * 5 / 9
    print(celsius)
except:
    print("Por favor, introduzca un número.")