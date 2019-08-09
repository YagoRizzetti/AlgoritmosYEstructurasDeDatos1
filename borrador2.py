print('-'*100)
print('BIENVENIDOS A TIENDA ELEGANCIA')
print('-'*100)

prendas = ('Remeras', 'Camisas', 'Pantalones', 'Faldas', 'Vestidos', 'Abrigos', 'Calzado')

precioSinPromo = 0
superPuntos = 0

#ARTICULO 1
tipoPrenda1 = int(input('Ingrese Codigo de la prenda seleccionada: 0=Remeras, 1=Camisas, 2=Pantalones, 3=Faldas, 4=Vestidos, 5=Abrigos, 6=Calzado: '))
prendaseleccionada1 = prendas[tipoPrenda1]
print(prendaseleccionada1)
precio1 = float(input('Ingrese precio: $'))
precioinicial1 = precio1
precioSinPromo = precioSinPromo + precio1

print("La prenda: ", tipoPrenda1,"participa de del plan SuperPuntos? s/n")
valor1 = input()
v1 = None
if(valor1 == "s"):
    v1 = 's'
    valor1 = precio1
    superPuntos = superPuntos + precio1
else:
    if(valor1 == "n"):
        v1 = "n"
        valor1 = 0

# ARTICULO 2
tipoPrenda2 = int(input('Ingrese Codigo de la prenda seleccionada: 0=Remeras, 1=Camisas, 2=Pantalones, 3=Faldas, 4=Vestidos, 5=Abrigos, 6=Calzado: '))
prendaseleccionada2 = prendas[tipoPrenda2]
print(prendaseleccionada2)
precio2 = float(input('Ingrese precio: $'))
precioinicial2 = precio2
precioSinPromo = precioSinPromo + precio2

print("La prenda: ", tipoPrenda2, "participa de del plan SuperPuntos? s/n")
valor2 = input()
v2 = None
if (valor2 == "s"):
    v2 = "s"
    valor2 = precio2
    superPuntos = superPuntos + precio2
else:
    if (valor2 == "n"):
        v2 = "n"
        valor2 = 0

# ARTICULO 3
tipoPrenda3 = int(input('Ingrese Codigo de la prenda seleccionada: 0=Remeras, 1=Camisas, 2=Pantalones, 3=Faldas, 4=Vestidos, 5=Abrigos, 6=Calzado: '))
prendaseleccionada3 = prendas[tipoPrenda3]
print(prendaseleccionada3)
precio3 = float(input('Ingrese precio: $'))
precioinicial3 = precio3
precioSinPromo = precioSinPromo + precio3

print("La prenda: ", tipoPrenda3, "participa de del plan SuperPuntos? s/n")
valor3 = input()
v3 = None
if (valor3 == "s"):
    v3 = "s"
    valor3 = precio3
    superPuntos = superPuntos + precio3
else:
    if (valor3 == "n"):
        v3 = "n"
        valor3 = 0

#PROMO 3X2
if tipoPrenda1 == tipoPrenda2 == tipoPrenda3:
    if precio1 < precio2 and precio1 < precio3:
        precio1 = 0
    else:
        if precio2 < precio3:
            precio2 = 0
        else:
            precio3 = 0

#PROMO 50%
if tipoPrenda1 == tipoPrenda2 and tipoPrenda1 != tipoPrenda3:
    if precio1 > precio2:
        precio1 = precio1 / 2
    else:
        precio2 = precio2 / 2

if tipoPrenda1 == tipoPrenda3 and tipoPrenda1 != tipoPrenda2:
    if precio1 > precio3:
        precio1 = precio1 / 2
    else:
        precio3 = precio3 / 2

if tipoPrenda2 == tipoPrenda3 and tipoPrenda2 != tipoPrenda1:
    if precio2 > precio3:
        precio2 = precio2 / 2
    else:
        precio3 = precio3 / 2

precioTotal = precio1 + precio2 + precio3
ahorro = precioSinPromo - precioTotal

#FORMA DE PAGO
formaDePago = int(input("Ingrese la forma de pago:/ 1=Contado/ 2=Tarjeta"))
montoAPagar = 0

if formaDePago == 1:
    formaDePago = "Contado (%10 de Descuento)"
    montoAPagar=precioTotal/100*90
else:
    if(formaDePago == 2):
        cuotas=int(input("ingrese en cuantas cuotas desea pagar:"))
        if(cuotas <= 3):
            formaDePago="Tarjeta (%2 de Recarga) cantidad de cuotas:", cuotas
            montoAPagar=precioTotal/100*102
        else:
            if(cuotas > 3):
                formaDePago="Tarjeta (%5 de Recarga) cantidad de cuotas:", cuotas
                montoAPagar=precioTotal/100*105
            else:
                if(cuotas <= 0):
                    formaDePago="Contado (%10 de Descuento)"
                    montoAPagar=precioTotal/100*90

if valor1 > 0 and valor2 > 0 and valor3 > 0:
    superPuntos = superPuntos * 2

print("----------------------------------------------------")
print("Tienda Elegancia")
print("Tipo, Precio, SuperPuntos")
print(prendaseleccionada1 , precioinicial1, v1)
print(prendaseleccionada2 , precioinicial2 , v2)
print(prendaseleccionada3 , precioinicial3 , v3)
print("Total sin promo: ", precioSinPromo)
print("Ahorro: ", ahorro)
print("Total Con Promo: ", precioTotal)
print("Forma de Pago: ", formaDePago)
print("Monto a Pagar: ", montoAPagar)
print("Usted obtiene: ", superPuntos, "SuperPuntos")
print("----------------------------------------------------")