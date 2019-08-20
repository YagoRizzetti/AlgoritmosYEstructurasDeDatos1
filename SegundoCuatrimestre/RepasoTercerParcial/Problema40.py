def buscar(v,num):
    for i in range(len(v)):
        if v[i] == num:
            return True
    return False

def generarVector(v1, v2):
    v3=[]
    for i in range(len(v1)):
        ban = buscar(v3,v1[i])
        if ban == False:
            for j in range(len(v2)):
                if v1[i] == v2[j]:
                    v3.append(v1[i])
                    break
    return v3

def main():
    n = int(input("Ingrese el tamaño del vector 1: "))
    m = int(input("Ingrese el tamaño del vector 2: "))
    v1 = [0] * n
    v2 = [0] * m
    cargarVector(v1)
    cargarVector(v2)
    v3 = generarVector(v1,v2)
    mostrarVector(v3)

main()