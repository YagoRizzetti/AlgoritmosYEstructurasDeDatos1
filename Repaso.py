#Desarrollar un programa que cargue desde teclado los lados de dos triangulos 
#y determine el valor del mayor perimtro



def main():
    print("Ingrese los 3 lasdos del primer Triangulo:")
    t1l1 = int(input("Lado 1: "))
    t1l2 = int(input("Lado 2: "))
    t1l3 = int(input("Lado 3: "))

    print("Ingrese los 3 lasdos del Segundo Triangulo:")
    t2l1 = int(input("Lado 1: "))
    t2l2 = int(input("Lado 2: "))
    t2l3 = int(input("Lado 3: "))

    p1 = perimetro(t1)
    p2 = perimtero(t2)
    
    mp = mayor(p1,p2)

main()