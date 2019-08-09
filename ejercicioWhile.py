#Desarrollar un programa que carge desde teclado una serie de 
#numeros y determine el promedio de los numeros negativos ingresados. 
#El fin de carga de datos se indica al ingresar el valor 0(cero)

numero = float(input("ingrese un numero distinto de cero:"))
cantNumNeg=0
totalNumNeg=0

while numero != 0:
    if numero < 0:
        cantNumNeg += 1
        totalNumNeg += numero
    numero = float(input("ingrese un numero distinto de cero:"))

promedio = totalNumNeg/cantNumNeg
print("el promedio de numeros negativos es: ", promedio)   
 