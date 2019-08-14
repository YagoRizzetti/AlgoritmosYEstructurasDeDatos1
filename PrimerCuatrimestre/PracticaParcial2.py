#1 Cantidad de palabras que tienen 'x' o 'X' en la primera mitad de la palabra
#2 Cantidad de palabras que comienzan con la ultima letra de laalabra anterior.
#3 Indicar con un mensaje si en el texto hay mas vocales que digitos (esVocal(car), esDigito(car), porcentaje(x,total))
#4 Porcentaje de palabras que comienzan y terminan con el mismo caracter.


def palabrasx(x):
    cp = 0
    cl = 0
    countpalx = 0
    tienex = False

    for i in x:
        if i == " " or i == ".":
            cp +=1
            if tienex:
                mit = cl / 2
                if x <= mit:
                    countpalx += 1
                    tienex = False
            cl = 0
        else:
            cl +=1
            if tienex == False and (i == "x" or i == "X"):
                x = cl
                tienex = True

    return countpalx

def main():
    text = input("Ingrese un texto que termine con un punto: ")

    tex = palabrasx(text)
    print(tex)

main()