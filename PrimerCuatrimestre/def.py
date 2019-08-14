def menor(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        men = n1
    else:
        if n2 < n3:
            men = n2
    else:
        men = n3

    return men

def calcular(men):
    cuadrado = men ** 2
    cubo = men ** 3
    
    return cuadrado , cubo

def test():
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))

    var = menor(a, b, c)
    res = calcular(var)

    print("el numero menor es: ", var)
    print("el cuadrado del numero ", var ,"es: " res[0] )
    print("el cubo del numero ", var ,"es: " res[1] )

test()