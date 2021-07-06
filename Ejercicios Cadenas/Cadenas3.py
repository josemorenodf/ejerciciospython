# Ingresar un mail por teclado. Verificar si el string ingresado contiene solo un carácter "@".

mail=input("Ingrese un mail: ") 
cantidad=0 
x=0 
print("Longitud del correo: ", len(mail))
for x in range(len(mail)): 
    if mail[x]=="@": 
        cantidad=cantidad+1 
        x=x+1 

if (cantidad==1): 
    print("El mail ingresado contiene solo un caracter @") 
else: 
    print(f"Correo {mail} incorrecto")