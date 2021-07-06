# un bucle que repite lo que recibe como entrada hasta que el usuario escribe “fin”, pero trata las líneas que empiezan por el carácter almohadilla como líneas que no deben mostrarse en pantalla.

while True:
    linea=input('> ')
    if linea[0] == '#':
        continue
    if linea == 'fin':
        break
    print(linea)
print('Terminado.')