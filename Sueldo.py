print("Sueldos por mes")

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Nomviembre","Diciembre")

primero = True
total = 0

for i in meses:
    sueldo = float(input("ingrese el valor del sueldo en el mes: " + i))
    print("El sueldo del mes: ", i, "es de: ", sueldo)

    if primero == True:
        mayor = (sueldo, i)
        menor = (sueldo, i)
        primero = False
    else:
        if sueldo > mayor:
            mayor = (sueldo, i)

        if sueldo < menor:
            menor = (sueldo, i)

aginaldo = round(mayor / 2, 2)
promedio = round(total /2, 2)

print("El mayor sueldo es de: ", menor[0], "en el mes: ", menor[1] )
print("El mayor sueldo es de: ", mayor[0], "en el mes: ", mayor[1] )
print("El aginaldo es de: ", aginaldo )