# Confeccionar un programa que permita cargar los nombres de 5 alumnos y sus notas respectivas. Luego ordenar las notas de mayor a menor. Imprimir las notas y los nombres de los alumnos.

alumnos=[] 
notas=[] 

for x in range(5): 
    nombre=input("Ingrese el nombre del alumno: ") 
    alumnos.append(nombre) 
    nota=int(input("Ingrese la nota de dicho alumno: ")) 
    notas.append(nota) 

for k in range(4): 
    for x in range(4-k): 
        if notas[x]<notas[x+1]: 
            aux1=notas[x] 
            notas[x]=notas[x+1] 
            notas[x+1]=aux1 
            aux2=alumnos[x] 
            alumnos[x]=alumnos[x+1] 
            alumnos[x+1]=aux2 

print("Lista de alumnos y sus notas ordenadas de mayor a menor:") 
for x in range(5): 
    print(f"{alumnos[x]} obtuvo una nota de {notas[x]}") 
