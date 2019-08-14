#Desarrollar un programa que carge las notas de n parciales(siendo n un valor que se informa 
#inicialmente en el programa) y, determine el porcentaje de parciales aprobados.

aprobados=0
porcentajeAprobados=0

cant = int(input("ingrese la cantidad de notas a cargar: "))

while cant <= 0 :
    cant = int(input("ERROR ingrese la cantidad de notas MAYORES A 0 a cargar: "))

for i in range(cant):
    nota = int(input("ingrese una nota: "))
    while nota < 0 or nota > 10 :
        print("ERROR")    
        nota = int(input("ingrese una nota: "))
    if nota >= 4 :
        aprobados += 1

porcentajeAprobados=aprobados*100/cant

print("El porcentaje de notas aprobadas es de: ", porcentajeAprobados)