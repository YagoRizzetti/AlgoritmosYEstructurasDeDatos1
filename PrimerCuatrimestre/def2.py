def may_men(a,b):
    if a>b:
        may = a
        men = b
    else:
        may = b
        men = a
    return may , men

def areaCuadrado(lado):
    res = lado ** 2
    return res

def areaCirculo(radio):
    res = 3,14 * radio ** 2
    return res

def test():
    n1=int(input("ingrese el valor del primer numero: "))
    n2=int(input("ingrese el valor del segundo numero: "))

    res = may_men(n1, n2)

    supCuadrado = areaCuadrado(res[0])
    supCirculo = areaCirculo(res[1])
    
    print("el area del cuadrado es de: ", supCuadrado)
    print("el area del circulo es de: ", supCirculo)

test()