numero = int(input("Ingresa un numero: "))
n = numero
l = []
suma = 0
l.append(numero)
suma += numero
while numero != 1:
    if numero % 2 == 0:
        numero = int(numero / 2)
        l.append(numero)
        suma += numero
    else:
        numero = int((numero * 3) + 1)
        l.append(numero)
        suma += numero

longitud = len(l)
promedio = suma/longitud

print("numero = " + str(n))
print("orbita del numero : ", l)
print("longitud del numero : " + str(longitud))
print("Promedio:" + str(promedio))
l.sort(reverse = True)
print("el mayor numero es:" + str(l[0]))