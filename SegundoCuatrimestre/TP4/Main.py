from Registro import *
from Funciones import *
from Archivos import *

def main():
    n = int(input("Ingrese una cantidad de Articulos mayor que cero(0): "))
    while n <= 0:
        print("ERROR!. La cantidad ingresada no es valida")
        n = int(input("Ingrese una cantidad de Articulos mayor que cero(0): "))                
    v = [None] * n
    generarArticulos(v)
    mostrarV(v)
    abc = "MisCompras.dat"
    atc = "MisCompras.txt"
    abf = "Favoritos.dat"
    fav = []
    a = False 
    o = 0
    while o != 6:
        print("\033[1;35m" + "\033[4;35m" + "_"*100 + "\033[0;35m" + "\033[1;35m")
        print("                                            MENU PRINCIPAL")
        print("\033[1;35m" + "\033[4;35m" + "_"*100 + "\033[0;36m" + "\033[1;36m" + "\n")
        print("1- Comprar")
        print("2- Ver las compras efectuadas en un intervalo de fechas")
        print("3- Ver todos los articulos en un Rango de Precio ")
        print("4- Agregar un nuevo articulo favorito")
        print("5- Actualizar la lista de Articulos Favoritos")
        print("6- Salir")
        o = int(input("Elija una opcion del menu: "))
        if o == 1:
            num = validarEntre("Ingrese el numero de identificacion del articulo que desea buscar: ", 0, n)
            art = buscarPorIdentificador(v, num)
            if art == -1:
                print("No se a podido encontrar el Articulo.")
            else:
                a = validarStock(v,art,abc,atc,a)
        elif o == 2:
            intervaloFechas(abc)
        elif o == 3:
            menYMay(v)
        elif o == 4:
            num = validarEntre("Ingrese el numero de identificacion del articulo que desea buscar: ", 0, n)
            articulo = buscarPorIdentificador(v, num)
            if articulo == -1:
                print("No se a podido encontrar el Articulo.")
            else:
                print("Articulo Encontrado!.")
                writeArticulo(v[articulo])
                agregarFavorito(v[articulo], fav)
        elif o == 5:
            a = True
            actualizarFavoritos(abf,fav)
            print("\nArticulos Favoritos actualizados con Exito.\n")
            m = validarEntre("Desea ver los articulos favoritos actualizados?: \n 1 = SI \n 2 = NO \n",0,3)
            if m == 1:
                favoritosActualizados(abf)
    if a == False:
        print("Gracias Vuelva Pronto!.")
    else:
        print("Desea borrar los archivos generados durante esta ejecucion?\n","1-Si\n","2-No")
        borrar = int(input())
        while borrar < 1 or borrar > 2:
            print("ERROR!. Ingrese una opcion valida")        
            print("Desea borrar los archivos generados durante esta ejecucion?\n","1-Si\n","2-No")
            borrar = int(input())
        if borrar == 1:
            if os.path.exists(abc):
                os.remove(abc)
            if os.path.exists(atc):
                os.remove(atc)
            if os.path.exists(abf):
                os.remove(abf)
            print("Gracias Vuelva Pronto!.")
        else:            
            print("Gracias Vuelva Pronto!.")


if __name__ == "__main__":
    main()

