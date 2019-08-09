#carge n valores desde teclado y determine la cantidad de numeros negativos ingresados.
#El valor de n es informado al comienzo del programa

a=0
n= int(input("ingrese la cantidad de numeros que va a ingresar"))

for i in range(n):
    num = int(input("ingrese el siguiente numero"))
    if num < 0:
        a += 1

print("Cantidad de negativos cargados: ", a)