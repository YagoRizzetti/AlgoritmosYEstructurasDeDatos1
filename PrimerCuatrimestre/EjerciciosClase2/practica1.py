articulo="s"
precio=0
nombre=None
while(articulo=="s"):
    print("Ingrese el nombre del articlo:")
    nombre=raw_input()
    print("ingrese el precio del articulo")
    precio=float(input())
    print("precio de contado-->1 , precio con tarjeta-->2")
    tipoDePago=input()
    if(tipoDePago==1):
        print("El precio de ", nombre, "contado es: ", precio/100*90)
        print("Desea cargar un nuevo producto? s/n")
        articulo=raw_input()
    if(tipoDePago==2):
        print("El precio de ", nombre, "contado es: ", precio/100*105)
        print("Desea cargar un nuevo producto? s/n")
        articulo=raw_input()
    else:
        print("precio de contado-->1 , precio con tarjeta-->2")
        