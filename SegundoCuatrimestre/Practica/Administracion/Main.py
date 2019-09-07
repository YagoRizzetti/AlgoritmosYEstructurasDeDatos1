#Cargar el arreglo pedido con los datos de los n resultados. Validar que el código del cargo se 
#encuentre entre 0 y 19. 

#Mostrar los datos de los concursantes que hayan aprobado el examen (se aprueba con 70 puntos o más). 

#Determinar cuántos concursantes rindieron el examen por cada tipo de cargo (es decir, 
#cuántos concursantes rindieron por el cargo 0, cuántos por el cargo 1, cuántos por el cargo 2,
#etc... hasta el cargo 19). 

#Mostrar los datos del arreglo, ordenados de mayor a menor, por el puntaje obtenido en el examen. 

#Cargar por teclado el nombre de un postulante, y mostrar por pantalla todos los datos del mismo si
#se encuentra en el vector. Si este postulante además aprobó el concurso, muestre un mensaje que 
#resalte ese resultado además de sus datos. Informe con otro mensaje si el postulante no se encuentra 
#en el vector.

def main():
    n = int(input("Ingrese La Cantidad de Examenes: "))
    v = [None] * n
    o = -1
    while o != 6:
        print("1-Cargar los datos de los " + str(n) + " Examenes")
        print("2-Ver los concursantes que aprobaron")
        print("3-Ver cuantos concursantes rindieron por cada Cargo")
        print("4-Ver todos los datos ordenados por puntaje de mayor a menor")
        print("5-Ver los datos de algun Concursante en especifico")
        print("6-Salir")
        

main()