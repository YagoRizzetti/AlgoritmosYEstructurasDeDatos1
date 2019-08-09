#Desarrollar un progrma en python que permita cargar por teclado un texto completo.
#Siempre se supone que el usuario cargara un punto para indicar el final del texto, y que cada palabra
#de ese texto esta separada de las demas por un espacio en blanco. El programa debe:

#1-Determinar cuantas palabras tiene al menos una vocal
#2-Determinar cuantas palabras contuvieron una o mas veces la expresion "ta".


def esVocal(car):
    car= car.lower()
    if car == "a" or car =="e" or car == "i" or car == "o" or car == "u":
        return True
    else:
        return False

def  test():
    ban = False
    count = 0 
    txt = input("Ingrese texto: ")
    for car in txt:
        if car != " " and car != ".":
            res = esVocal(car)
            if res == True:
                ban = True
        else:
            if ban == True:
                ban = False
                count +=1
    print("La cantidad de palabras que tienen vocales dentro del texto ingresado son: ", count)

test()