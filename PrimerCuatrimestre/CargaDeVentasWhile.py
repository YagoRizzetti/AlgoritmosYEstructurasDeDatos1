cantDeVentasDelMes = int(input("Ingrse la cantidad de ventas en x mes(Ingrese '-1' Para terminar): "))

cant0=False
cant1=0
cant2=0
cant3=0
acumulador=0

while cantDeVentasDelMes != -1 :
    if cantDeVentasDelMes >= 0 :
        if cantDeVentasDelMes < 10000 :
            cant1 += 1
            if cantDeVentasDelMes == 0 and cant0 == False :
                cant0=True
        else:
            if cantDeVentasDelMes < 15000 :
                cant2 += 1
            else: 
                if cantDeVentasDelMes > 15000 :
                    cant3 += 1
        acumulador += cantDeVentasDelMes            
        cantDeVentasDelMes = int(input("Ingrse la cantidad de ventas en x mes(Ingrese '-1' Para terminar): "))
    else:
        cantDeVentasDelMes = int(input("ERROR Ingrse la cantidad de ventas POSITIVAS en x mes(Ingrese '-1' Para terminar): "))

if cant0 == True :
    print("se ingresaron al menos en un mes una cantidad cero de ventas")
else:
    print("No hubo cantidad de de ventas iguales a cero")

print("La cantidad total de automoviles que se vendieron es: ", acumulador)
print("hubo una cantidad ", cant1 , "de meses en los que se vendieron entre 1 y 10000 autos")
print("hubo una cantidad ", cant2 , "de meses en los que se vendieron entre 10000 y 15000 autos")
print("hubo una cantidad ", cant2 , "de meses en los que se vendieron mas 15000 autos")