# Recoger entradas de texto del usuario hasta que éste escriba fin. 

while True:
    linea=input('> ')
    if linea == 'Fin':
        break
    print(linea)
print('Terminado.')