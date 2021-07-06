# Crear y cargar una lista con los nombres de tres alumnos. Cada alumno tiene dos notas, almacenar las notas en una lista paralela. Cada componente de la lista paralela debe ser también una lista con las dos notas. Imprimir luego cada nombre y sus dos notas.

nombres=[] 
notas=[] 
for x in range(3): 
    nombre=input("Ingrese el nombre del alumno: ") 
    nombres.append(nombre) 
    nota1=int(input("Ingrese la primer nota: ")) 
    nota2=int(input("Ingrese la segunda nota: ")) 
    notas.append([nota1,nota2]) 
for x in range(3): 
    print(f"{nombres[x]} obtuvo las siguientes 2 notas: {notas[x][0]} (nota 1) y {notas[x][1]} (nota 2)") 