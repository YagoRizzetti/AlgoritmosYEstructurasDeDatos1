operacion="si"

while(operacion=="si"):
    print("ingrese el primer numero:")
    a=input()
    print("Ingrese el segundo numero:")
    b=input()
    print("Tipee 1 si desea dividir el primero por el segundo, Tipee 2 si desea dividir el segundo por el primero")
    respuesta1=input()
    if(respuesta1==1):
        print("El resultado es: ", a/b)
        print("Desea saber el resto? si/no:")
        resto=raw_input()
        if(resto=="si"):
            print("El resto es:", a%b)
            print("Desea realizar una nueva operacion? si/no:")
            operacion=raw_input()
        else:     
            print("Desea realizar una nueva operacion? si/no:")
            operacion=raw_input()
    else:
        print("El resultado es: ", b/a)  
        print("Desea saber el resto? si/no:")
        resto=raw_input()
        if(resto=="si"):
            print("El resto es:", b%a)
            print("Desea realizar una nueva operacion? si/no:")
            operacion=raw_input()
        else:     
            print("Desea realizar una nueva operacion? si/no:")
            operacion=raw_input()  
if(operacion=="no"):
    print("adios")