from Generador import *

def main():
    v = cargarVectorDesdeArchivo("cuotas.dat")
    if len(v)==0:
        print("No se pudo cargar")
    else:
        opcion = mostrarMenu()
        while opcion != 0:
            if opcion == 1:
                mostrarVector(v)
            elif opcion == 2:
                socio = int(input("Socio: "))
                dep = int(input("Deporte: "))
                pos = buscar(v,socio,dep)
                dia = int(input("Dia: "))
                valor = int(input("Valor: "))
                if pos == -1:
                    v.append(Cuota(socio,dep,dia,valor))
                else:
                    v[pos].dia = dia
                    v[pos].monto = valor

main()