# Se tiene que cargar la siguiente información: 1. Nombres de 3 empleados 2. Ingresos en concepto de sueldo, cobrado por cada empleado, en los últimos 3 meses. 
 
# Confeccionar el programa para:

# a) Realizar la carga de los nombres de empleados y los tres sueldos por cada empleado. b) Generar una lista que contenga el ingreso acumulado en sueldos en los últimos 3 meses para cada empleado. c) Mostrar por pantalla el total pagado en sueldos a cada empleado en los últimos 3 meses) Obtener el nombre del empleado que tuvo el mayor ingreso acumulado.

nombres=[] 
sueldos=[] 
totalsueldos=[] 
for x in range(3): 
    nombre=input("Ingrese el nombre del empleado: ") 
    nombres.append(nombre) 
    sueldo1=int(input("Ingrese el primer sueldo: ")) 
    sueldo2=int(input("Ingrese el segundo sueldo: ")) 
    sueldo3=int(input("Ingrese el tercer sueldo: ")) 
    sueldos.append([sueldo1, sueldo2, sueldo3]) 
for x in range(3): 
    total=sueldos[x][0]+sueldos[x][1]+sueldos[x][2] 
    totalsueldos.append(total) 
for x in range(3): 
    print(f"{nombres[x]} obtuvo un salario total de {totalsueldos[x]} en los últimos 3 meses") 
    posmayor=0 
    mayor=totalsueldos[0] 
for x in range(1,3): 
    if totalsueldos[x]>mayor: 
        mayor=totalsueldos[x] 
        posmayor=x 
print(f"Empleado con mayores ingresos en los ultimos tres meses: {nombres[posmayor]}, percibiendo un ingreso de {mayor}") 