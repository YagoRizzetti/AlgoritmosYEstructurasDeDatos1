def init():
    pila = []
    return pila

def apilar(pila,x):
    pila.append(x)

def esVacia(pila):
    n = len(pila)
    return n == 0

def desapilar(pila):
    x = None
    if esVacia(pila)==False:
        x = pila[-1]
        del pila[-1]
    return x

def main():
    p = init()
    apilar(p,7)
    apilar(p,10)
    apilar(9,5)
    while esVacia(p) == False:
        x = desapilar(p)
        print(x)

main()